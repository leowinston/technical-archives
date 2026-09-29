"""Topological sort of a fixed DAG with at least one step that has several choices."""

from __future__ import annotations

import heapq
import random
from typing import Dict, List, Sequence, Tuple

from problemgen.latex import build_document_body, format_sequence, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_graph

TOPIC = "topological_sort"
ALIASES = ("topo", "topological", "topological-sort")

POSITIONS: Dict[int, Tuple[float, float]] = {
    0: (0.0, 0.0),
    1: (2.5, 2.5),
    3: (2.5, -2.5),
    5: (5.0, 2.5),
    4: (5.0, -2.5),
    2: (7.5, 0.0),
    6: (10.0, 2.5),
    7: (10.0, -2.5),
}

TEMPLATE_EDGES: List[Tuple[int, int, str]] = [
    (0, 1, ""),
    (0, 3, ""),
    (1, 5, ""),
    (3, 4, ""),
    (5, 2, ""),
    (5, 6, ""),
    (4, 7, ""),
    (2, 6, ""),
    (2, 7, ""),
]


def topo_stats(n: int, edges: Sequence[Tuple[int, int, None]]) -> Tuple[List[int], int]:
    """Kahn's algorithm, smallest vertex first. Return (order, steps with several choices)."""
    indeg = [0] * n
    graph: Dict[int, List[int]] = {i: [] for i in range(n)}
    for u, v, _ in edges:
        graph[u].append(v)
        indeg[v] += 1
    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    order: List[int] = []
    ambiguous_steps = 0
    while heap:
        if len(heap) > 1:
            ambiguous_steps += 1
        u = heapq.heappop(heap)
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    return order, ambiguous_steps


def generate(rng: random.Random) -> Problem:
    # The DAG is fixed, so this generator does not draw from rng.
    edges = [(u, v, None) for (u, v, _) in TEMPLATE_EDGES]
    for _ in range(400):
        order, ambiguous_steps = topo_stats(len(POSITIONS), edges)
        if len(order) == len(POSITIONS) and ambiguous_steps >= 1:
            render_edges = [(u, v, None, style) for (u, v, style) in TEMPLATE_EDGES]
            figure = render_graph(POSITIONS, render_edges, directed=True, weighted=False, title="DAG for topological sorting.")
            prompt = (
                "Compute a topological ordering for the directed acyclic graph below. "
                "If multiple choices are available at some step, note the available zero-indegree set."
            )
            solution = wrap_paragraph(f"One valid topological ordering is {format_sequence(order)}.")
            return Problem(
                section_title="Graphs",
                subsection_title="Topological Sort",
                body=build_document_body(prompt, figure=figure),
                notes=[
                    "topic=topological_sort",
                    f"vertices={len(POSITIONS)}",
                    f"edges={len(TEMPLATE_EDGES)}",
                    f"ambiguous_steps={ambiguous_steps}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial topological-sort instance.")
