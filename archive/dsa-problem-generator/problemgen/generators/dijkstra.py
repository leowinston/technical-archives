"""Dijkstra tracing on a fixed layout with random weights that force distance improvements."""

from __future__ import annotations

import heapq
import math
import random
from typing import Dict, List, Optional, Sequence, Tuple

from problemgen.generators.common import generate_template_weights
from problemgen.latex import build_document_body, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_graph

TOPIC = "dijkstra"
ALIASES = ()

POSITIONS: Dict[int, Tuple[float, float]] = {
    0: (0.0, 0.0),
    1: (2.5, 2.5),
    3: (2.5, -2.5),
    2: (4.5, 0.0),
    4: (6.5, 3.0),
    5: (8.0, 0.0),
    6: (9.0, -3.0),
    7: (10.5, 2.0),
}

# (u, v, TikZ edge style) for each directed edge.
TEMPLATE_EDGES: List[Tuple[int, int, str]] = [
    (0, 1, ""),
    (0, 2, ""),
    (0, 3, ""),
    (1, 4, "bend left=15"),
    (1, 2, ""),
    (2, 5, ""),
    (3, 5, ""),
    (4, 1, "bend left=15"),
    (4, 5, ""),
    (4, 7, ""),
    (5, 6, "bend right=15"),
    (5, 7, ""),
    (6, 5, "bend right=15"),
    (6, 3, ""),
    (6, 7, ""),
]


def dijkstra_stats(n: int, edges: Sequence[Tuple[int, int, int]]) -> Tuple[List[float], int, List[Optional[int]]]:
    """Return (distances from 0, count of improved finite estimates, predecessors)."""
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [math.inf] * n
    parent: List[Optional[int]] = [None] * n
    dist[0] = 0
    pq: List[Tuple[float, int]] = [(0, 0)]
    improvements = 0
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                if dist[v] < math.inf:
                    improvements += 1
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, improvements, parent


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        weights = generate_template_weights(rng, len(TEMPLATE_EDGES), 1, 9, require_duplicate=True)
        edges = [(u, v, w) for (u, v, _), w in zip(TEMPLATE_EDGES, weights)]
        dist, improvements, parent = dijkstra_stats(len(POSITIONS), edges)
        if all(d < math.inf for d in dist) and improvements >= 2 and len(set(int(d) for d in dist)) >= 5:
            render_edges = [(u, v, w, style) for (u, v, style), w in zip(TEMPLATE_EDGES, weights)]
            figure = render_graph(POSITIONS, render_edges, directed=True, weighted=True, title="Directed weighted graph for Dijkstra's algorithm.")
            prompt = (
                "Starting from vertex 0, apply Dijkstra's algorithm to the graph below. "
                "Record the distance estimates, predecessor updates, and the order in which vertices are settled."
            )
            tree_edges = [(p, i) for i, p in enumerate(parent) if p is not None]
            solution = wrap_paragraph(
                "Final distances: "
                + ", ".join(f"{i}:{int(d)}" for i, d in enumerate(dist))
                + ". Shortest-path tree edges: "
                + ", ".join(f"({u},{v})" for u, v in tree_edges)
                + "."
            )
            return Problem(
                section_title="Graphs",
                subsection_title="Dijkstra's Algorithm",
                body=build_document_body(prompt, figure=figure),
                notes=[
                    "topic=dijkstra",
                    f"vertices={len(POSITIONS)}",
                    f"edges={len(TEMPLATE_EDGES)}",
                    f"improvement_count={improvements}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial Dijkstra instance.")
