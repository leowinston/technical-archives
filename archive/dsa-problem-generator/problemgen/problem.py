"""The Problem record every generator returns, and its LaTeX document form."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from problemgen.latex import LATEX_PREAMBLE, latex_escape


@dataclass
class Problem:
    section_title: str
    subsection_title: str
    body: str
    notes: List[str] = field(default_factory=list)
    solution: str = ""

    def to_latex(self, seed: int, with_solution: bool = False) -> str:
        comment_block = "\n".join(f"% {note}" for note in ([f"seed={seed}"] + self.notes))
        solution_block = ""
        if with_solution and self.solution.strip():
            solution_block = (
                "\n\\subsection*{Instructor Reference}\n"
                + self.solution.strip()
                + "\n"
            )
        return (
            LATEX_PREAMBLE.strip()
            + "\n\\begin{document}\n\n"
            + "\\begin{center}\n"
            + "    \\Large\\textbf{CS 253: Data Structures and Algorithms}\\\\\n"
            + "    \\large\\textbf{Randomized Final Study Problem}\n"
            + "\\end{center}\n"
            + "\\vspace{1em}\n\n"
            + comment_block
            + "\n\n"
            + f"\\section*{{{latex_escape(self.section_title)}}}\n"
            + f"\\subsection*{{{latex_escape(self.subsection_title)}}}\n"
            + self.body.strip()
            + "\n"
            + solution_block
            + "\n\\end{document}\n"
        )
