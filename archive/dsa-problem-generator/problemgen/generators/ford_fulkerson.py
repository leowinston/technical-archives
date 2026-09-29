"""Ford-Fulkerson max flow (Edmonds-Karp BFS paths) needing at least three augmentations."""

from __future__ import annotations

import math
import random
from typing import Dict, List, Sequence, Tuple

from problemgen.generators.common import generate_template_weights
from problemgen.latex import build_document_body, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_flow_graph

TOPIC = "ford_fulkerson"
ALIASES = ("ff", "ford-fulkerson", "max-flow", "max_flow")

POSITIONS: Dict[int, Tuple[float, float]] = {
    0: (0.0, 0.0),   # s
    1: (2.8, 2.4),   # a
    2: (2.8, -2.4),  # b
    3: (6.0, 2.6),   # c
    4: (6.0, -2.6),  # d
    5: (8.8, 0.0),   # t
}

LABELS: Dict[int, str] = {
    0: "s",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "t",
}

TEMPLATE_EDGES: List[Tuple[int, int]] = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 1),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 4),
    (4, 3),
    (3, 5),
    (4, 5),
]

SOURCE = 0
SINK = 5


def edmonds_karp(
    n: int,
    edges: Sequence[Tuple[int, int, int]],
    source: int,
    sink: int,
) -> Tuple[int, List[Tuple[List[int], int]], Dict[Tuple[int, int], int]]:
    """Return (max flow value, [(augmenting path, bottleneck)], final flow per edge)."""
    capacity: Dict[Tuple[int, int], int] = {}
    for u, v, c in edges:
        capacity[(u, v)] = capacity.get((u, v), 0) + c
        capacity.setdefault((v, u), 0)

    residual: Dict[Tuple[int, int], int] = dict(capacity)
    flow: Dict[Tuple[int, int], int] = {(u, v): 0 for u, v, _ in edges}

    adj: Dict[int, List[int]] = {i: [] for i in range(n)}
    for u, v, _ in edges:
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    augmentations: List[Tuple[List[int], int]] = []
    total_flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q: List[int] = [source]
        for x in q:
            for y in adj[x]:
                if parent[y] == -1 and residual.get((x, y), 0) > 0:
                    parent[y] = x
                    q.append(y)
                    if y == sink:
                        break
            if parent[sink] != -1:
                break
        if parent[sink] == -1:
            break

        path: List[int] = []
        v = sink
        bottleneck = math.inf
        while v != source:
            u = parent[v]
            path.append(v)
            bottleneck = min(bottleneck, residual[(u, v)])
            v = u
        path.append(source)
        path.reverse()
        b = int(bottleneck)

        v = sink
        while v != source:
            u = parent[v]
            residual[(u, v)] -= b
            residual[(v, u)] = residual.get((v, u), 0) + b
            if (u, v) in flow:
                flow[(u, v)] += b
            elif (v, u) in flow:
                flow[(v, u)] -= b
            v = u

        total_flow += b
        augmentations.append((path, b))

    return total_flow, augmentations, flow


def generate(rng: random.Random) -> Problem:
    n = len(POSITIONS)
    for _ in range(500):
        capacities = generate_template_weights(rng, len(TEMPLATE_EDGES), 2, 14, require_duplicate=True)
        edges = [(u, v, c) for (u, v), c in zip(TEMPLATE_EDGES, capacities)]
        max_flow, augmentations, final_flow = edmonds_karp(n, edges, SOURCE, SINK)
        if max_flow < 10 or len(augmentations) < 3:
            continue
        used_edges = sum(1 for (u, v, _) in edges if final_flow.get((u, v), 0) > 0)
        if used_edges < 5:
            continue

        figure = render_flow_graph(
            POSITIONS,
            LABELS,
            edges,
            title="Flow network with capacities for Ford-Fulkerson tracing.",
        )
        prompt = (
            "Starting with an initial flow of 0 on every edge, perform the Ford-Fulkerson algorithm "
            "to find the maximum flow from $s$ to $t$. For each iteration, show the augmenting path, "
            "its bottleneck capacity, and the updated flow values."
        )
        arrow = r"$\to$"
        path_text = "; ".join(
            f"{arrow.join(LABELS[v] for v in path)} (bottleneck {b})"
            for path, b in augmentations
        )
        flow_items = ", ".join(
            f"{LABELS[u]}{arrow}{LABELS[v]}:{final_flow[(u, v)]}/{cap}"
            for u, v, cap in edges
        )
        solution = (
            wrap_paragraph(f"Maximum flow value: {max_flow}.")
            + wrap_paragraph(f"Augmenting path sequence: {path_text}.")
            + wrap_paragraph(f"Final edge flows (flow/capacity): {flow_items}.")
        )
        return Problem(
            section_title="Graphs",
            subsection_title="Ford-Fulkerson Maximum Flow",
            body=build_document_body(prompt, figure=figure),
            notes=[
                "topic=ford_fulkerson",
                f"vertices={n}",
                f"edges={len(edges)}",
                f"augmentations={len(augmentations)}",
                f"max_flow={max_flow}",
            ],
            solution=solution,
        )
    raise RuntimeError("Unable to generate a non-trivial Ford-Fulkerson instance.")
