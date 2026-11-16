"""Keep every consumer of preamble.sty in step with it.

preamble.sty is the only place a custom LaTeX macro is defined. Three things read it:

  Obsidian        the Extended MathJax plugin loads preamble.sty at startup
  Latex Suite     needs each macro name in its ALL_MACROS list, or it splits
                  the macro while you type (\\SD -> \\S D)
  the MkDocs site .github/site/prepare.py turns the macros into MathJax config

Run this after editing preamble.sty:

    python tools/macros.py          # rewrite the Latex Suite list, list the macros
    python tools/macros.py --check  # exit 1 if the Latex Suite list is out of date

The site needs no manual step: it reads preamble.sty on every build.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREAMBLE = ROOT / "preamble.sty"
LATEX_SUITE = ROOT / ".obsidian" / "plugins" / "obsidian-latex-suite" / "data.json"
DEFINITION = re.compile(r"\\(?:re)?newcommand\s*\{\\([A-Za-z]+)\}\s*(?:\[(\d)\])?\s*")
PUSH = re.compile(r"(ALL_MACROS\.push\(\s*)(.*?)(\s*\);)", re.S)


def braced(s: str, i: int) -> str:
    """Content of the {...} group that starts at s[i]."""
    depth = 0
    for j in range(i, len(s)):
        depth += s[j] == "{"
        depth -= s[j] == "}"
        if depth == 0:
            return s[i + 1 : j]
    raise ValueError("unbalanced braces in preamble.sty")


def preamble_macros() -> dict:
    """{name: body} or {name: [body, n_args]}, the shape MathJax's `macros` option takes."""
    text = "\n".join(re.split(r"(?<!\\)%", line)[0] for line in PREAMBLE.read_text(encoding="utf-8").splitlines())
    macros = {}
    for m in DEFINITION.finditer(text):
        body = braced(text, m.end())
        macros[m.group(1)] = [body, int(m.group(2))] if m.group(2) else body
    return macros


def sync_latex_suite(names: list[str], write: bool) -> bool:
    """Return True if the Latex Suite list already matched."""
    data = json.loads(LATEX_SUITE.read_text(encoding="utf-8"))
    wanted = ", ".join(f'"\\\\{n}"' for n in names)
    m = PUSH.search(data["snippets"])
    if not m:
        raise SystemExit("ALL_MACROS.push(...) not found in the Latex Suite snippets")
    if m.group(2).strip() == wanted:
        return True
    if write:
        data["snippets"] = data["snippets"][: m.start(2)] + wanted + data["snippets"][m.end(2) :]
        LATEX_SUITE.write_text(json.dumps(data, indent=2), encoding="utf-8")  # the plugin's own format
    return False


def main() -> int:
    names = list(preamble_macros())
    check = "--check" in sys.argv
    in_sync = sync_latex_suite(names, write=not check)
    print(f"{len(names)} macros in preamble.sty: " + " ".join("\\" + n for n in names))
    if in_sync:
        print("Latex Suite list: already in sync")
        return 0
    if check:
        print("Latex Suite list: OUT OF DATE, run `python tools/macros.py`")
        return 1
    print("Latex Suite list: updated. Quit Obsidian (Cmd+Q) and reopen it to load the change.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
