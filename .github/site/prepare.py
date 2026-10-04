"""Stage the vault for MkDocs.

Copies the notes into _docs/, renames each Index.md to index.md so it becomes
its folder's landing page, and turns preamble.sty into a MathJax macro config
so the site renders the same macros as Obsidian.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_docs"
SKIP = {".git", ".github", ".obsidian", ".trash", "_docs", "_site", ".venv", "venv", "__pycache__"}

INDEX_LINK = re.compile(r"(\]\((?:[^)\s]*/)?)Index\.md")
QUOTE = re.compile(r"^((?:\s*>)*\s*)(.*)$")
FENCE = re.compile(r"^\s*(```|~~~)")


def pad_display_math(text):
    """Put blank lines around $$ blocks.

    Obsidian renders $$ blocks that touch the surrounding text, but MkDocs only
    sees display math when it is its own paragraph. Keeps any > callout prefix.
    """
    out, in_math, in_fence = [], False, False
    lines = text.split("\n")
    for i, line in enumerate(lines):
        prefix, body = QUOTE.match(line).groups()
        if FENCE.match(body):
            in_fence = not in_fence
        stripped = body.strip()
        if in_fence or not stripped.startswith("$$") and not (in_math and stripped.endswith("$$")):
            out.append(line)
            continue
        opens = not in_math and stripped.startswith("$$")
        one_line = opens and len(stripped) > 4 and stripped.endswith("$$")
        blank = prefix.rstrip()
        if opens and out and QUOTE.match(out[-1]).group(2).strip():
            out.append(blank)
        out.append(line)
        if opens and not one_line:
            in_math = True
            continue
        in_math = False
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if QUOTE.match(nxt).group(2).strip():
            out.append(blank)
    return "\n".join(out)


def copy_vault():
    if OUT.exists():
        shutil.rmtree(OUT)
    for src in ROOT.rglob("*"):
        rel = src.relative_to(ROOT)
        if any(part in SKIP or part.startswith(".") for part in rel.parts) or src.is_dir():
            continue
        name = "index.md" if src.name == "Index.md" else src.name
        dest = OUT / rel.parent / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".md":
            text = INDEX_LINK.sub(r"\1index.md", src.read_text(encoding="utf-8"))
            dest.write_text(pad_display_math(text), encoding="utf-8")
        else:
            shutil.copy2(src, dest)


def braced(s, i):
    """Return (content, end) for the {...} group starting at s[i]."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1 : j], j + 1
    raise ValueError("unbalanced braces in preamble.sty")


def preamble_macros():
    text = "\n".join(line.split("%")[0] for line in (ROOT / "preamble.sty").read_text().splitlines())
    macros = {}
    for m in re.finditer(r"\\(?:re)?newcommand\s*\{\\([A-Za-z]+)\}\s*(?:\[(\d)\])?\s*", text):
        body, _ = braced(text, m.end())
        macros[m.group(1)] = [body, int(m.group(2))] if m.group(2) else body
    return macros


def write_mathjax(macros):
    import json

    js = OUT / "javascripts" / "mathjax.js"
    js.parent.mkdir(parents=True, exist_ok=True)
    js.write_text(
        "window.MathJax = {\n"
        "  tex: {\n"
        '    inlineMath: [["\\\\(", "\\\\)"]],\n'
        '    displayMath: [["\\\\[", "\\\\]"]],\n'
        "    processEscapes: true,\n"
        "    processEnvironments: true,\n"
        f"    macros: {json.dumps(macros, indent=2)}\n"
        "  },\n"
        '  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex|md-nav__link|md-ellipsis" }\n'
        "};\n"
        "document$.subscribe(() => {\n"
        "  MathJax.startup.output.clearCache();\n"
        "  MathJax.typesetClear();\n"
        "  MathJax.texReset();\n"
        "  MathJax.typesetPromise();\n"
        "});\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    copy_vault()
    macros = preamble_macros()
    write_mathjax(macros)
    print(f"staged {OUT.relative_to(ROOT)}/ with {len(macros)} preamble macros")
