"""Prim's MST on a fixed layout, requiring stale frontier edges to be rejected."""

from __future__ import annotations

import heapq
import random
from typing import Dict, List, Sequence, Tuple

from problemgen.generators.common import generate_template_weights
from problemgen.latex import build_document_body, format_sequence, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_graph

TOPIC = "prim"
ALIASES = ()

POSITIONS: Dict[int, Tuple[float, float]] = {
    0: (0.0, 0.0),
    1: (2.6, 2.6),
    2: (2.6, -2.6),
    3: (5.2, 0.0),
    4: (7.8, 2.6),
    5: (7.8, -2.6),
    6: (10.4, 0.0),
}

TEMPLATE_EDGES: List[Tuple[int, int, str]] = [
    (0, 1, ""),
    (0, 3, ""),
    (0, 2, ""),
    (1, 3, ""),
    (1, 4, ""),
    (2, 3, ""),
    (2, 5, ""),
    (3, 4, ""),
    (3, 5, ""),
    (4, 5, ""),
    (4, 6, ""),
    (5, 6, ""),
]


def prim_stats(n: int, edges: Sequence[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], int]:
    """Lazy Prim from vertex 0. Return (MST edges in order, stale heap entries skipped)."""
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    visited = {0}
    pq: List[Tuple[int, int, int]] = []
    for v, w in graph[0]:
        heapq.heappush(pq, (w, 0, v))
    mst: List[Tuple[int, int, int]] = []
    rejected = 0
    while pq and len(visited) < n:
        w, u, v = heapq.heappop(pq)
        if v in visited:
            rejected += 1
            continue
        visited.add(v)
        mst.append((u, v, w))
        for nxt, nw in graph[v]:
            if nxt not in visited:
                heapq.heappush(pq, (nw, v, nxt))
    return mst, rejected


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        weights = generate_template_weights(rng, len(TEMPLATE_EDGES), 1, 9, require_duplicate=True)
        edges = [(u, v, w) for (u, v, _), w in zip(TEMPLATE_EDGES, weights)]
        mst, rejected = prim_stats(len(POSITIONS), edges)
        if len(mst) == len(POSITIONS) - 1 and rejected >= 2:
            render_edges = [(u, v, w, style) for (u, v, style), w in zip(TEMPLATE_EDGES, weights)]
            figure = render_graph(POSITIONS, render_edges, directed=False, weighted=True, title="Undirected weighted graph for Prim's algorithm.")
            weight = sum(w for _, _, w in mst)
            prompt = (
                "Starting from vertex 0, apply Prim's algorithm to the graph below. "
                "Show which edge is chosen at each iteration and maintain the current frontier."
            )
            solution = wrap_paragraph(
                "One MST edge order from Prim's algorithm: "
                + format_sequence([f"({u},{v},{w})" for u, v, w in mst])
                + f". Total weight: {weight}."
            )
            return Problem(
                section_title="Graphs",
                subsection_title="Prim's Algorithm",
                body=build_document_body(prompt, figure=figure),
                notes=[
                    "topic=prim",
                    f"vertices={len(POSITIONS)}",
                    f"edges={len(TEMPLATE_EDGES)}",
                    f"rejected_edges={rejected}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial Prim instance.")
