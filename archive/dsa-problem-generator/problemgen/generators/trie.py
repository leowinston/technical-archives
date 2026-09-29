"""Trie construction and deletion over word banks with shared prefixes."""

from __future__ import annotations

import random
from typing import List, Sequence

from problemgen.latex import build_document_body, format_word_list, make_centered, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import render_layout_tree, trie_to_layout
from problemgen.structures import Trie, TrieNode

TOPIC = "trie"
ALIASES = ()

WORD_BANKS: List[List[str]] = [
    ["map", "man", "many", "mat", "math", "me", "met", "meter", "meet", "meal"],
    ["apple", "apply", "app", "append", "apex", "ape", "apart", "apartment", "apt", "apricot"],
    ["code", "coder", "coding", "codex", "coil", "coin", "cold", "color", "column", "come"],
    ["star", "start", "stare", "stack", "stamp", "stand", "stay", "steam", "steel", "step"],
]


def count_branching_nodes(node: TrieNode) -> int:
    total = 1 if len(node.children) >= 2 else 0
    for child in node.children.values():
        total += count_branching_nodes(child)
    return total


def word_has_shared_prefix(words: Sequence[str], word: str) -> bool:
    # Any shared prefix includes the first letter, so this is the whole test.
    return any(w != word and w[:1] == word[:1] for w in words)


def generate(rng: random.Random) -> Problem:
    for _ in range(200):
        bank = list(rng.choice(WORD_BANKS))
        rng.shuffle(bank)
        words = sorted(bank[: rng.randint(8, 10)])
        trie = Trie()
        for word in words:
            trie.insert(word)
        branching_nodes = count_branching_nodes(trie.root)
        delete_candidates = [w for w in words if word_has_shared_prefix(words, w)]
        if branching_nodes < 3 or not delete_candidates:
            continue
        deletion = rng.choice(delete_candidates)
        trie.delete(deletion)
        prompt = (
            "Construct the standard trie for the word set "
            f"{format_word_list(words)}. Then delete the word "
            f"\\texttt{{{deletion}}}, carefully preserving shared-prefix paths "
            "and terminal markers."
        )
        solution = (
            wrap_paragraph(
                f"Final trie after deleting \\texttt{{{deletion}}}. Branching nodes in the original trie: {branching_nodes}."
            )
            + make_centered(render_layout_tree(trie_to_layout(trie.root, r"$\varepsilon$"), x_scale=1.15, y_scale=1.35))
        )
        return Problem(
            section_title="String-Based Structures",
            subsection_title="Trie Construction and Deletion",
            body=build_document_body(prompt),
            notes=[
                "topic=trie",
                f"branching_nodes={branching_nodes}",
                f"deleted_word={deletion}",
            ],
            solution=solution,
        )
    raise RuntimeError("Unable to generate a non-trivial trie instance.")
