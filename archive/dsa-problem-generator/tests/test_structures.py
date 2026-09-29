"""Invariant checks for the data structures after random insert/delete sequences."""

from __future__ import annotations

import random
import unittest
from typing import List, Optional

from problemgen.generators.rb_to_24 import rb_to_two_four
from problemgen.structures import AVLNode, AVLTree, BTreeNode, RBNode, RBTree, Trie, TwoFourTree, UnionFind

TRIALS = 300


def random_operations(rng: random.Random):
    inserts = rng.sample(range(1, 100), rng.randint(1, 25))
    deletions = rng.sample(inserts, rng.randint(0, len(inserts)))
    return inserts, deletions


def avl_inorder(node: Optional[AVLNode]) -> List[int]:
    if node is None:
        return []
    return avl_inorder(node.left) + [node.key] + avl_inorder(node.right)


def check_avl(testcase: unittest.TestCase, node: Optional[AVLNode]) -> int:
    if node is None:
        return 0
    left = check_avl(testcase, node.left)
    right = check_avl(testcase, node.right)
    testcase.assertLessEqual(abs(left - right), 1, f"unbalanced at {node.key}")
    testcase.assertEqual(node.height, 1 + max(left, right), f"stale height at {node.key}")
    return node.height


def rb_inorder(node: RBNode, nil: RBNode) -> List[int]:
    if node is nil:
        return []
    return rb_inorder(node.left, nil) + [node.key] + rb_inorder(node.right, nil)


def check_rb(testcase: unittest.TestCase, node: RBNode, nil: RBNode) -> int:
    """Return the black height, asserting no red-red edges and matching child black heights."""
    if node is nil:
        return 1
    for child in (node.left, node.right):
        if child is not nil:
            testcase.assertIs(child.parent, node, f"bad parent pointer under {node.key}")
            if node.color == "R":
                testcase.assertEqual(child.color, "B", f"red node {node.key} has a red child")
    left = check_rb(testcase, node.left, nil)
    right = check_rb(testcase, node.right, nil)
    testcase.assertEqual(left, right, f"black heights differ under {node.key}")
    return left + (1 if node.color == "B" else 0)


def check_two_four(testcase: unittest.TestCase, node: BTreeNode, is_root: bool = True) -> List[int]:
    """Assert node sizes, child counts, and key ordering. Return the leaf depths below node."""
    testcase.assertLessEqual(len(node.keys), 3)
    if not is_root:
        testcase.assertGreaterEqual(len(node.keys), 1)
    testcase.assertEqual(node.keys, sorted(node.keys))
    if node.leaf:
        testcase.assertEqual(node.children, [])
        return [0]
    testcase.assertEqual(len(node.children), len(node.keys) + 1)
    depths: List[int] = []
    for idx, child in enumerate(node.children):
        if idx > 0:
            testcase.assertTrue(all(k > node.keys[idx - 1] for k in two_four_keys(child)))
        if idx < len(node.keys):
            testcase.assertTrue(all(k < node.keys[idx] for k in two_four_keys(child)))
        depths.extend(d + 1 for d in check_two_four(testcase, child, is_root=False))
    return depths


def two_four_keys(node: BTreeNode) -> List[int]:
    if node.leaf:
        return list(node.keys)
    keys: List[int] = []
    for idx, child in enumerate(node.children):
        keys.extend(two_four_keys(child))
        if idx < len(node.keys):
            keys.append(node.keys[idx])
    return keys


class AVLTreeTests(unittest.TestCase):
    def test_balanced_and_sorted_after_random_operations(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            inserts, deletions = random_operations(rng)
            tree = AVLTree()
            for key in inserts:
                tree.insert(key)
            for key in deletions:
                tree.delete(key)
            self.assertEqual(avl_inorder(tree.root), sorted(set(inserts) - set(deletions)))
            check_avl(self, tree.root)

    def test_ascending_inserts_rotate(self) -> None:
        tree = AVLTree()
        for key in (1, 2, 3):
            tree.insert(key)
        self.assertEqual(tree.rotation_count, 1)
        self.assertEqual(tree.root.key, 2)


class RedBlackTreeTests(unittest.TestCase):
    def test_invariants_after_random_operations(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            inserts, deletions = random_operations(rng)
            tree = RBTree()
            for key in inserts:
                tree.insert(key)
            for key in deletions:
                tree.delete(key)
            self.assertEqual(rb_inorder(tree.root, tree.nil), sorted(set(inserts) - set(deletions)))
            if tree.root is not tree.nil:
                self.assertEqual(tree.root.color, "B")
                self.assertIs(tree.root.parent, tree.nil)
            check_rb(self, tree.root, tree.nil)

    def test_deleting_missing_key_is_a_no_op(self) -> None:
        tree = RBTree()
        for key in (10, 5, 15):
            tree.insert(key)
        tree.delete(99)
        self.assertEqual(rb_inorder(tree.root, tree.nil), [5, 10, 15])


class TwoFourTreeTests(unittest.TestCase):
    def test_invariants_after_random_operations(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            inserts, deletions = random_operations(rng)
            tree = TwoFourTree()
            for key in inserts:
                tree.insert(key)
            for key in deletions:
                tree.delete(key)
            self.assertEqual(two_four_keys(tree.root), sorted(set(inserts) - set(deletions)))
            depths = check_two_four(self, tree.root)
            self.assertEqual(len(set(depths)), 1, "leaves are at different depths")

    def test_fourth_key_splits_and_promotes_the_right_middle_key(self) -> None:
        tree = TwoFourTree()
        for key in (10, 20, 30, 40):
            tree.insert(key)
        self.assertEqual(tree.split_count, 1)
        self.assertEqual(tree.root.keys, [30])
        self.assertEqual([child.keys for child in tree.root.children], [[10, 20], [40]])


class RedBlackToTwoFourTests(unittest.TestCase):
    def test_conversion_is_a_valid_two_four_tree_with_the_same_keys(self) -> None:
        rng = random.Random(253)
        for _ in range(TRIALS):
            keys = rng.sample(range(1, 100), rng.randint(1, 25))
            tree = RBTree()
            for key in keys:
                tree.insert(key)
            converted = rb_to_two_four(tree.root, tree.nil)
            self.assertEqual(two_four_keys(converted), sorted(keys))
            depths = check_two_four(self, converted)
            self.assertEqual(len(set(depths)), 1)


class TrieTests(unittest.TestCase):
    def contains(self, trie: Trie, word: str) -> bool:
        node = trie.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.terminal

    def test_delete_keeps_shared_prefixes_and_prunes_dead_branches(self) -> None:
        trie = Trie()
        for word in ("app", "apple", "apply", "apt"):
            trie.insert(word)
        trie.delete("apple")
        self.assertFalse(self.contains(trie, "apple"))
        for word in ("app", "apply", "apt"):
            self.assertTrue(self.contains(trie, word))
        self.assertEqual(set(trie.root.children["a"].children["p"].children["p"].children["l"].children), {"y"})

        trie.delete("app")
        self.assertFalse(self.contains(trie, "app"))
        self.assertTrue(self.contains(trie, "apply"))


class UnionFindTests(unittest.TestCase):
    def test_union_reports_whether_sets_merged(self) -> None:
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.union(1, 2))
        self.assertFalse(uf.union(0, 2))
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertNotEqual(uf.find(0), uf.find(3))


if __name__ == "__main__":
    unittest.main()
