"""Boyer-Moore tracing where at least one good-suffix jump beats the bad-character rule."""

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

TOPIC = "boyer_moore"
ALIASES = ("boyer", "boyer-moore")

PATTERNS = [
    "DAABB",
    "ABACABA",
    "ANAANA",
    "TATATA",
    "WXYWX",
    "CABACAB",
]


def good_suffix_shifts(pattern: str) -> List[int]:
    m = len(pattern)
    shift = [0] * (m + 1)
    bpos = [0] * (m + 1)
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]
    return shift


def search_stats(text: str, pattern: str) -> Tuple[int, List[int]]:
    """Return (good-suffix-driven jumps, match start indices)."""
    last = {ch: idx for idx, ch in enumerate(pattern)}
    shift = good_suffix_shifts(pattern)
    s = 0
    uses = 0
    matches: List[int] = []
    while s <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += shift[0] if shift[0] > 0 else 1
        else:
            bad_char = j - last.get(text[s + j], -1)
            good_suffix = shift[j + 1]
            if len(pattern) - 1 - j > 0 and good_suffix >= bad_char and good_suffix > 1:
                uses += 1
            s += max(1, bad_char, good_suffix)
    return uses, matches


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        pattern = rng.choice(PATTERNS)
        alphabet = sorted(set(pattern))
        prefix = "".join(rng.choice(alphabet) for _ in range(rng.randint(5, 8)))
        infix = "".join(rng.choice(alphabet) for _ in range(rng.randint(5, 7)))
        text = prefix + pattern[: len(pattern) - 1] + infix + pattern + rng.choice(alphabet) * 2
        uses, matches = search_stats(text, pattern)
        if uses >= 1 and matches:
            bad_char_row = [["Character"] + alphabet, ["Last Index"] + [blank_cell() for _ in alphabet]]
            last = {ch: idx for idx, ch in enumerate(pattern)}
            solution_row = [["Character"] + alphabet, ["Last Index"] + [str(last[ch]) for ch in alphabet]]
            prompt = (
                f"Apply the Boyer-Moore algorithm to find the pattern ``\\texttt{{{pattern}}}'' "
                'in the text string below. Show the preprocessing table and every shift used in the scan.'
            )
            solution = (
                make_centered(make_table(solution_row))
                + "\n"
                + wrap_paragraph(f"Match positions: {format_sequence(matches)}. Good-suffix-driven jumps observed: {uses}.")
            )
            return Problem(
                section_title="Linear Sorting and String Matching",
                subsection_title="Boyer-Moore",
                body=build_document_body(prompt, extras=make_text_display(text) + "\n" + make_centered(make_table(bad_char_row))),
                notes=[
                    "topic=boyer_moore",
                    f"good_suffix_jumps={uses}",
                    f"match_count={len(matches)}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial Boyer-Moore instance.")
