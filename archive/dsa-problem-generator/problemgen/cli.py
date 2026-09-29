"""Command-line interface: print one problem, or write a seeded set to a folder."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from problemgen.generators import CANONICAL_TOPICS, CS253ProblemGenerator

# Seeds used for the committed output/ folder.
OUTPUT_SEEDS = (1, 2, 3)

# Subfolder of output/ that each topic is filed under.
CATEGORIES: Dict[str, Sequence[str]] = {
    "trees": ("avl", "red_black", "two_four", "rb_to_24"),
    "data_structures": ("hashing", "skip_list"),
    "sorting": ("counting_sort", "radix_sort"),
    "text_processing": ("boyer_moore", "kmp", "trie", "huffman"),
    "dynamic_programming": ("knapsack", "lcs", "edit_distance"),
    "graphs": ("dijkstra", "topological_sort", "prim", "kruskal", "ford_fulkerson"),
}
TOPIC_CATEGORY: Dict[str, str] = {topic: category for category, topics in CATEGORIES.items() for topic in topics}


def write_outputs(out_dir: Path, seeds: Sequence[int] = OUTPUT_SEEDS) -> List[Path]:
    """Write output/<category>/<topic>/<topic>-seed<N>.tex with solutions for every topic.

    A seed whose problem repeats an earlier seed's (the topological-sort DAG is
    fixed, for example) is skipped rather than written twice.
    """
    written: List[Path] = []
    for topic in CANONICAL_TOPICS:
        seen_bodies = set()
        for seed in seeds:
            problem = CS253ProblemGenerator(seed=seed).generate(topic)
            if problem.body in seen_bodies:
                continue
            seen_bodies.add(problem.body)
            path = out_dir / TOPIC_CATEGORY[topic] / topic / f"{topic}-seed{seed}.tex"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(problem.to_latex(seed=seed, with_solution=True))
            written.append(path)
    return written


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate randomized CS 253 study problems as standalone LaTeX.")
    parser.add_argument(
        "--topic",
        default="random",
        help="Topic to generate. Examples: avl, rb, 2-4, skip-list, trie, kmp, dijkstra, hashing, huffman, random.",
    )
    parser.add_argument("--seed", type=int, default=None, help="Optional RNG seed for reproducible output.")
    parser.add_argument(
        "--with-solution",
        action="store_true",
        help="Append an instructor reference section with a solved end-state or table.",
    )
    parser.add_argument("--list-topics", action="store_true", help="Print supported canonical topics and exit.")
    parser.add_argument(
        "--write-all",
        metavar="DIR",
        type=Path,
        help=f"Write every topic with seeds {', '.join(map(str, OUTPUT_SEEDS))} and solutions to DIR, then exit.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    if args.list_topics:
        for topic in CANONICAL_TOPICS:
            print(topic)
        return
    if args.write_all is not None:
        paths = write_outputs(args.write_all)
        print(f"Wrote {len(paths)} problems to {args.write_all}")
        return
    generator = CS253ProblemGenerator(seed=args.seed)
    problem = generator.generate(args.topic)
    print(problem.to_latex(seed=generator.seed, with_solution=args.with_solution))
