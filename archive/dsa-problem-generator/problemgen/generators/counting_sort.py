"""Counting sort over a small letter alphabet with repeated keys."""

from __future__ import annotations

import random
from typing import List

from problemgen.latex import (
    blank_cell,
    build_document_body,
    format_sequence,
    make_centered,
    make_table,
    wrap_paragraph,
)
from problemgen.problem import Problem

TOPIC = "counting_sort"
ALIASES = ("counting", "counting-sort")

ALPHABET = ["A", "B", "C", "D", "E"]


def start_indices(counts: List[int]) -> List[int]:
    starts: List[int] = []
    running = 0
    for count in counts:
        starts.append(running)
        running += count
    return starts


def generate(rng: random.Random) -> Problem:
    while True:
        values = [rng.choice(ALPHABET) for _ in range(rng.randint(11, 14))]
        if len(set(values)) >= 4 and max(values.count(ch) for ch in ALPHABET) >= 3:
            break
    counts = [values.count(ch) for ch in ALPHABET]
    starts = start_indices(counts)
    rows = [
        ["Letter"] + ALPHABET,
        ["Count"] + [blank_cell() for _ in ALPHABET],
        ["Start Index"] + [blank_cell() for _ in ALPHABET],
    ]
    solution_rows = [
        ["Letter"] + ALPHABET,
        ["Count"] + [str(c) for c in counts],
        ["Start Index"] + [str(s) for s in starts],
    ]
    prompt = (
        "Use counting sort to sort the letter array "
        f"{format_sequence(values)}. Show the frequency count array, the starting-index array, "
        "and the final stable output array."
    )
    solution = (
        make_centered(make_table(solution_rows))
        + "\n"
        + wrap_paragraph(f"Sorted output: {format_sequence(sorted(values))}.")
    )
    return Problem(
        section_title="Linear Sorting and String Matching",
        subsection_title="Counting Sort",
        body=build_document_body(prompt, extras=make_centered(make_table(rows))),
        notes=[
            "topic=counting_sort",
            f"distinct_letters={len(set(values))}",
            f"max_frequency={max(counts)}",
        ],
        solution=solution,
    )
