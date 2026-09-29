"""Each generator's solver checked against an independent brute-force answer."""

from __future__ import annotations

import itertools
import math
import random
import unittest
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from typing import List, Sequence, Tuple

from problemgen.generators import boyer_moore, counting_sort, dijkstra, edit_distance, ford_fulkerson, huffman
from problemgen.generators import kmp, knapsack, kruskal, lcs, prim, radix_sort, topological_sort
from problemgen.render import render_skip_list
from problemgen.structures import SkipList

TRIALS = 200


def all_matches(text: str, pattern: str) -> List[int]:
    return [i for i in range(len(text) - len(pattern) + 1) if text.startswith(pattern, i)]


def random_text(rng: random.Random, pattern: str) -> str:
    alphabet = sorted(set(pattern))
    text = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 30)))
    cut = rng.randint(0, len(text))
    return text[:cut] + pattern + text[cut:]


def weighted_edges(rng: random.Random, template: Sequence[Tuple[int, ...]]) -> List[Tuple[int, int, int]]:
    return [(edge[0], edge[1], rng.randint(1, 9)) for edge in template]


def is_spanning_tree(n: int, edges: Sequence[Tuple[int, int, int]]) -> bool:
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x

    for u, v, _ in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len(edges) == n - 1


def brute_force_mst_weight(n: int, edges: Sequence[Tuple[int, int, int]]) -> int:
    return min(
        sum(w for _, _, w in subset)
        for subset in itertools.combinations(edges, n - 1)
        if is_spanning_tree(n, subset)
    )


