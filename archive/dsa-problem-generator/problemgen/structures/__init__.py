"""Data structures the generators simulate to build problems and solutions."""

from problemgen.structures.avl import AVLNode, AVLTree
from problemgen.structures.red_black import RBNode, RBTree
from problemgen.structures.skip_list import SkipList
from problemgen.structures.trie import Trie, TrieNode
from problemgen.structures.two_four import BTreeNode, TwoFourTree
from problemgen.structures.union_find import UnionFind

__all__ = [
    "AVLNode",
    "AVLTree",
    "BTreeNode",
    "RBNode",
    "RBTree",
    "SkipList",
    "Trie",
    "TrieNode",
    "TwoFourTree",
    "UnionFind",
]
