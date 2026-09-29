"""Every generator honors its non-triviality rules, and the CLI still works."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from typing import Callable, Dict

from problemgen import CANONICAL_TOPICS, TOPIC_ALIASES, CS253ProblemGenerator, resolve_topic

ROOT = Path(__file__).resolve().parent.parent
SEEDS = range(1, 41)

# The rejection rule each generator promises, read back from the notes it records.
RULES: Dict[str, Callable[[Dict[str, int]], bool]] = {
    "avl": lambda n: n["insert_rotations"] >= 2 and n["delete_rotations"] >= 1,
    "red_black": lambda n: n["insert_rotations"] >= 1
    and n["insert_recolors"] >= 3
    and n["delete_rotations"] + n["delete_recolors"] >= 1,
    "two_four": lambda n: n["splits"] >= 1 and n["merge_count"] + n["borrow_count"] >= 1,
    "skip_list": lambda n: n["promotions"] >= 5 and n["max_height"] >= 4,
    "trie": lambda n: n["branching_nodes"] >= 3,
    "counting_sort": lambda n: n["distinct_letters"] >= 4 and n["max_frequency"] >= 3,
    "radix_sort": lambda n: n["max_digits"] >= 4 and n["passes"] == n["max_digits"],
    "boyer_moore": lambda n: n["good_suffix_jumps"] >= 1 and n["match_count"] >= 1,
    "kmp": lambda n: n["max_failure"] >= 2 and n["fallbacks"] >= 2 and n["match_count"] >= 1,
    "knapsack": lambda n: n["optimal_value"] > n["greedy_value"] and n["optimal_value"] >= 10,
    "lcs": lambda n: n["lcs_length"] >= 3,
    "edit_distance": lambda n: 2 <= n["distance"] <= 5,
    "dijkstra": lambda n: n["improvement_count"] >= 2,
    "topological_sort": lambda n: n["ambiguous_steps"] >= 1,
    "prim": lambda n: n["rejected_edges"] >= 2,
    "kruskal": lambda n: n["rejected_edges"] >= 2,
    "hashing": lambda n: n["collisions"] >= 3,
    "rb_to_24": lambda n: n["red_nodes"] >= 2,
    "ford_fulkerson": lambda n: n["augmentations"] >= 3 and n["max_flow"] >= 10,
    "huffman": lambda n: n["distinct_chars"] >= 5
    and n["distinct_code_lengths"] >= 3
    and n["tied_weights"] >= 1
    and n["huffman_bits"] < n["fixed_bits"],
}


def numeric_notes(notes) -> Dict[str, int]:
    parsed: Dict[str, int] = {}
    for note in notes:
        key, _, value = note.partition("=")
        if value.lstrip("-").isdigit():
            parsed[key] = int(value)
    return parsed


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-B", str(ROOT / "cs253_problem_generator.py"), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class GeneratorTests(unittest.TestCase):
    def test_every_topic_has_a_rule(self) -> None:
        self.assertEqual(set(RULES), set(CANONICAL_TOPICS))

    def test_generated_problems_are_non_trivial(self) -> None:
        for topic in CANONICAL_TOPICS:
            for seed in SEEDS:
                with self.subTest(topic=topic, seed=seed):
                    problem = CS253ProblemGenerator(seed=seed).generate(topic)
                    self.assertEqual(problem.notes[0], f"topic={topic}")
                    self.assertTrue(problem.body.strip())
                    self.assertTrue(problem.solution.strip())
                    self.assertTrue(RULES[topic](numeric_notes(problem.notes)), problem.notes)

    def test_same_seed_gives_same_document(self) -> None:
        for topic in CANONICAL_TOPICS + ["random"]:
            first = CS253ProblemGenerator(seed=7).generate(topic).to_latex(7, with_solution=True)
            second = CS253ProblemGenerator(seed=7).generate(topic).to_latex(7, with_solution=True)
            self.assertEqual(first, second, topic)

    def test_different_seeds_give_different_problems(self) -> None:
        # topological_sort uses a fixed DAG, so it is the one topic that never varies.
        for topic in CANONICAL_TOPICS:
            if topic == "topological_sort":
                continue
            bodies = {CS253ProblemGenerator(seed=seed).generate(topic).body for seed in range(1, 6)}
            self.assertGreater(len(bodies), 1, topic)

    def test_string_matching_text_is_centered_not_inline(self) -> None:
        # \texttt never line-breaks, so an inline text string runs past the right margin.
        for topic in ("kmp", "boyer_moore"):
            for seed in SEEDS:
                with self.subTest(topic=topic, seed=seed):
                    body = CS253ProblemGenerator(seed=seed).generate(topic).body
                    prompt, _, rest = body.partition("\\begin{center}")
                    self.assertEqual(prompt.count("\\texttt{"), 1, prompt)  # only the short pattern
                    self.assertRegex(rest, r"^\n\\texttt\{[A-Z]+\}\n\\end\{center\}")

    def test_solution_only_appears_when_requested(self) -> None:
        problem = CS253ProblemGenerator(seed=1).generate("avl")
        self.assertNotIn("Instructor Reference", problem.to_latex(1))
        self.assertIn("Instructor Reference", problem.to_latex(1, with_solution=True))

    def test_aliases_resolve_to_canonical_topics(self) -> None:
        for alias, canonical in TOPIC_ALIASES.items():
            self.assertEqual(resolve_topic(alias), canonical)
            self.assertEqual(resolve_topic(alias.upper()), canonical)
        self.assertEqual(resolve_topic("rb"), "red_black")
        self.assertEqual(resolve_topic("2-4"), "two_four")
        self.assertEqual(resolve_topic("max-flow"), "ford_fulkerson")

    def test_unknown_topic_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown topic 'heapsort'"):
            CS253ProblemGenerator(seed=1).generate("heapsort")


class CLITests(unittest.TestCase):
    def test_list_topics(self) -> None:
        result = run_cli("--list-topics")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.split(), CANONICAL_TOPICS)

    def test_seeded_problem_matches_library_output(self) -> None:
        result = run_cli("--topic", "rb", "--seed", "475845898", "--with-solution")
        self.assertEqual(result.returncode, 0, result.stderr)
        expected = CS253ProblemGenerator(seed=475845898).generate("red_black").to_latex(475845898, with_solution=True)
        self.assertEqual(result.stdout, expected + "\n")
        self.assertIn("% seed=475845898", result.stdout)

    def test_unseeded_run_records_its_seed(self) -> None:
        result = run_cli("--topic", "kmp")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertRegex(result.stdout, r"% seed=\d+")

    def test_unknown_topic_fails(self) -> None:
        result = run_cli("--topic", "heapsort")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unknown topic", result.stderr)


if __name__ == "__main__":
    unittest.main()
