"""Huffman coding of a random string, with a stated tie-break so the tree is unique."""

from __future__ import annotations

import heapq
import math
import random
import string
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from problemgen.latex import build_document_body, make_centered, make_table, wrap_paragraph
from problemgen.problem import Problem
from problemgen.render import LayoutNode, render_layout_tree

TOPIC = "huffman"
ALIASES = ("huffman-coding", "huffman-code")


@dataclass
class HuffmanNode:
    weight: int
    chars: str  # sorted characters under this node; chars[0] is the tie-break key
    left: Optional["HuffmanNode"] = None
    right: Optional["HuffmanNode"] = None

    @property
    def is_leaf(self) -> bool:
        return self.left is None


def build_huffman_tree(freqs: Dict[str, int]) -> Tuple[HuffmanNode, List[Tuple[HuffmanNode, HuffmanNode, HuffmanNode]]]:
    """Merge the two lightest trees until one remains; return (root, merges in order).

    Ties on weight go to the tree holding the alphabetically smallest character. Trees
    are disjoint, so that key never ties and the tree is unique. The first tree
    removed becomes the left (0) child.
    """
    heap = [(w, ch, HuffmanNode(w, ch)) for ch, w in freqs.items()]
    heapq.heapify(heap)
    merges: List[Tuple[HuffmanNode, HuffmanNode, HuffmanNode]] = []
    while len(heap) > 1:
        _, _, first = heapq.heappop(heap)
        _, _, second = heapq.heappop(heap)
        merged = HuffmanNode(first.weight + second.weight, "".join(sorted(first.chars + second.chars)), first, second)
        merges.append((first, second, merged))
        heapq.heappush(heap, (merged.weight, merged.chars[0], merged))
    return heap[0][2], merges


def codewords(root: HuffmanNode) -> Dict[str, str]:
    codes: Dict[str, str] = {}

    def walk(node: HuffmanNode, prefix: str) -> None:
        if node.is_leaf:
            codes[node.chars] = prefix
            return
        walk(node.left, prefix + "0")
        walk(node.right, prefix + "1")

    walk(root, "")
    return codes


def encode(text: str, codes: Dict[str, str]) -> str:
    return "".join(codes[ch] for ch in text)


def decode(bits: str, root: HuffmanNode) -> str:
    out: List[str] = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.is_leaf:
            out.append(node.chars)
            node = root
    if node is not root:
        raise ValueError("bit string ends in the middle of a codeword")
    return "".join(out)


def tree_label(node: HuffmanNode) -> str:
    return f"\\texttt{{{node.chars}}}\\,({node.weight})"


def to_layout(node: HuffmanNode, bit: str = "") -> LayoutNode:
    if node.is_leaf:
        return LayoutNode(label=f"\\texttt{{{node.chars}}}:{node.weight}", style="listnode", edge_label=bit)
    children = [to_layout(node.left, "0"), to_layout(node.right, "1")]
    return LayoutNode(label=str(node.weight), style="every tree node", children=children, edge_label=bit)


def random_text(rng: random.Random) -> str:
    letters = sorted(rng.sample(string.ascii_lowercase[:16], rng.randint(5, 7)))
    counts = [rng.choice((1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8)) for _ in letters]
    chars = [ch for ch, c in zip(letters, counts) for _ in range(c)]
    rng.shuffle(chars)
    return "".join(chars)


def generate(rng: random.Random) -> Problem:
    for _ in range(400):
        text = random_text(rng)
        freqs = dict(sorted(Counter(text).items()))
        if not 20 <= len(text) <= 32:
            continue
        root, merges = build_huffman_tree(freqs)
        codes = codewords(root)
        lengths = {len(code) for code in codes.values()}
        huffman_bits = len(encode(text, codes))
        fixed_width = math.ceil(math.log2(len(freqs)))
        fixed_bits = fixed_width * len(text)
        tied_weights = len(freqs) - len(set(freqs.values()))
        if len(lengths) < 3 or huffman_bits >= fixed_bits or tied_weights < 1:
            continue

        message = "".join(rng.choice(sorted(freqs)) for _ in range(5))
        message_bits = encode(message, codes)
        prompt = (
            f"Consider the string \\texttt{{{text}}} of length {len(text)}.\n\n"
            "\\begin{enumerate}[label=(\\alph*)]\n"
            "  \\item Give the frequency of each character.\n"
            "  \\item Build the Huffman tree. At each step remove the two trees of smallest total frequency; "
            "when frequencies tie, remove first the tree containing the alphabetically smallest character. "
            "The first tree removed becomes the left child, and left edges are labeled 0, right edges 1.\n"
            "  \\item List the codeword for each character.\n"
            "  \\item How many bits does the Huffman encoding of the string use? Compare this with a "
            f"fixed-length code, which needs {fixed_width} bits per character.\n"
            f"  \\item Decode the bit string \\texttt{{{message_bits}}} using your tree.\n"
            "\\end{enumerate}"
        )

        freq_table = make_table(
            [["Character"] + [f"\\texttt{{{ch}}}" for ch in freqs], ["Frequency"] + [str(w) for w in freqs.values()]],
            align="|l|" + "c|" * len(freqs),
        )
        merge_rows = [["Step", "First removed (0)", "Second removed (1)", "New tree"]]
        for step, (first, second, merged) in enumerate(merges, 1):
            merge_rows.append([str(step), tree_label(first), tree_label(second), tree_label(merged)])
        code_rows = [["Character", "Frequency", "Codeword", "Bits"]]
        for ch, weight in sorted(freqs.items(), key=lambda item: (len(codes[item[0]]), codes[item[0]])):
            code_rows.append([f"\\texttt{{{ch}}}", str(weight), f"\\texttt{{{codes[ch]}}}", f"{weight} $\\times$ {len(codes[ch])} = {weight * len(codes[ch])}"])
        savings = fixed_bits - huffman_bits
        solution = (
            wrap_paragraph("(a) Frequencies:")
            + make_centered(freq_table)
            + "\n"
            + wrap_paragraph("(b) Merges in order:")
            + make_centered(make_table(merge_rows, align="|c|l|l|l|"))
            + "\n"
            + make_centered(render_layout_tree(to_layout(root), x_scale=1.3, y_scale=1.3))
            + "\n"
            + wrap_paragraph("(c) Codewords:")
            + make_centered(make_table(code_rows, align="|c|c|c|c|"))
            + "\n"
            + wrap_paragraph(
                f"(d) Huffman encoding: {huffman_bits} bits. Fixed-length: {len(text)} $\\times$ {fixed_width} = "
                f"{fixed_bits} bits, so Huffman saves {savings} bits."
            )
            + "\n"
            + wrap_paragraph(f"(e) \\texttt{{{message_bits}}} decodes to \\texttt{{{message}}}.")
        )
        return Problem(
            section_title="Greedy Algorithms",
            subsection_title="Huffman Coding",
            body=build_document_body(prompt),
            notes=[
                "topic=huffman",
                f"distinct_chars={len(freqs)}",
                f"text_length={len(text)}",
                f"distinct_code_lengths={len(lengths)}",
                f"tied_weights={tied_weights}",
                f"huffman_bits={huffman_bits}",
                f"fixed_bits={fixed_bits}",
            ],
            solution=solution,
        )
    raise RuntimeError("Unable to generate a non-trivial Huffman instance.")
