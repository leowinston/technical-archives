"""Stage the vault for MkDocs.

Publishes exactly the notes git tracks, so a local preview matches the live
site and notes still waiting in the review queue never leak out.

For each published note it:
  - renames Index.md to index.md so it becomes its folder's landing page
  - puts blank lines around $$ blocks, which MkDocs needs and Obsidian doesn't
  - unlinks anything that points at a note or file that isn't published
    (a list item that was only such a link is dropped, and so is a heading
    left with nothing under it)
and it turns preamble.sty into the MathJax macro config, so the site renders
the same macros as Obsidian.

    python .github/site/prepare.py            # tracked files only
    python .github/site/prepare.py --all      # everything on disk (local preview)
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
SITE = Path(__file__).resolve().parent
OUT = ROOT / "_docs"
sys.path.insert(0, str(ROOT / "tools"))
from macros import preamble_macros  # noqa: E402

SKIP_DIRS = {".git", ".github", ".obsidian", ".trash", ".workspace", ".claude", ".agents", ".codex",
             ".claudian", "_docs", "_site", ".venv", "venv", "__pycache__", "tools", "node_modules"}
SKIP_NAMES = {"AGENTS.md", "requirements.txt", "preamble.sty", ".gitignore", ".DS_Store"}
SKIP_SUFFIXES = {".desmos"}
MATHJAX_VERSION = "3.2.2"

INDEX_LINK = re.compile(r"(\]\((?:[^)\s]*/)?)Index\.md")
QUOTE = re.compile(r"^((?:\s*>)*\s*)(.*)$")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")
ONLY_LINK_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+XDEADX(?:\s*[—–-].*)?$")
HEADING = re.compile(r"^(#{1,6})\s")


def published_files(everything: bool):
    if not everything:
        try:
            out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
            files = [ROOT / p for p in out.decode("utf-8").split("\0") if p]
        except (OSError, subprocess.CalledProcessError):
            everything = True
    if everything:
        files = [p for p in ROOT.rglob("*") if p.is_file()]
    for src in files:
        rel = src.relative_to(ROOT)
        if SKIP_DIRS & set(rel.parts) or rel.name in SKIP_NAMES or rel.suffix in SKIP_SUFFIXES:
            continue
        if src.is_file():
            yield rel


def pad_display_math(text):
    """Put blank lines around $$ blocks, keeping any > callout prefix."""
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


def drop_dead_links(text, rel, published):
    """Unlink targets that aren't published. Returns (text, number_removed)."""
    removed = 0

    def fix(m):
        nonlocal removed
        bang, label, target = m.groups()
        path = unquote(target.split("#")[0])
        if not path or re.match(r"[a-z][a-z0-9+.-]*:", target, re.I):
            return m.group(0)
        parts = []
        for part in (rel.parent / path).parts:
            if part == "..":
                if not parts:
                    return m.group(0)  # points outside the vault; leave it
                parts.pop()
            elif part != ".":
                parts.append(part)
        if "/".join(parts) in published:
            return m.group(0)
        removed += 1
        return "XDEADX" if bang else f"XDEADX{label}XENDX"

    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE.match(QUOTE.match(line).group(2)):
            in_fence = not in_fence
        if in_fence:
            out.append(line)
            continue
        new = LINK.sub(fix, line)
        if new != line:
            # a bullet that was nothing but a dead link (or a dead image) says nothing now
            bare = re.sub(r"XDEADX.*?XENDX", "XDEADX", new)
            if ONLY_LINK_ITEM.match(bare) or bare.strip() == "XDEADX":
                continue
            new = new.replace("XDEADX", "").replace("XENDX", "")
        out.append(new)

    # drop headings whose section is now empty
    lines, keep = out, [True] * len(out)
    for i, line in enumerate(lines):
        h = HEADING.match(line)
        if not h or not removed:
            continue
        level, empty = len(h.group(1)), True
        for nxt in lines[i + 1 :]:
            h2 = HEADING.match(nxt)
            if h2 and len(h2.group(1)) <= level:
                break
            if nxt.strip() and not h2 and nxt.strip() != "---":
                empty = False
                break
        keep[i] = not empty
    return "\n".join(l for l, k in zip(lines, keep) if k), removed


def copy_vault(everything=False):
    if OUT.exists():
        shutil.rmtree(OUT)
    files = list(published_files(everything))
    published = {f.as_posix() for f in files}
    unlinked = 0
    for rel in files:
        name = "index.md" if rel.name == "Index.md" else rel.name
        dest = OUT / rel.parent / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if rel.suffix == ".md":
            text, n = drop_dead_links((ROOT / rel).read_text(encoding="utf-8"), rel, published)
            unlinked += n
            text = INDEX_LINK.sub(r"\1index.md", text)
            dest.write_text(pad_display_math(text), encoding="utf-8")
        else:
            shutil.copy2(ROOT / rel, dest)
    return len(files), unlinked


def write_mathjax(macros):
    """MathJax config plus the library itself.

    The library is served from the site when `npm ci` has run in .github/site
    (CI always does), so math doesn't depend on a CDN being reachable. Without
    it, the page falls back to the same pinned version on jsDelivr.
    """
    js_dir = OUT / "javascripts"
    js_dir.mkdir(parents=True, exist_ok=True)
    vendored = SITE / "node_modules" / "mathjax-full" / "es5"
    if vendored.is_dir():
        # only what the page loads: the bundle, the autoloaded TeX extensions, and the web fonts
        for part in ("tex-mml-chtml.js", "input/tex/extensions", "output/chtml/fonts/woff-v2"):
            src, dest = vendored / part, js_dir / "mathjax" / part
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dest) if src.is_dir() else shutil.copy2(src, dest)
        loader = 'new URL("mathjax/tex-mml-chtml.js", document.currentScript.src).href'
    else:
        loader = f'"https://cdn.jsdelivr.net/npm/mathjax@{MATHJAX_VERSION}/es5/tex-mml-chtml.js"'
    (js_dir / "mathjax.js").write_text(
        "window.MathJax = {\n"
        "  tex: {\n"
        '    inlineMath: [["\\\\(", "\\\\)"]],\n'
        '    displayMath: [["\\\\[", "\\\\]"]],\n'
        "    processEscapes: true,\n"
        "    processEnvironments: true,\n"
        f"    macros: {json.dumps(macros, indent=2)}\n"
        "  },\n"
        '  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex|md-nav__link|md-ellipsis", enableMenu: false }\n'
        "};\n"
        "(function () {\n"
        '  var s = document.createElement("script");\n'
        f"  s.src = {loader};\n"
        "  s.async = true;\n"
        "  document.head.appendChild(s);\n"
        "})();\n",
        encoding="utf-8",
    )
    css_dir = OUT / "stylesheets"
    css_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SITE / "extra.css", css_dir / "extra.css")


if __name__ == "__main__":
    n, unlinked = copy_vault(everything="--all" in sys.argv)
    macros = preamble_macros()
    write_mathjax(macros)
    print(f"staged {n} files in {OUT.relative_to(ROOT)}/, {len(macros)} preamble macros, "
          f"{unlinked} links to unpublished notes removed")
