"""Standard trie with prefix-pruning deletion."""

from __future__ import annotations

from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.terminal = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.terminal = True

    def delete(self, word: str) -> None:
        self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if node.terminal:
                node.terminal = False
            return not node.children and not node.terminal
        ch = word[depth]
        child = node.children.get(ch)
        if child is None:
            return False
        should_prune = self._delete(child, word, depth + 1)
        if should_prune:
            del node.children[ch]
        return not node.children and not node.terminal
