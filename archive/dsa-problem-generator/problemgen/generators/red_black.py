"""Red-black insert/delete tracing that forces rotations and recolorings."""

from __future__ import annotations

import random

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import build_document_body, format_sequence, make_centered, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_rb_tree
from problemgen.structures import RBTree

TOPIC = "red_black"
ALIASES = ("rb", "red-black")


def generate(rng: random.Random) -> Problem:
    for _ in range(600):
        inserts = sample_unique_ints(rng, rng.randint(10, 12), 5, 95)
        deletions = rng.sample(inserts, rng.randint(2, 3))
        tree = RBTree()
        for value in inserts:
            tree.insert(value)
        insert_rotations = tree.rotation_count
        insert_recolors = tree.recolor_count
        for value in deletions:
            tree.delete(value)
        delete_rotations = tree.rotation_count - insert_rotations
        delete_recolors = tree.recolor_count - insert_recolors
        if (
            tree.root is not tree.nil
            and insert_rotations >= 1
            and insert_recolors >= 3
            and delete_rotations + delete_recolors >= 1
        ):
            final_tree = render_rb_tree(tree.root, tree.nil)
            prompt = (
                "Start from an empty red-black tree. Insert the keys in "
                f"{format_sequence(inserts)}. Then remove the keys in "
                f"{format_sequence(deletions)}, showing every recoloring and "
                "rotation needed to restore the red-black invariants."
            )
            solution = (
                wrap_paragraph(
                    f"Final red-black tree after all updates. Insert rotations: {insert_rotations}, "
                    f"insert recolors: {insert_recolors}, delete rotations: {delete_rotations}, "
                    f"delete recolors: {delete_recolors}."
                )
                + make_centered(final_tree)
            )
            return Problem(
                section_title="Sequence-Based Structures",
                subsection_title="Red-Black Tree Tracing Challenge",
                body=build_document_body(prompt),
                notes=[
                    "topic=red_black",
                    f"insert_rotations={insert_rotations}",
                    f"insert_recolors={insert_recolors}",
                    f"delete_rotations={delete_rotations}",
                    f"delete_recolors={delete_recolors}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial red-black instance.")
