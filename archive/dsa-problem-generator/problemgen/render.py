"""TikZ drawings for trees, skip lists, and graphs."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

from problemgen.latex import latex_escape
from problemgen.structures import AVLNode, BTreeNode, RBNode, SkipList, TrieNode


@dataclass
class LayoutNode:
    label: str
    style: str
    children: List["LayoutNode"] = field(default_factory=list)
    edge_label: str = ""  # drawn on the edge from this node's parent, e.g. a Huffman bit


def render_positioned_tree(
    positions: Dict[int, Tuple[float, float]],
    edges: Sequence[Tuple[int, int]],
    tokens: Dict[int, Tuple[str, str]],
    x_scale: float,
    y_scale: float,
    edge_labels: Optional[Dict[Tuple[int, int], str]] = None,
) -> str:
    lines = ["\\begin{tikzpicture}[>={Stealth[length=2mm]}]"]
    for node_id, (x, y) in sorted(positions.items()):
        style, label = tokens[node_id]
        lines.append(f"  \\node[{style}] (n{node_id}) at ({x * x_scale:.2f}, {y * y_scale:.2f}) {{{label}}};")
    for parent, child in edges:
        label = (edge_labels or {}).get((parent, child), "")
        if label:
            side = "above left" if positions[child][0] < positions[parent][0] else "above right"
            lines.append(f"  \\draw (n{parent}) -- node[midway, {side}, inner sep=1pt] {{{label}}} (n{child});")
        else:
            lines.append(f"  \\draw (n{parent}) -- (n{child});")
    lines.append("\\end{tikzpicture}")
    return "\n".join(lines)


def render_layout_tree(root: LayoutNode, x_scale: float = 1.6, y_scale: float = 1.5) -> str:
    """Place leaves left to right and center each parent over its children."""
    positions: Dict[int, Tuple[float, float]] = {}
    edges: List[Tuple[int, int]] = []
    tokens: Dict[int, Tuple[str, str]] = {}
    edge_labels: Dict[Tuple[int, int], str] = {}
    next_id = 0
    leaf_index = 0

    def walk(current: LayoutNode, depth: int) -> Tuple[float, int]:
        nonlocal next_id, leaf_index
        node_id = next_id
        next_id += 1
        tokens[node_id] = (current.style, current.label)
        child_xs: List[float] = []
        for child in current.children:
            child_x, child_id = walk(child, depth + 1)
            child_xs.append(child_x)
            edges.append((node_id, child_id))
            if child.edge_label:
                edge_labels[(node_id, child_id)] = child.edge_label
        if child_xs:
            x = sum(child_xs) / len(child_xs)
        else:
            x = float(leaf_index)
            leaf_index += 1
        positions[node_id] = (x, -depth)
        return x, node_id

    walk(root, 0)
    return render_positioned_tree(positions, edges, tokens, x_scale=x_scale, y_scale=y_scale, edge_labels=edge_labels)


def render_avl_tree(node: Optional[AVLNode]) -> str:
    if node is None:
        return "\\begin{tikzpicture}\n\\end{tikzpicture}"

    def convert(current: AVLNode) -> LayoutNode:
        children = [convert(child) for child in (current.left, current.right) if child is not None]
        return LayoutNode(label=str(current.key), style="every tree node", children=children)

    return render_layout_tree(convert(node), x_scale=1.8, y_scale=1.6)


def render_rb_tree(node: RBNode, nil: RBNode) -> str:
    if node is nil:
        return "\\begin{tikzpicture}\n\\end{tikzpicture}"

    def convert(current: RBNode) -> LayoutNode:
        children = [convert(child) for child in (current.left, current.right) if child is not nil]
        style = "blacknode" if current.color == "B" else "rednode"
        return LayoutNode(label=str(current.key), style=style, children=children)

    return render_layout_tree(convert(node), x_scale=1.8, y_scale=1.6)


def two_four_to_layout(node: Optional[BTreeNode]) -> LayoutNode:
    assert node is not None and (node.keys or not node.leaf)
    label = r" $\mid$ ".join(str(k) for k in node.keys)
    children = [two_four_to_layout(child) for child in node.children]
    return LayoutNode(label=label, style="listnode", children=children)


def trie_to_layout(node: TrieNode, label: str) -> LayoutNode:
    token_text = label if label.startswith("$") and label.endswith("$") else latex_escape(label)
    children = [trie_to_layout(node.children[ch], ch) for ch in sorted(node.children)]
    if node.terminal:
        children.append(LayoutNode(label="T", style="tfnode"))
    return LayoutNode(label=token_text, style="listnode", children=children)


def render_skip_list(skip_list: SkipList) -> str:
    keys = skip_list.ordered_keys()
    rows: List[str] = []
    columns = ["$-\\infty$"] + [str(k) for k in keys] + ["$+\\infty$"]
    for level in range(skip_list.max_level, 0, -1):
        row_cells = []
        for idx, label in enumerate(columns):
            if idx == 0 or idx == len(columns) - 1:
                row_cells.append(label)
            else:
                key = int(label)
                row_cells.append(label if skip_list.heights[key] >= level else "")
        rows.append("    " + " & ".join(row_cells) + r" \\")
    matrix_rows = "\n".join(rows)
    arrow_lines: List[str] = []
    for row in range(1, skip_list.max_level + 1):
        # Empty matrix cells have no TikZ node, so link each occupied cell to the next one.
        level = skip_list.max_level - row + 1
        occupied = [
            col
            for col, label in enumerate(columns, 1)
            if col in (1, len(columns)) or skip_list.heights[int(label)] >= level
        ]
        for left, right in zip(occupied, occupied[1:]):
            arrow_lines.append(f"\\draw[->] (m-{row}-{left}) -- (m-{row}-{right});")
    horiz = "\n".join(arrow_lines)
    return (
        "\\begin{tikzpicture}[>={Stealth[length=2mm]}]\n"
        "\\matrix (m) [matrix of nodes, nodes={skipnode}, column sep=0.3cm, row sep=0.5cm] {\n"
        + matrix_rows
        + "\n};\n"
        + horiz
        + "\n\\end{tikzpicture}"
    )


def angle_to_label(dx: float, dy: float) -> str:
    angle = (math.degrees(math.atan2(dy, dx)) + 360.0) % 360.0
    directions = [
        (22.5, "right"),
        (67.5, "above right"),
        (112.5, "above"),
        (157.5, "above left"),
        (202.5, "left"),
        (247.5, "below left"),
        (292.5, "below"),
        (337.5, "below right"),
        (360.5, "right"),
    ]
    for boundary, label in directions:
        if angle < boundary:
            return label
    return "above"


def render_graph(
    positions: Dict[int, Tuple[float, float]],
    edges: Sequence[Tuple[int, int, Optional[int], str]],
    directed: bool,
    weighted: bool,
    title: Optional[str] = None,
) -> str:
    header = "[>={Stealth[length=2mm]}, main node/.style={circle,draw,minimum size=0.6cm}]"
    if not directed:
        header = "[main node/.style={circle,draw,minimum size=0.6cm}]"
    lines = [f"\\begin{{tikzpicture}}{header}"]
    if title:
        lines.append(f"% {title}")
    for node, (x, y) in sorted(positions.items()):
        lines.append(f"  \\node[main node] ({node}) at ({x}, {y}) {{{node}}};")
    for u, v, w, style in edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        label_pos = angle_to_label(x2 - x1, y2 - y1)
        options = [style] if style else []
        draw_cmd = "\\draw[->" + ("," + ",".join(options) if options else "") + "]" if directed else "\\draw"
        if weighted and w is not None:
            lines.append(f"  {draw_cmd} ({u}) edge node[{label_pos}] {{{w}}} ({v});")
        elif directed:
            lines.append(f"  {draw_cmd} ({u}) edge ({v});")
        else:
            lines.append(f"  {draw_cmd} ({u}) -- ({v});")
    lines.append("\\end{tikzpicture}")
    return "\n".join(lines)


def render_flow_graph(
    positions: Dict[int, Tuple[float, float]],
    labels: Dict[int, str],
    edges: Sequence[Tuple[int, int, int]],
    title: Optional[str] = None,
) -> str:
    lines = ["\\begin{tikzpicture}[>={Stealth[length=2mm]}, main node/.style={circle,draw,minimum size=0.6cm}]"]
    if title:
        lines.append(f"% {title}")
    for node, (x, y) in sorted(positions.items()):
        lines.append(f"  \\node[main node] ({node}) at ({x}, {y}) {{{labels[node]}}};")
    for u, v, cap in edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        label_pos = angle_to_label(x2 - x1, y2 - y1)
        lines.append(f"  \\draw[->] ({u}) edge node[{label_pos}] {{{cap}}} ({v});")
    lines.append("\\end{tikzpicture}")
    return "\n".join(lines)
