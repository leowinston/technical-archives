"""(2,4) tree using the course's bottom-up insertion and deletion conventions."""

from __future__ import annotations

from typing import List


class BTreeNode:
    def __init__(self, leaf: bool = True) -> None:
        self.leaf = leaf
        self.keys: List[int] = []
        self.children: List["BTreeNode"] = []


class TwoFourTree:
    """A (2,4) tree implementing Barker's bottom-up conventions."""

    def __init__(self) -> None:
        self.root = BTreeNode(True)
        self.split_count = 0
        self.merge_count = 0
        self.borrow_count = 0

    def insert(self, key: int) -> None:
        # CHANGED: Delegate to a bottom-up recursive insertion instead of top-down
        promoted_key, new_right = self._insert_bottom_up(self.root, key)
        if promoted_key is not None:
            new_root = BTreeNode(False)
            new_root.keys = [promoted_key]
            new_root.children = [self.root, new_right]
            self.root = new_root

    def _insert_bottom_up(self, node: BTreeNode, key: int):
        idx = self._find_key(node, key)
        if idx < len(node.keys) and node.keys[idx] == key:
            return None, None # Ignore duplicates

        if node.leaf:
            node.keys.insert(idx, key)
        else:
            promoted_key, new_right = self._insert_bottom_up(node.children[idx], key)
            if promoted_key is not None:
                node.keys.insert(idx, promoted_key)
                node.children.insert(idx + 1, new_right)

        # CHANGED (Barker Convention): Bottom-up split only when node reaches 5-node (4 keys)
        if len(node.keys) == 4:
            self.split_count += 1
            # Keys: [A, B, C, D].
            # CHANGED (Convention 1): Promote right-middle -> index 2 (C)
            promoted = node.keys[2]

            new_sibling = BTreeNode(node.leaf)
            new_sibling.keys = [node.keys[3]] # Right child gets [D]

            node.keys = node.keys[:2] # Left child keeps [A, B]

            if not node.leaf:
                # 5 children total. Left keeps 3, Right gets 2.
                new_sibling.children = node.children[3:]
                node.children = node.children[:3]

            return promoted, new_sibling

        return None, None

    def delete(self, key: int) -> None:
        if not self.root.keys and self.root.leaf:
            return
        # CHANGED: Delegate to bottom-up recursive deletion
        self._delete_bottom_up(self.root, key)
        if not self.root.keys and not self.root.leaf:
            self.root = self.root.children[0]

    def _find_key(self, node: BTreeNode, key: int) -> int:
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < key:
            idx += 1
        return idx

    def _delete_bottom_up(self, node: BTreeNode, key: int) -> bool:
        # Returns True if the node underflowed (has 0 keys)
        idx = self._find_key(node, key)

        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                node.keys.pop(idx)
            else:
                # CHANGED (Convention 2): ALWAYS copy successor onto the node to be deleted
                succ = self._get_succ(node, idx)
                node.keys[idx] = succ
                # Recursively delete the successor from the right child subtree
                if self._delete_bottom_up(node.children[idx + 1], succ):
                    self._fix_underflow(node, idx + 1)
        else:
            if node.leaf:
                return False # Key not found
            # Go down to the appropriate child
            if self._delete_bottom_up(node.children[idx], key):
                self._fix_underflow(node, idx)

        return len(node.keys) < 1

    def _fix_underflow(self, node: BTreeNode, idx: int):
        # CHANGED (Convention 3): Look at right sibling first for borrowing
        if idx < len(node.keys) and len(node.children[idx + 1].keys) > 1:
            self._borrow_from_next(node, idx)
        elif idx > 0 and len(node.children[idx - 1].keys) > 1:
            self._borrow_from_prev(node, idx)
        else:
            # CHANGED (Convention 4): Standard merging logic
            if idx < len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _get_succ(self, node: BTreeNode, idx: int) -> int:
        current = node.children[idx + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    def _borrow_from_prev(self, node: BTreeNode, idx: int) -> None:
        self.borrow_count += 1
        child = node.children[idx]
        sibling = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node: BTreeNode, idx: int) -> None:
        self.borrow_count += 1
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node: BTreeNode, idx: int) -> None:
        self.merge_count += 1
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.children.pop(idx + 1)
