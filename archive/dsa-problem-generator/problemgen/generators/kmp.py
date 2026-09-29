"""Knuth-Morris-Pratt tracing where the search must fall back at least twice."""

from __future__ import annotations

import random
from typing import List, Tuple

from problemgen.latex import (
    blank_cell,
    build_document_body,
    format_sequence,
    make_centered,
    make_table,
    make_text_display,
    wrap_paragraph,
)
from problemgen.problem import Problem

TOPIC = "kmp"
ALIASES = ()

PATTERNS = [
    "ABACABA",
    "ABAAB",
    "CABACAB",
    "WXYWX",
    "TATATA",
    "ANAANA",
]


def failure_function(pattern: str) -> List[int]:
    failure = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            failure[i] = j
    return failure


def search_stats(text: str, pattern: str) -> Tuple[int, List[int]]:
    """Return (fallback count, match start indices)."""
    failure = failure_function(pattern)
    j = 0
    fallbacks = 0
    matches: List[int] = []
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = failure[j - 1]
            fallbacks += 1
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                matches.append(i - len(pattern) + 1)
                j = failure[j - 1]
    return fallbacks, matches


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        pattern = rng.choice(PATTERNS)
        alphabet = sorted(set(pattern))
        chunks = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(2, 5)))
            for _ in range(rng.randint(4, 6))
        ]
        text = "".join(chunks[:2]) + pattern + "".join(chunks[2:]) + pattern[: len(pattern) - 2]
        failure = failure_function(pattern)
        fallbacks, matches = search_stats(text, pattern)
        if max(failure) >= 2 and fallbacks >= 2 and matches:
            rows = [
                ["Index"] + [str(i) for i in range(len(pattern))],
                ["Pattern"] + list(pattern),
                ["f(i)"] + [blank_cell() for _ in pattern],
            ]
            solution_rows = [
                ["Index"] + [str(i) for i in range(len(pattern))],
                ["Pattern"] + list(pattern),
                ["f(i)"] + [str(v) for v in failure],
            ]
            prompt = (
                f"Apply the Knuth-Morris-Pratt algorithm to find the pattern ``\\texttt{{{pattern}}}'' "
                'in the text string below. First compute the failure function, then trace the search.'
            )
            solution = (
                make_centered(make_table(solution_rows))
                + "\n"
                + wrap_paragraph(f"Match positions: {format_sequence(matches)}. Fallback count during search: {fallbacks}.")
            )
            return Problem(
                section_title="Linear Sorting and String Matching",
                subsection_title="Knuth-Morris-Pratt (KMP)",
                body=build_document_body(prompt, extras=make_text_display(text) + "\n" + make_centered(make_table(rows))),
                notes=[
                    "topic=kmp",
                    f"max_failure={max(failure)}",
                    f"fallbacks={fallbacks}",
                    f"match_count={len(matches)}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial KMP instance.")
