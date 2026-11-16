"""Render the vault's graphs as static SVGs.

A graph is a small text spec in the Obsidian Desmos plugin's syntax, saved as
`Assets/<name>.desmos`. This script draws each spec with matplotlib and writes
`Assets/<name>.svg` next to it. Notes embed the SVG as an image, so the graph
shows up in Obsidian, on GitHub, and on the MkDocs site without any plugin.

    python tools/figures.py                 # redraw every spec whose SVG is stale
    python tools/figures.py --all           # redraw everything
    python tools/figures.py --convert NOTE  # turn a note's desmos-graph blocks
                                            # into specs + SVGs + image links
    python tools/figures.py --check         # report specs that fail, write nothing

Supported spec lines (one per line, fields split on `|`):
    y=f(x)        explicit curve          x=g(y) or x=c   sideways curve / vertical line
    F(x,y)=G(x,y) implicit curve          (a,b)           point (`open` for hollow)
    y\\ge f(x)     shaded region           k=2, k=[1,2,3]  constant / one curve per value
Fields after the expression: restrictions (`x>=0`, `0<x<2`), `dashed`,
`dotted`, `open`, and a `#rrggbb` colour.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".github", ".obsidian", "venv", ".venv", "_docs", "_site", "node_modules"}
BLOCK = re.compile(r"```desmos-graph\n(.*?)```[ \t]*\n?", re.S)
PALETTE = ["#2d70b3", "#c74440", "#388c46", "#fa7e19", "#6042a6", "#000000"]
FUNCS = {"ln": "np.log", "log": "np.log10", "sin": "np.sin", "cos": "np.cos", "tan": "np.tan",
         "exp": "np.exp", "sqrt": "np.sqrt", "arctan": "np.arctan", "abs": "np.abs",
         "sinh": "np.sinh", "cosh": "np.cosh", "tanh": "np.tanh"}

# ---------------------------------------------------------------- LaTeX -> numpy

TOKEN = re.compile(
    r"\s*(?:(?P<num>\d+\.?\d*|\.\d+)|(?P<cmd>\\[A-Za-z]+)"
    r"|(?P<id>[A-Za-z](?:_(?:\{[A-Za-z0-9]+\}|[A-Za-z0-9]))?)|(?P<op>[-+*/^(){},=]))"
)


def tokenize(src: str) -> list[tuple[str, str]]:
    src = src.replace("\\left", "").replace("\\right", "").replace("\\cdot", "*")
    src = src.replace("\\,", " ").replace("\\ ", " ").replace("\\pi", " pi ")
    out, i = [], 0
    while i < len(src):
        if src[i].isspace():
            i += 1
            continue
        m = TOKEN.match(src, i)
        if not m:
            raise ValueError(f"cannot read {src[i:i+12]!r}")
        kind = m.lastgroup
        text = m.group(kind)
        if kind == "id":
            text = text.replace("{", "").replace("}", "")
            # `pi` arrives as two single-letter ids; glue it back together
            if text == "i" and out and out[-1] == ("id", "p"):
                out[-1] = ("id", "pi")
                i = m.end()
                continue
        out.append((kind, text))
        i = m.end()
    return out


class Parser:
    """Recursive-descent translator from Desmos LaTeX to a numpy expression."""

    def __init__(self, tokens):
        self.t, self.i, self.names = tokens, 0, set()

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None)

    def take(self, text=None):
        kind, val = self.peek()
        if text is not None and val != text:
            raise ValueError(f"expected {text!r}, got {val!r}")
        self.i += 1
        return val

    def expr(self):
        kind, val = self.peek()
        sign = self.take() if val in ("+", "-") else ""
        left = ("-" if sign == "-" else "") + self.term()
        while self.peek()[1] in ("+", "-"):
            op = self.take()
            left = f"{left}{op}{self.term()}"
        return f"({left})"

    def term(self):
        left = self.power()
        while True:
            kind, val = self.peek()
            if val in ("*", "/"):
                self.take()
                left = f"{left}{val}{self.power()}"
            elif kind in ("num", "id", "cmd") or val in ("(", "{"):
                left = f"{left}*{self.power()}"  # implicit multiplication
            else:
                return left

    def power(self):
        base = self.atom()
        if self.peek()[1] == "^":
            self.take()
            base = f"({base}**{self.arg()})"
        return base

    def arg(self):
        """One argument: a braced group, or a single atom (with unary minus)."""
        if self.peek()[1] == "{":
            return self.group("{", "}")
        if self.peek()[1] == "-":
            self.take()
            return f"(-{self.atom()})"
        return self.atom()

    def group(self, open_, close):
        self.take(open_)
        inner = self.expr()
        self.take(close)
        return inner

    def atom(self):
        kind, val = self.peek()
        if kind == "num":
            self.take()
            return val
        if kind == "id":
            self.take()
            if val == "e":
                return "np.e"
            if val == "pi":
                return "np.pi"
            self.names.add(val)
            return f"V[{val!r}]"
        if val == "(":
            return self.group("(", ")")
        if val == "{":
            return self.group("{", "}")
        if val == "-":
            self.take()
            return f"(-{self.power()})"
        if kind == "cmd":
            self.take()
            name = val[1:]
            if name == "frac":
                return f"({self.group('{', '}')}/{self.group('{', '}')})"
            if name == "sqrt":
                return f"np.sqrt({self.group('{', '}')})"
            if name in ("max", "min"):
                self.take("(")
                args = [self.expr()]
                while self.peek()[1] == ",":
                    self.take()
                    args.append(self.expr())
                self.take(")")
                return f"np.{name}imum.reduce(np.broadcast_arrays({','.join(args)}))"
            if name in FUNCS:
                exponent = None
                if self.peek()[1] == "^":  # \sin^{2}(x)
                    self.take()
                    exponent = self.arg()
                inner = self.group("(", ")") if self.peek()[1] == "(" else self.power_chain()
                call = f"{FUNCS[name]}({inner})"
                return f"({call}**{exponent})" if exponent else call
            raise ValueError(f"unsupported command {val}")
        raise ValueError(f"unexpected {val!r}")

    def power_chain(self):
        """Argument of a function written without parentheses: \\sin 2x."""
        left = self.power()
        while self.peek()[0] in ("num", "id") or self.peek()[1] == "{":
            left = f"{left}*{self.power()}"
        return left


def compile_expr(src: str):
    """Return (python_source, names_used) for one LaTeX expression."""
    p = Parser(tokenize(src))
    code = p.expr()
    if p.i != len(p.t):
        raise ValueError(f"trailing {p.t[p.i][1]!r} in {src!r}")
    return code, p.names


def evaluate(src: str, env: dict):
    code, _ = compile_expr(src)
    with np.errstate(all="ignore"):
        return eval(code, {"np": np, "V": env})  # noqa: S307 - our own generated source


# ---------------------------------------------------------------- spec parsing

def split_top(text: str, sep: str) -> list[str]:
    """Split on `sep` outside brackets."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        depth += ch in "([{"
        depth -= ch in ")]}"
        if ch == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    return parts + [cur]


def parse_spec(text: str):
    head, _, body = text.partition("---") if "---" in text else ("", "", text)
    settings = {}
    for item in re.split(r"[;\n]", head):
        if "=" in item:
            key, val = item.split("=", 1)
            settings[key.strip()] = val.strip()
    params, items = {}, []
    for raw in body.strip().splitlines():
        raw = raw.strip()
        if not raw:
            continue
        fields = [f.strip() for f in raw.split("|")]
        expr = re.sub(r"\\ge(?![a-z])", ">=", re.sub(r"\\le(?![a-z])", "<=", fields[0]))
        item = {"expr": expr, "color": None, "style": "-", "open": False, "limits": [], "raw": raw}
        for f in fields[1:]:
            if f.startswith("#"):
                item["color"] = f
            elif f == "dashed":
                item["style"] = "--"
            elif f == "dotted":
                item["style"] = ":"
            elif f == "open":
                item["open"] = True
            elif f:
                item["limits"].append(f)
        m = re.fullmatch(r"([A-Za-z](?:_\{?[A-Za-z0-9]+\}?)?)\s*=\s*(.+)", expr)
        name = m.group(1).replace("{", "").replace("}", "") if m else None
        if m and name not in ("x", "y") and len(fields) == 1:
            params[name] = m.group(2)
        else:
            items.append(item)
    return settings, params, items


def names_in(src: str) -> set:
    """Every variable or parameter name that appears in a piece of a spec line."""
    try:
        return {val for kind, val in tokenize(re.sub(r"<=|>=|<|>|\\[|\\]", ",", src)) if kind == "id"}
    except ValueError:
        return set()


def envs_for(used: set, params: dict) -> list[dict]:
    """Parameter values for one spec line.

    A line that mentions a list-valued parameter (directly or through another
    definition) is drawn once per value; lists used together are paired up.
    """
    needed, frontier = set(), set(used)
    while frontier:
        name = frontier.pop()
        if name in params and name not in needed:
            needed.add(name)
            frontier |= names_in(params[name])
    lists = {n: [float(evaluate(v, {})) for v in split_top(params[n][1:-1], ",")]
             for n in needed if params[n].startswith("[")}
    count = min((len(v) for v in lists.values()), default=1)
    envs = []
    for j in range(count):
        env = {k: v[j] for k, v in lists.items()}
        todo = {n: params[n] for n in needed if n not in lists}
        for _ in range(len(todo) + 1):
            for name, src in list(todo.items()):
                try:
                    env[name] = float(evaluate(src, env))
                    del todo[name]
                except KeyError:
                    pass
        if todo:
            raise ValueError(f"undefined parameter in {sorted(todo)}")
        envs.append(env)
    return envs


# ---------------------------------------------------------------- drawing

def limit_mask(limits, env, X, Y):
    mask = np.ones(np.broadcast(X, Y).shape, dtype=bool)
    for lim in limits:
        parts = re.split(r"(<=|>=|<|>)", lim)
        vals = [evaluate(p, {**env, "x": X, "y": Y}) for p in parts[0::2]]
        for a, op, b in zip(vals, parts[1::2], vals[1:]):
            mask &= {"<": np.less, "<=": np.less_equal, ">": np.greater, ">=": np.greater_equal}[op](a, b)
    return mask


def draw(text: str, out: Path):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"svg.fonttype": "none", "svg.hashsalt": "technical-archives",
                         "font.family": "sans-serif", "font.size": 9})
    settings, params, items = parse_spec(text)
    x0, x1 = (float(evaluate(settings.get(k, d), {})) for k, d in (("left", "-10"), ("right", "10")))
    y0, y1 = (float(evaluate(settings.get(k, d), {})) for k, d in (("bottom", "-7"), ("top", "7")))
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    xs, ys = np.linspace(x0, x1, 1601), np.linspace(y0, y1, 1601)
    auto = iter(PALETTE * 20)

    for item in items:
        expr, color = item["expr"], item["color"] or next(auto)
        kw = {"color": color, "linestyle": item["style"], "linewidth": 1.6}
        used = names_in(expr) | set().union(*(names_in(l) for l in item["limits"]), set())
        for env in envs_for(used, params):
            point = re.fullmatch(r"\((.+)\)", expr)
            if point and "=" not in expr and len(split_top(point.group(1), ",")) == 2:
                px, py = (
                    [float(evaluate(v, env)) for v in split_top(c.strip()[1:-1], ",")]
                    if c.strip().startswith("[") else float(evaluate(c, env))
                    for c in split_top(point.group(1), ",")
                )
                px, py = np.broadcast_arrays(np.atleast_1d(px), np.atleast_1d(py))
                ax.plot(px, py, "o", ms=5.5, color=color, mfc="white" if item["open"] else color,
                        mew=1.4, zorder=5, clip_on=False)
            elif m := re.fullmatch(r"y\s*(<=|>=)\s*(.+)", expr):
                yv = evaluate(m.group(2), {**env, "x": xs}) + 0 * xs
                edge = y1 if m.group(1) == ">=" else y0
                ax.fill_between(xs, yv, edge, color=color, alpha=0.18, linewidth=0)
                ax.plot(xs, yv, **kw)
            elif re.match(r"y\s*=", expr) and "y" not in compile_expr(expr.split("=", 1)[1])[1]:
                yv = np.asarray(evaluate(expr.split("=", 1)[1], {**env, "x": xs}), dtype=float) + 0 * xs
                yv = np.where(limit_mask(item["limits"], env, xs, yv), yv, np.nan)
                yv[~np.isfinite(yv)] = np.nan
                jump = np.abs(np.diff(yv, prepend=yv[0])) > 0.6 * (y1 - y0)  # break at asymptotes
                ax.plot(xs, np.where(jump, np.nan, yv), **kw)
            elif re.match(r"x\s*=", expr) and "x" not in compile_expr(expr.split("=", 1)[1])[1]:
                xv = np.asarray(evaluate(expr.split("=", 1)[1], {**env, "y": ys}), dtype=float) + 0 * ys
                xv = np.where(limit_mask(item["limits"], env, xv, ys), xv, np.nan)
                xv[~np.isfinite(xv)] = np.nan
                ax.plot(xv, ys, **kw)
            elif "=" in expr:
                lhs, rhs = expr.split("=", 1)
                X, Y = np.meshgrid(np.linspace(x0, x1, 700), np.linspace(y0, y1, 700))
                full = {**env, "x": X, "y": Y}
                Z = np.asarray(evaluate(lhs, full) - evaluate(rhs, full), dtype=float) + 0 * X
                Z = np.where(limit_mask(item["limits"], env, X, Y), Z, np.nan)
                Z[np.abs(Z) > 1e6] = np.nan
                ax.contour(X, Y, Z, levels=[0], colors=[color], linestyles=[item["style"]], linewidths=1.6)
            else:
                raise ValueError(f"cannot draw {item['raw']!r}")

    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.grid(True, color="#e6e6e6", linewidth=0.7)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side, lo, hi in (("left", x0, x1), ("bottom", y0, y1)):
        ax.spines[side].set_color("#555555")
        if lo <= 0 <= hi:
            ax.spines[side].set_position("zero")
    ax.tick_params(colors="#555555", labelsize=8, length=3)
    if "xAxisLabel" in settings:
        ax.set_xlabel(settings["xAxisLabel"], loc="right", color="#333333")
    if "yAxisLabel" in settings:
        ax.set_ylabel(settings["yAxisLabel"], loc="top", rotation=0, color="#333333")
    fig.tight_layout(pad=0.6)
    if out is not None:
        fig.savefig(out, format="svg", metadata={"Date": None}, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- commands

def specs():
    for p in sorted(ROOT.rglob("*.desmos")):
        if not SKIP & set(p.relative_to(ROOT).parts):
            yield p


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def assets_dir(note: Path) -> Path:
    """The Assets folder of the note's section: the folder that holds Index.md."""
    for parent in note.parents:
        if (parent / "Index.md").exists():
            for name in ("Assets", "assets"):
                if (parent / name).is_dir():
                    return parent / name
            return parent / "Assets"
    return note.parent / "Assets"


def convert(note: Path) -> int:
    text = note.read_text(encoding="utf-8")
    assets = assets_dir(note)
    count = 0

    def swap(m):
        nonlocal count
        count += 1
        name = f"{slug(note.stem)}-{count}"
        assets.mkdir(exist_ok=True)
        draw(m.group(1), assets / f"{name}.svg")  # raises before anything is written
        (assets / f"{name}.desmos").write_text(m.group(1), encoding="utf-8")
        rel = Path(*[".."] * (len(note.relative_to(assets.parent).parts) - 1), assets.name, f"{name}.svg")
        return f"![{note.stem}, figure {count}]({rel.as_posix().replace(' ', '%20')})\n"

    new = BLOCK.sub(swap, text)
    if count:
        note.write_text(new, encoding="utf-8")
    return count


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--all", action="store_true", help="redraw every spec")
    ap.add_argument("--check", action="store_true", help="try every spec and every desmos-graph block; write nothing")
    ap.add_argument("--convert", nargs="+", metavar="NOTE", help="convert the desmos-graph blocks in these notes")
    args = ap.parse_args()

    if args.convert:
        for n in args.convert:
            print(f"{convert(Path(n).resolve())} figure(s)  {n}")
        return 0
    if args.check:
        bad = 0
        sources = [(p, p.read_text(encoding="utf-8")) for p in specs()]
        for md in sorted(ROOT.rglob("*.md")):
            if not SKIP & set(md.relative_to(ROOT).parts):
                sources += [(md, m.group(1)) for m in BLOCK.finditer(md.read_text(encoding="utf-8"))]
        for p, text in sources:
            try:
                draw(text, None)
            except Exception as e:  # noqa: BLE001 - report every failure
                bad += 1
                print(f"FAIL {p.relative_to(ROOT)}: {e}")
        print(f"{len(sources) - bad}/{len(sources)} graphs draw cleanly")
        return 1 if bad else 0
    done = 0
    for spec in specs():
        svg = spec.with_suffix(".svg")
        if args.all or not svg.exists() or svg.stat().st_mtime < spec.stat().st_mtime:
            draw(spec.read_text(encoding="utf-8"), svg)
            done += 1
    print(f"drew {done} figure(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
