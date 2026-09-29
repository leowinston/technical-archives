"""Separate-chaining hash table with at least three collisions and one chain of length three."""

from __future__ import annotations

import random
from typing import Dict, List

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import blank_cell, build_document_body, format_sequence, make_centered, make_table
from problemgen.problem import Problem

TOPIC = "hashing"
ALIASES = ("hash",)

TABLE_SIZES = [5, 7, 11]


def generate(rng: random.Random) -> Problem:
    for _ in range(200):
        m = rng.choice(TABLE_SIZES)
        keys = sample_unique_ints(rng, rng.randint(8, 10), 10, 99)
        buckets: Dict[int, List[int]] = {i: [] for i in range(m)}
        for key in keys:
            buckets[key % m].append(key)
        collisions = sum(max(0, len(chain) - 1) for chain in buckets.values())
        if collisions >= 3 and max(len(chain) for chain in buckets.values()) >= 3:
            rows = [["Bucket", "Chain"]]
            for bucket in range(m):
                rows.append([str(bucket), blank_cell()])
            solution_rows = [["Bucket", "Chain"]]
            for bucket in range(m):
                if buckets[bucket]:
                    chain = "$" + " \\rightarrow ".join(str(v) for v in buckets[bucket]) + "$"
                else:
                    chain = "$\\varnothing$"
                solution_rows.append([str(bucket), chain])
            prompt = (
                f"Build a hash table with {m} buckets using the hash function $h(k)=k \\bmod {m}$ and separate chaining. "
                f"Insert the keys in the order {format_sequence(keys)}."
            )
            solution = make_centered(make_table(solution_rows, align="|c|l|"))
            return Problem(
                section_title="Conversions and Hashing",
                subsection_title="Separate Chaining Hash Table",
                body=build_document_body(prompt, extras=make_centered(make_table(rows, align="|c|l|"))),
                notes=[
                    "topic=hashing",
                    f"table_size={m}",
                    f"collisions={collisions}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial hashing instance.")
