"""Skip list stored as prescribed tower heights, so problems avoid coin-flip ambiguity."""

from __future__ import annotations

from typing import Dict, List


class SkipList:
    def __init__(self, max_level: int = 5) -> None:
        self.max_level = max_level
        self.heights: Dict[int, int] = {}

    def insert(self, key: int, height: int) -> None:
        self.heights[key] = min(height, self.max_level)

    def delete(self, key: int) -> None:
        self.heights.pop(key, None)

    def ordered_keys(self) -> List[int]:
        return sorted(self.heights)
