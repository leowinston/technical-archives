"""LaTeX preamble and small formatting helpers shared by every generator."""

from __future__ import annotations

import textwrap
from typing import Optional, Sequence


LATEX_PREAMBLE = r"""
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{tikz-qtree}
\usetikzlibrary{arrows.meta, positioning, graphs, automata, matrix, calc}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}
\setlist{nosep}

\tikzset{
    every tree node/.style={circle, draw, minimum size=0.6cm, inner sep=1pt},
    blank/.style={draw=none, fill=none, edge from parent/.style={draw=none}},
    blacknode/.style={circle, draw, fill=black, text=white, minimum size=0.6cm, inner sep=1pt},
    whitenode/.style={circle, draw, fill=white, text=black, minimum size=0.6cm, inner sep=1pt},
    rednode/.style={circle, draw, fill=white, text=black, minimum size=0.6cm, inner sep=1pt},
    tfnode/.style={rectangle, draw, rounded corners=2pt, minimum size=0.45cm, inner sep=1pt},
    listnode/.style={rectangle, draw, rounded corners=2pt, minimum height=0.6cm, inner sep=3pt},
    skipnode/.style={rectangle, draw, minimum size=0.6cm, inner sep=2pt},
    main node/.style={circle, draw, minimum size=0.6cm}
}
"""


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def format_sequence(values: Sequence[object]) -> str:
    return r"\texttt{[" + ", ".join(str(v) for v in values) + "]}"


def format_word_list(words: Sequence[str]) -> str:
    return r"\texttt{" + ", ".join(words) + "}"


def blank_cell() -> str:
    return r"\phantom{0}"


def make_centered(content: str) -> str:
    return f"\\begin{{center}}\n{content}\n\\end{{center}}"


def make_text_display(text: str) -> str:
    """Center a long unbreakable string on its own line so it cannot run into the margin."""
    return make_centered(f"\\texttt{{{text}}}")


def make_table(rows: Sequence[Sequence[str]], align: Optional[str] = None) -> str:
    width = max(len(row) for row in rows)
    padded_rows = [list(row) + [blank_cell()] * (width - len(row)) for row in rows]
    spec = align if align is not None else "|" + "|".join("c" for _ in range(width)) + "|"
    lines = [f"\\begin{{tabular}}{{{spec}}}", "\\hline"]
    for row in padded_rows:
        lines.append(" " + " & ".join(row) + r" \\")
        lines.append("\\hline")
    lines.append("\\end{tabular}")
    return "\n".join(lines)


def wrap_paragraph(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def build_document_body(prompt: str, figure: str = "", extras: str = "") -> str:
    parts = [wrap_paragraph(prompt)]
    if figure.strip():
        parts.append(make_centered(figure.strip()))
    if extras.strip():
        parts.append(extras.strip())
    return "\n".join(parts)
