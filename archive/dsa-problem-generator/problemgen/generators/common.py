"""Random-input helpers shared by several generators."""

from __future__ import annotations

import random
from typing import List


def sample_unique_ints(rng: random.Random, n: int, low: int = 1, high: int = 99) -> List[int]:
    return rng.sample(range(low, high + 1), n)


def generate_template_weights(
    rng: random.Random,
    edge_count: int,
    low: int,
    high: int,
    require_duplicate: bool = False,
) -> List[int]:
    """Draw one weight per template edge; optionally insist on at least one tie."""
    while True:
        weights = [rng.randint(low, high) for _ in range(edge_count)]
        if require_duplicate and len(set(weights)) == edge_count:
            continue
        return weights
