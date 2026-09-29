"""Longest common subsequence DP where the answer is neither tiny nor a whole string."""

from __future__ import annotations

import random
from typing import List

from problemgen.latex import blank_cell, build_document_body, make_centered, make_table, wrap_paragraph
from problemgen.problem import Problem

TOPIC = "lcs"
ALIASES = ()


def lcs_table(a: str, b: str) -> List[List[int]]:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def generate(rng: random.Random) -> Problem:
    alphabet = "ABCDE"
    for _ in range(400):
        a = "".join(rng.choice(alphabet) for _ in range(rng.randint(6, 7)))
        b = "".join(rng.choice(alphabet) for _ in range(rng.randint(6, 7)))
        dp = lcs_table(a, b)
        lcs_len = dp[-1][-1]
        if 3 <= lcs_len < min(len(a), len(b)):
            rows = [["", "$\\varepsilon$"] + list(b)]
            rows.append(["$\\varepsilon$", "0"] + ["0"] * len(b))
            for ch in a:
                rows.append([ch, "0"] + [blank_cell() for _ in b])
            solution_rows = [["", "$\\varepsilon$"] + list(b)]
            solution_rows.append(["$\\varepsilon$"] + [str(v) for v in dp[0]])
            for i, ch in enumerate(a, 1):
                solution_rows.append([ch] + [str(v) for v in dp[i]])
            prompt = (
                f'Compute the longest common subsequence of the strings \\texttt{{{a}}} and \\texttt{{{b}}}. '
                "The 0th row and 0th column are filled in for you; complete the rest of the table."
            )
            solution = (
                wrap_paragraph(f"LCS length: {lcs_len}.")
                + make_centered(make_table(solution_rows))
            )
            return Problem(
                section_title="Dynamic Programming",
                subsection_title="Longest Common Subsequence",
                body=build_document_body(prompt, extras=make_centered(make_table(rows))),
                notes=[
                    "topic=lcs",
                    f"lcs_length={lcs_len}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial LCS instance.")
