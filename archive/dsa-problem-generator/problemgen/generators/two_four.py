"""(2,4) tree tracing with at least one split and one merge or borrow."""

from __future__ import annotations

import random

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import build_document_body, format_sequence, make_centered, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_layout_tree, two_four_to_layout
from problemgen.structures import TwoFourTree

TOPIC = "two_four"
ALIASES = ("24", "2-4", "2,4", "two-four")


def generate(rng: random.Random) -> Problem:
    for _ in range(600):
        inserts = sample_unique_ints(rng, rng.randint(10, 12), 5, 95)
        deletions = rng.sample(inserts, rng.randint(2, 3))
        tree = TwoFourTree()
        for value in inserts:
            tree.insert(value)
        insert_splits = tree.split_count
        for value in deletions:
            tree.delete(value)
        delete_events = tree.merge_count + tree.borrow_count
        if insert_splits >= 1 and delete_events >= 1 and tree.root.keys:
            final_tree = render_layout_tree(two_four_to_layout(tree.root), x_scale=2.2, y_scale=1.8)
            prompt = (
                "Start from an empty (2,4) tree. Insert the keys in "
                f"{format_sequence(inserts)}. Then remove the keys in "
                f"{format_sequence(deletions)}, showing each split, borrow, or merge."
            )
            solution = (
                wrap_paragraph(
                    f"Final (2,4) tree after all updates. Splits: {insert_splits}. "
                    f"Delete merges/borrows: {delete_events}."
                )
                + make_centered(final_tree)
            )
            return Problem(
                section_title="Sequence-Based Structures",
                subsection_title="(2,4) Tree Tracing Challenge",
                body=build_document_body(prompt),
                notes=[
                    "topic=two_four",
                    f"splits={insert_splits}",
                    f"merge_count={tree.merge_count}",
                    f"borrow_count={tree.borrow_count}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial (2,4) tree instance.")
