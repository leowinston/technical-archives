"""LSD radix sort with four-digit keys and repeated low digits."""

from __future__ import annotations

import random
from typing import List, Sequence

from problemgen.latex import blank_cell, build_document_body, format_sequence, make_centered, make_table
from problemgen.problem import Problem

TOPIC = "radix_sort"
ALIASES = ("radix", "radix-sort")


def radix_passes(values: Sequence[int]) -> List[List[int]]:
    """Return the array after each stable bucket pass, least significant digit first."""
    arr = list(values)
    passes: List[List[int]] = []
    digits = len(str(max(arr)))
    for exp in range(digits):
        buckets: List[List[int]] = [[] for _ in range(10)]
        for value in arr:
            digit = (value // (10 ** exp)) % 10
            buckets[digit].append(value)
        arr = [value for bucket in buckets for value in bucket]
        passes.append(list(arr))
    return passes


def generate(rng: random.Random) -> Problem:
    while True:
        values = [rng.randint(10, 9999) for _ in range(rng.randint(9, 10))]
        max_digits = len(str(max(values)))
        if max_digits >= 4 and len({v % 10 for v in values}) <= len(values) - 2:
            break
    passes = radix_passes(values)
    rows = [["Pass 0"] + [str(v) for v in values]]
    for idx in range(1, len(passes) + 1):
        rows.append([f"Pass {idx}"] + [blank_cell() for _ in values])
    solution_rows = [["Pass 0"] + [str(v) for v in values]]
    for idx, arr in enumerate(passes, 1):
        solution_rows.append([f"Pass {idx}"] + [str(v) for v in arr])
    prompt = (
        "Use least significant digit (LSD) radix sort on the array "
        f"{format_sequence(values)}. Label each digit pass and preserve stability."
    )
    solution = make_centered(make_table(solution_rows))
    return Problem(
        section_title="Linear Sorting and String Matching",
        subsection_title="LSD Radix Sort",
        body=build_document_body(prompt, extras=make_centered(make_table(rows))),
        notes=[
            "topic=radix_sort",
            f"passes={len(passes)}",
            f"max_digits={len(str(max(values)))}",
        ],
        solution=solution,
    )
