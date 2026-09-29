"""Red-black to (2,4) conversion: absorb each red child into its black parent's node."""

from __future__ import annotations

import random
from typing import List, Optional

from problemgen.generators.common import sample_unique_ints
from problemgen.latex import build_document_body, make_centered
from problemgen.problem import Problem
from problemgen.render import render_layout_tree, render_rb_tree, two_four_to_layout
from problemgen.structures import BTreeNode, RBNode, RBTree

TOPIC = "rb_to_24"
ALIASES = ("conversion", "rb-to-24")


def rb_to_two_four(node: RBNode, nil: RBNode) -> Optional[BTreeNode]:
    if node is nil:
        return None
    assert node.color == "B"
    out = BTreeNode(node.left is nil and node.right is nil)
    keys: List[int] = []
    children: List[Optional[BTreeNode]] = []
    if node.left is not nil and node.left.color == "R":
        left = node.left
        keys.append(left.key)  # type: ignore[arg-type]
        children.append(rb_to_two_four(left.left, nil))
        children.append(rb_to_two_four(left.right, nil))
    else:
        children.append(rb_to_two_four(node.left, nil))
    keys.append(node.key)  # type: ignore[arg-type]
    if node.right is not nil and node.right.color == "R":
        right = node.right
        keys.append(right.key)  # type: ignore[arg-type]
        children.append(rb_to_two_four(right.left, nil))
        children.append(rb_to_two_four(right.right, nil))
    else:
        children.append(rb_to_two_four(node.right, nil))
    out.keys = keys
    cleaned_children = [child for child in children if child is not None]
    out.children = cleaned_children
    out.leaf = not cleaned_children
    return out


def count_red_nodes(node: RBNode, nil: RBNode) -> int:
    if node is nil:
        return 0
    return (1 if node.color == "R" else 0) + count_red_nodes(node.left, nil) + count_red_nodes(node.right, nil)


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        inserts = sample_unique_ints(rng, rng.randint(8, 10), 5, 95)
        tree = RBTree()
        for value in inserts:
            tree.insert(value)
        red_nodes = count_red_nodes(tree.root, tree.nil)
        if tree.root is tree.nil or red_nodes < 2:
            continue
        rb_figure = render_rb_tree(tree.root, tree.nil)
        converted = rb_to_two_four(tree.root, tree.nil)
        solution = make_centered(render_layout_tree(two_four_to_layout(converted), x_scale=2.2, y_scale=1.8))
        prompt = "Convert the following red-black tree into the equivalent (2,4) tree."
        return Problem(
            section_title="Conversions and Hashing",
            subsection_title="Red-Black to (2,4) Tree Conversion",
            body=build_document_body(prompt, figure=rb_figure),
            notes=[
                "topic=rb_to_24",
                f"red_nodes={red_nodes}",
                f"source_sequence={inserts}",
            ],
            solution=solution,
        )
    raise RuntimeError("Unable to generate a valid RB-to-(2,4) conversion instance.")
