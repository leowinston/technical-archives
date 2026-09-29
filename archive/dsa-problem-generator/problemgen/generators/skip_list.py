"""Skip list tracing with prescribed tower heights, rejecting flat lists."""

from __future__ import annotations

import random

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import build_document_body, format_sequence, make_centered, make_table, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_skip_list
from problemgen.structures import SkipList

TOPIC = "skip_list"
ALIASES = ("skip", "skip-list")


def random_height(rng: random.Random, max_level: int = 5) -> int:
    height = 1
    while height < max_level and rng.random() < 0.5:
        height += 1
    return height


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        inserts = sample_unique_ints(rng, rng.randint(10, 12), 5, 95)
        deletions = rng.sample(inserts, rng.randint(2, 3))
        heights = {key: random_height(rng, 5) for key in inserts}
        promoted = sum(h - 1 for h in heights.values())
        tall_nodes = sum(1 for h in heights.values() if h >= 3)
        if promoted < 5 or tall_nodes < 2 or max(heights.values()) < 4:
            continue
        skip_list = SkipList(5)
        for key in inserts:
            skip_list.insert(key, heights[key])
        for key in deletions:
            skip_list.delete(key)
        rows = [["Key"] + [str(k) for k in inserts], ["Height"] + [str(heights[k]) for k in inserts]]
        prompt = (
            "Construct a skip list by inserting the keys in "
            f"{format_sequence(inserts)}. Use the prescribed tower heights in the table below "
            "to remove coin-flip ambiguity. After the structure is built, remove the keys in "
            f"{format_sequence(deletions)}, showing each pointer update."
        )
        solution = (
            wrap_paragraph(
                f"Promotions above the base level: {promoted}. Final skip list after the deletions:"
            )
            + make_centered(render_skip_list(skip_list))
        )
        return Problem(
            section_title="Sequence-Based Structures",
            subsection_title="Skip List Tracing Challenge",
            body=build_document_body(prompt, extras=make_centered(make_table(rows))),
            notes=[
                "topic=skip_list",
                f"promotions={promoted}",
                f"max_height={max(heights.values())}",
            ],
            solution=solution,
        )
    raise RuntimeError("Unable to generate a non-trivial skip list instance.")
