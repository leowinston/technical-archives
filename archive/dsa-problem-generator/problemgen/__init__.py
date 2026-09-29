"""Randomized CS 253 tracing-problem generator.

The generator produces standalone LaTeX documents that follow the visual
conventions used in the supplied CS 253 study guide:
  * tikz-qtree for tree-style drawings
  * blacknode / white-filled red-node styling for red-black trees
  * matrix-based skip list drawings
  * explicit-coordinate graph layouts

Each topic lives in its own module under ``problemgen.generators``. A
generator simulates the algorithm on random inputs and rejects trivial
instances, so every problem it emits is worth tracing by hand.
"""

from problemgen.generators import (
    CANONICAL_TOPICS,
    GENERATORS,
    TOPIC_ALIASES,
    CS253ProblemGenerator,
    resolve_topic,
)
from problemgen.problem import Problem

__all__ = [
    "CANONICAL_TOPICS",
    "GENERATORS",
    "TOPIC_ALIASES",
    "CS253ProblemGenerator",
    "Problem",
    "resolve_topic",
]
