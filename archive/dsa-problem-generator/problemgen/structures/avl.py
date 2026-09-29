"""AVL tree that counts the rotations it performs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class AVLNode:
    key: int
    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    height: int = 1


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None
        self.rotation_count = 0

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update(self, node: AVLNode) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _right_rotate(self, y: AVLNode) -> AVLNode:
        self.rotation_count += 1
        x = y.left
        assert x is not None
        t2 = x.right
        x.right = y
        y.left = t2
        self._update(y)
        self._update(x)
        return x

    def _left_rotate(self, x: AVLNode) -> AVLNode:
        self.rotation_count += 1
        y = x.right
        assert y is not None
        t2 = y.left
        y.left = x
        x.right = t2
        self._update(x)
        self._update(y)
        return y

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        self._update(node)
        balance = self._balance(node)
        if balance > 1 and key < node.left.key:  # type: ignore[union-attr]
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:  # type: ignore[union-attr]
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:  # type: ignore[union-attr]
            node.left = self._left_rotate(node.left)  # type: ignore[arg-type]
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:  # type: ignore[union-attr]
            node.right = self._right_rotate(node.right)  # type: ignore[arg-type]
            return self._left_rotate(node)
        return node

    def _min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        self._update(node)
        balance = self._balance(node)
        if balance > 1 and self._balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._left_rotate(node.left)  # type: ignore[arg-type]
            return self._right_rotate(node)
        if balance < -1 and self._balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._right_rotate(node.right)  # type: ignore[arg-type]
            return self._left_rotate(node)
        return node
