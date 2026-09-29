"""Kruskal's MST on a fixed layout, requiring at least two cycle-forming edges to be discarded."""

from __future__ import annotations

import random
from typing import Dict, List, Sequence, Tuple

from problemgen.generators.common import generate_template_weights
from problemgen.latex import build_document_body, format_sequence, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_graph
from problemgen.structures import UnionFind

TOPIC = "kruskal"
ALIASES = ()

POSITIONS: Dict[int, Tuple[float, float]] = {
    0: (0.0, 0.0),
    1: (2.4, 2.6),
    5: (2.4, -2.6),
    6: (4.8, 0.0),
    2: (7.1, 2.6),
    4: (7.1, -2.6),
    3: (9.8, 0.0),
    7: (9.8, 3.9),
}

TEMPLATE_EDGES: List[Tuple[int, int, str]] = [
    (0, 1, ""),
    (0, 6, ""),
    (0, 5, ""),
    (1, 2, ""),
    (1, 6, ""),
    (5, 6, ""),
    (5, 4, ""),
    (6, 2, ""),
    (6, 4, ""),
    (2, 7, ""),
    (2, 3, ""),
    (4, 3, ""),
    (3, 7, ""),
]


def kruskal_stats(n: int, edges: Sequence[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
    """Return (accepted MST edges in order, discarded edges)."""
    uf = UnionFind(n)
    mst: List[Tuple[int, int, int]] = []
    rejected = 0
    for u, v, w in sorted(edges, key=lambda item: item[2]):
        if uf.union(u, v):
            mst.append((u, v, w))
        else:
            rejected += 1
    return mst, rejected


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        weights = generate_template_weights(rng, len(TEMPLATE_EDGES), 1, 9, require_duplicate=True)
        edges = [(u, v, w) for (u, v, _), w in zip(TEMPLATE_EDGES, weights)]
        mst, rejected = kruskal_stats(len(POSITIONS), edges)
        if len(mst) == len(POSITIONS) - 1 and rejected >= 2:
            render_edges = [(u, v, w, style) for (u, v, style), w in zip(TEMPLATE_EDGES, weights)]
            figure = render_graph(POSITIONS, render_edges, directed=False, weighted=True, title="Undirected weighted graph for Kruskal's algorithm.")
            weight = sum(w for _, _, w in mst)
            prompt = (
                "Apply Kruskal's algorithm to the graph below. Consider the edges in nondecreasing order by weight, "
                "and indicate which edges are accepted or discarded."
            )
            solution = wrap_paragraph(
                "Accepted MST edges: "
                + format_sequence([f"({u},{v},{w})" for u, v, w in mst])
                + f". Total weight: {weight}."
            )
            return Problem(
                section_title="Graphs",
                subsection_title="Kruskal's Algorithm",
                body=build_document_body(prompt, figure=figure),
                notes=[
                    "topic=kruskal",
                    f"vertices={len(POSITIONS)}",
                    f"edges={len(TEMPLATE_EDGES)}",
                    f"rejected_edges={rejected}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial Kruskal instance.")
