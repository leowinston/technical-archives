"""Topic registry: one module per topic, each exposing TOPIC, ALIASES, and generate(rng).

To add a topic, write a module with those three names and list it in MODULES.
"""

from __future__ import annotations

import random
from typing import Callable, Dict, List, Optional

from problemgen.generators import (
    avl,
    boyer_moore,
    counting_sort,
    dijkstra,
    edit_distance,
    ford_fulkerson,
    hashing,
    huffman,
    kmp,
    knapsack,
    kruskal,
    lcs,
    prim,
    radix_sort,
    rb_to_24,
    red_black,
    skip_list,
    topological_sort,
    trie,
    two_four,
)
from problemgen.problem import Problem

# Order matters: --topic random draws from this list, so reordering changes seeded output.
MODULES = [
    avl,
    red_black,
    two_four,
    skip_list,
    trie,
    counting_sort,
    radix_sort,
    boyer_moore,
    kmp,
    knapsack,
    lcs,
    edit_distance,
    dijkstra,
    topological_sort,
    prim,
    kruskal,
    hashing,
    rb_to_24,
    ford_fulkerson,
    huffman,
]

GENERATORS: Dict[str, Callable[[random.Random], Problem]] = {module.TOPIC: module.generate for module in MODULES}

CANONICAL_TOPICS: List[str] = list(GENERATORS)

TOPIC_ALIASES: Dict[str, str] = {"random": "random"}
for _module in MODULES:
    for _alias in (_module.TOPIC, *_module.ALIASES):
        TOPIC_ALIASES[_alias] = _module.TOPIC


def resolve_topic(topic: str) -> str:
    canonical = TOPIC_ALIASES.get(topic.lower(), topic.lower())
    if canonical != "random" and canonical not in GENERATORS:
        supported = ", ".join(sorted(CANONICAL_TOPICS))
        raise ValueError(f"Unknown topic '{topic}'. Supported topics: {supported}")
    return canonical


class CS253ProblemGenerator:
    """Seeded entry point: the same seed and topic always produce the same problem."""

    def __init__(self, seed: Optional[int] = None) -> None:
        self.seed = seed if seed is not None else random.SystemRandom().randrange(1, 10**9)
        self.rng = random.Random(self.seed)

    def generate(self, topic: str) -> Problem:
        canonical = resolve_topic(topic)
        if canonical == "random":
            canonical = self.rng.choice(CANONICAL_TOPICS)
        return GENERATORS[canonical](self.rng)