class StringMatchingTests(unittest.TestCase):
    def test_kmp_failure_function_matches_definition(self) -> None:
        for pattern in kmp.PATTERNS + ["AAAA", "ABCD", "AABAAAB"]:
            expected = [
                max(k for k in range(i + 1) if pattern[:k] == pattern[i + 1 - k : i + 1])
                for i in range(len(pattern))
            ]
            self.assertEqual(kmp.failure_function(pattern), expected, pattern)

    def test_kmp_finds_every_match(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            pattern = rng.choice(kmp.PATTERNS)
            text = random_text(rng, pattern)
            self.assertEqual(kmp.search_stats(text, pattern)[1], all_matches(text, pattern))

    def test_boyer_moore_finds_every_match(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            pattern = rng.choice(boyer_moore.PATTERNS)
            text = random_text(rng, pattern)
            self.assertEqual(boyer_moore.search_stats(text, pattern)[1], all_matches(text, pattern))


class SortingTests(unittest.TestCase):
    def test_radix_passes_are_stable_digit_sorts(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            values = [rng.randint(0, 9999) for _ in range(rng.randint(1, 12))]
            passes = radix_sort.radix_passes(values)
            self.assertEqual(len(passes), len(str(max(values))))
            for k, arr in enumerate(passes, 1):
                # Python's sort is stable, so this is what a correct LSD pass must produce.
                self.assertEqual(arr, sorted(values, key=lambda v: v % 10**k))
            self.assertEqual(passes[-1], sorted(values))

    def test_counting_sort_start_indices(self) -> None:
        self.assertEqual(counting_sort.start_indices([3, 0, 2, 4, 1]), [0, 3, 3, 5, 9])


class DynamicProgrammingTests(unittest.TestCase):
    def test_knapsack_matches_brute_force(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            n = rng.randint(1, 7)
            weights = [rng.randint(1, 7) for _ in range(n)]
            values = [rng.randint(1, 15) for _ in range(n)]
            capacity = rng.randint(0, 14)
            best = max(
                sum(values[i] for i in subset)
                for r in range(n + 1)
                for subset in itertools.combinations(range(n), r)
                if sum(weights[i] for i in subset) <= capacity
            )
            self.assertEqual(knapsack.knapsack_table(weights, values, capacity)[-1][-1], best)
            self.assertLessEqual(knapsack.greedy_value(weights, values, capacity), best)

    def test_lcs_matches_brute_force(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            a = "".join(rng.choice("ABCDE") for _ in range(rng.randint(0, 7)))
            b = "".join(rng.choice("ABCDE") for _ in range(rng.randint(0, 7)))

            def is_subsequence(s: str, t: str) -> bool:
                it = iter(t)
                return all(ch in it for ch in s)

            best = max(
                r
                for r in range(len(a) + 1)
                for idx in itertools.combinations(range(len(a)), r)
                if is_subsequence("".join(a[i] for i in idx), b)
            )
            self.assertEqual(lcs.lcs_table(a, b)[-1][-1], best, (a, b))

    def test_edit_distance_matches_recursive_definition(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            a = rng.choice(edit_distance.BASE_WORDS)
            b = edit_distance.mutate_word(rng, a)

            @lru_cache(maxsize=None)
            def dist(i: int, j: int) -> int:
                if i == 0 or j == 0:
                    return i + j
                return min(
                    dist(i - 1, j) + 1,
                    dist(i, j - 1) + 1,
                    dist(i - 1, j - 1) + (a[i - 1] != b[j - 1]),
                )

            self.assertEqual(edit_distance.edit_distance_table(a, b)[-1][-1], dist(len(a), len(b)))


class GraphTests(unittest.TestCase):
    def test_dijkstra_matches_bellman_ford(self) -> None:
        rng = random.Random(253)
        n = len(dijkstra.POSITIONS)
        for _ in range(TRIALS):
            edges = weighted_edges(rng, dijkstra.TEMPLATE_EDGES)
            expected = [math.inf] * n
            expected[0] = 0
            for _ in range(n - 1):
                for u, v, w in edges:
                    expected[v] = min(expected[v], expected[u] + w)
            dist, _, parent = dijkstra.dijkstra_stats(n, edges)
            self.assertEqual(dist, expected)
            weight = {(u, v): w for u, v, w in edges}
            for v, p in enumerate(parent):
                if p is not None:
                    self.assertEqual(dist[v], dist[p] + weight[(p, v)])

    def test_topological_order_respects_every_edge(self) -> None:
        edges = [(u, v, None) for u, v, _ in topological_sort.TEMPLATE_EDGES]
        order, ambiguous = topological_sort.topo_stats(len(topological_sort.POSITIONS), edges)
        self.assertEqual(sorted(order), list(range(len(topological_sort.POSITIONS))))
        position = {vertex: idx for idx, vertex in enumerate(order)}
        for u, v, _ in edges:
            self.assertLess(position[u], position[v])
        self.assertGreaterEqual(ambiguous, 1)

    def test_prim_and_kruskal_find_minimum_spanning_trees(self) -> None:
        rng = random.Random(253)
        for module, stats in ((prim, prim.prim_stats), (kruskal, kruskal.kruskal_stats)):
            n = len(module.POSITIONS)
            for _ in range(40):
                edges = weighted_edges(rng, module.TEMPLATE_EDGES)
                mst, _ = stats(n, edges)
                self.assertTrue(is_spanning_tree(n, mst))
                self.assertEqual(sum(w for _, _, w in mst), brute_force_mst_weight(n, edges))

    def test_max_flow_equals_min_cut_and_flow_is_feasible(self) -> None:
        rng = random.Random(253)
        n = len(ford_fulkerson.POSITIONS)
        source, sink = ford_fulkerson.SOURCE, ford_fulkerson.SINK
        inner = [v for v in range(n) if v not in (source, sink)]
        for _ in range(TRIALS):
            edges = [(u, v, rng.randint(2, 14)) for u, v in ford_fulkerson.TEMPLATE_EDGES]
            value, augmentations, flow = ford_fulkerson.edmonds_karp(n, edges, source, sink)
            min_cut = min(
                sum(c for u, v, c in edges if u in side and v not in side)
                for r in range(len(inner) + 1)
                for chosen in itertools.combinations(inner, r)
                for side in [{source, *chosen}]
            )
            self.assertEqual(value, min_cut)
            self.assertEqual(value, sum(b for _, b in augmentations))
            for u, v, c in edges:
                self.assertTrue(0 <= flow[(u, v)] <= c)
            for vertex in inner:
                inflow = sum(flow[(u, v)] for u, v, _ in edges if v == vertex)
                outflow = sum(flow[(u, v)] for u, v, _ in edges if u == vertex)
                self.assertEqual(inflow, outflow)


def brute_force_prefix_code_cost(weights: Sequence[int]) -> int:
    """Cheapest sum of weight * length over code lengths satisfying Kraft with equality."""
    k = len(weights)
    heaviest_first = sorted(weights, reverse=True)
    best = math.inf
    for lengths in itertools.combinations_with_replacement(range(1, k), k):
        if sum(Fraction(1, 2**length) for length in lengths) == 1:
            best = min(best, sum(w * length for w, length in zip(heaviest_first, lengths)))
    return best


class HuffmanTests(unittest.TestCase):
    def test_huffman_cost_is_optimal(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            freqs = {ch: rng.randint(1, 9) for ch in "abcdefg"[: rng.randint(2, 7)]}
            root, merges = huffman.build_huffman_tree(freqs)
            codes = huffman.codewords(root)
            cost = sum(freqs[ch] * len(code) for ch, code in codes.items())
            self.assertEqual(cost, brute_force_prefix_code_cost(list(freqs.values())), freqs)
            self.assertEqual(len(merges), len(freqs) - 1)
            self.assertEqual(root.weight, sum(freqs.values()))

    def test_codes_are_prefix_free_and_round_trip(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            text = huffman.random_text(rng)
            root, _ = huffman.build_huffman_tree(dict(Counter(text)))
            codes = huffman.codewords(root)
            for a, b in itertools.permutations(codes.values(), 2):
                self.assertFalse(b.startswith(a), (a, b))
            self.assertEqual(huffman.decode(huffman.encode(text, codes), root), text)

    def test_tie_break_ignores_input_order(self) -> None:
        freqs = {"a": 2, "b": 2, "c": 2, "d": 2, "e": 4}
        expected = huffman.codewords(huffman.build_huffman_tree(freqs)[0])
        # a and b tie at the start, so the rule makes a the left child of their merge.
        self.assertEqual(expected["a"], expected["b"][:-1] + "0")
        for _ in range(20):
            items = list(freqs.items())
            random.Random(_).shuffle(items)
            self.assertEqual(huffman.codewords(huffman.build_huffman_tree(dict(items))[0]), expected)


class SkipListRenderTests(unittest.TestCase):
    def test_arrows_only_reference_occupied_cells(self) -> None:
        skip_list = SkipList(5)
        for key, height in ((10, 1), (20, 3), (30, 1), (40, 5)):
            skip_list.insert(key, height)
        drawing = render_skip_list(skip_list)
        # Top row (level 5) holds only the sentinels and 40: columns 1, 5, 6.
        self.assertIn(r"\draw[->] (m-1-1) -- (m-1-5);", drawing)
        self.assertIn(r"\draw[->] (m-1-5) -- (m-1-6);", drawing)
        self.assertNotIn("(m-1-2)", drawing)
        # Base row links every column.
        for col in range(1, 6):
            self.assertIn(f"(m-5-{col}) -- (m-5-{col + 1})", drawing)


if __name__ == "__main__":
    unittest.main()
