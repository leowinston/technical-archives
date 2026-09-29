"""AVL insert/delete tracing with at least two insert rotations and one delete rotation."""

from __future__ import annotations

import random

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import build_document_body, format_sequence, make_centered, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_avl_tree
from problemgen.structures import AVLTree

TOPIC = "avl"
ALIASES = ()


def generate(rng: random.Random) -> Problem:
    for _ in range(600):
        inserts = sample_unique_ints(rng, rng.randint(10, 12), 5, 95)
        deletions = rng.sample(inserts, rng.randint(2, 3))
        tree = AVLTree()
        for value in inserts:
            tree.insert(value)
        insert_rotations = tree.rotation_count
        for value in deletions:
            tree.delete(value)
        delete_rotations = tree.rotation_count - insert_rotations
        if insert_rotations >= 2 and delete_rotations >= 1 and tree.root is not None:
            solution_tree = render_avl_tree(tree.root)
            prompt = (
                "Start from an empty AVL tree. Insert the keys in "
                f"{format_sequence(inserts)}. Then remove the keys in "
                f"{format_sequence(deletions)}, showing each structural change "
                "and every balance-factor-driven rotation."
            )
            solution = (
                wrap_paragraph(
                    f"Final AVL tree after all updates. Insert rotations: {insert_rotations}. "
                    f"Delete rotations: {delete_rotations}."
                )
                + make_centered(solution_tree)
            )
            return Problem(
                section_title="Sequence-Based Structures",
                subsection_title="AVL Tree Tracing Challenge",
                body=build_document_body(prompt),
                notes=[
                    "topic=avl",
                    f"insert_rotations={insert_rotations}",
                    f"delete_rotations={delete_rotations}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial AVL instance.")
