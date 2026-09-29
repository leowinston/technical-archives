"""0/1 knapsack DP, keeping only instances where greedy-by-ratio is suboptimal."""

from __future__ import annotations

import random
from typing import List, Sequence

from problemgen.latex import blank_cell, build_document_body, make_centered, make_table, wrap_paragraph
from problemgen.problem import Problem

TOPIC = "knapsack"
ALIASES = ()


def greedy_value(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    order = sorted(
        range(len(weights)),
        key=lambda i: (values[i] / weights[i], values[i], -weights[i]),
        reverse=True,
    )
    total_weight = 0
    total_value = 0
    for idx in order:
        if total_weight + weights[idx] <= capacity:
            total_weight += weights[idx]
            total_value += values[idx]
    return total_value


def knapsack_table(weights: Sequence[int], values: Sequence[int], capacity: int) -> List[List[int]]:
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if weights[i - 1] <= c:
                dp[i][c] = max(dp[i][c], values[i - 1] + dp[i - 1][c - weights[i - 1]])
    return dp


def generate(rng: random.Random) -> Problem:
    for _ in range(500):
        n = rng.randint(5, 6)
        weights = [rng.randint(1, 7) for _ in range(n)]
        values = [rng.randint(2, 15) for _ in range(n)]
        capacity = rng.randint(8, 12)
        greedy = greedy_value(weights, values, capacity)
        dp = knapsack_table(weights, values, capacity)
        optimal = dp[-1][-1]
        if optimal > greedy and optimal >= 10:
            header = ["i \\textbackslash\\ c"] + [str(c) for c in range(capacity + 1)]
            rows = [header, ["0"] + ["0"] * (capacity + 1)]
            for i in range(1, n + 1):
                rows.append([str(i), "0"] + [blank_cell() for _ in range(capacity)])
            solution_rows = [header]
            for i in range(n + 1):
                solution_rows.append([str(i)] + [str(v) for v in dp[i]])
            prompt = (
                f"Given a knapsack of capacity {capacity} with weights "
                f"$w = \\{{{', '.join(str(w) for w in weights)}\\}}$ and values "
                f"$v = \\{{{', '.join(str(v) for v in values)}\\}}$, complete the 0/1 knapsack "
                "dynamic-programming table and determine the optimal value."
            )
            solution = (
                wrap_paragraph(f"Greedy-by-ratio value: {greedy}. Optimal DP value: {optimal}.")
                + make_centered(make_table(solution_rows))
            )
            return Problem(
                section_title="Dynamic Programming",
                subsection_title="0/1 Knapsack",
                body=build_document_body(prompt, extras=make_centered(make_table(rows))),
                notes=[
                    "topic=knapsack",
                    f"greedy_value={greedy}",
                    f"optimal_value={optimal}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a knapsack instance where greedy fails.")
