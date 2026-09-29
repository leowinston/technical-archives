"""Edit distance DP between a CS word and a randomly mutated copy of it."""

from __future__ import annotations

import random
from typing import List

from problemgen.latex import blank_cell, build_document_body, make_centered, make_table, wrap_paragraph
from problemgen.problem import Problem

TOPIC = "edit_distance"
ALIASES = ("edit", "edit-distance")

BASE_WORDS = ["algorithm", "datastruct", "dynamic", "analysis", "pattern", "network"]


def edit_distance_table(a: str, b: str) -> List[List[int]]:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost,
            )
    return dp


def mutate_word(rng: random.Random, word: str) -> str:
    chars = list(word)
    alphabet = "algorithmcs"
    actions = rng.randint(2, 4)
    for _ in range(actions):
        op = rng.choice(["replace", "insert", "delete"])
        if op == "replace" and chars:
            idx = rng.randrange(len(chars))
            chars[idx] = rng.choice(alphabet)
        elif op == "insert":
            idx = rng.randrange(len(chars) + 1)
            chars.insert(idx, rng.choice(alphabet))
        elif op == "delete" and len(chars) > 4:
            idx = rng.randrange(len(chars))
            chars.pop(idx)
    return "".join(chars)


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        a = rng.choice(BASE_WORDS)
        b = mutate_word(rng, a)
        if not (5 <= len(b) <= 11):
            continue
        dp = edit_distance_table(a, b)
        distance = dp[-1][-1]
        if 2 <= distance <= 5:
            rows = [["", "$\\varepsilon$"] + list(b)]
            rows.append(["$\\varepsilon$"] + [str(v) for v in dp[0]])
            for i, ch in enumerate(a, 1):
                rows.append([ch, str(i)] + [blank_cell() for _ in b])
            solution_rows = [["", "$\\varepsilon$"] + list(b)]
            solution_rows.append(["$\\varepsilon$"] + [str(v) for v in dp[0]])
            for i, ch in enumerate(a, 1):
                solution_rows.append([ch] + [str(v) for v in dp[i]])
            prompt = (
                f'Compute the edit distance between the strings \\texttt{{{a}}} and \\texttt{{{b}}}. '
                "The base cases are already filled in; complete the rest of the dynamic-programming table."
            )
            solution = (
                wrap_paragraph(f"Edit distance: {distance}.")
                + make_centered(make_table(solution_rows))
            )
            return Problem(
                section_title="Dynamic Programming",
                subsection_title="Edit Distance",
                body=build_document_body(prompt, extras=make_centered(make_table(rows))),
                notes=[
                    "topic=edit_distance",
                    f"distance={distance}",
                ],
                solution=solution,
            )
    raise RuntimeError("Unable to generate a non-trivial edit-distance instance.")
