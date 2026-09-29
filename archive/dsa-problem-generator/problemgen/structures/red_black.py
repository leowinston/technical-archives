"""CLRS-style red-black tree that counts rotations and recolorings."""

from __future__ import annotations

from typing import Optional


class RBNode:
    def __init__(self, key: Optional[int], color: str = "B") -> None:
        self.key = key
        self.color = color
        self.left: "RBNode"
        self.right: "RBNode"
        self.parent: "RBNode"


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None, "B")
        self.nil.left = self.nil.right = self.nil.parent = self.nil
        self.root = self.nil
        self.rotation_count = 0
        self.recolor_count = 0

    def _set_color(self, node: RBNode, color: str) -> None:
        if node is self.nil:
            return
        if node.color != color:
            node.color = color
            self.recolor_count += 1

    def left_rotate(self, x: RBNode) -> None:
        self.rotation_count += 1
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y: RBNode) -> None:
        self.rotation_count += 1
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.nil:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key: int) -> None:
        node = RBNode(key, "R")
        node.left = node.right = self.nil
        parent = self.nil
        current = self.root
        while current is not self.nil:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return
        node.parent = parent
        if parent is self.nil:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.insert_fixup(node)

    def insert_fixup(self, z: RBNode) -> None:
        while z.parent.color == "R":
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "R":
                    self._set_color(z.parent, "B")
                    self._set_color(y, "B")
                    self._set_color(z.parent.parent, "R")
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    self._set_color(z.parent, "B")
                    self._set_color(z.parent.parent, "R")
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "R":
                    self._set_color(z.parent, "B")
                    self._set_color(y, "B")
                    self._set_color(z.parent.parent, "R")
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    self._set_color(z.parent, "B")
                    self._set_color(z.parent.parent, "R")
                    self.left_rotate(z.parent.parent)
        self._set_color(self.root, "B")

    def transplant(self, u: RBNode, v: RBNode) -> None:
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node: RBNode) -> RBNode:
        current = node
        while current.left is not self.nil:
            current = current.left
        return current

    def search(self, key: int) -> RBNode:
        current = self.root
        while current is not self.nil and current.key != key:
            current = current.left if key < current.key else current.right
        return current

    def delete(self, key: int) -> None:
        z = self.search(key)
        if z is self.nil:
            return
        y = z
        y_original_color = y.color
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            if y.color != z.color:
                self._set_color(y, z.color)
        if y_original_color == "B":
            self.delete_fixup(x)
        if self.root is not self.nil:
            self._set_color(self.root, "B")

    def delete_fixup(self, x: RBNode) -> None:
        while x is not self.root and x.color == "B":
            if x is x.parent.left:
                w = x.parent.right
                if w.color == "R":
                    self._set_color(w, "B")
                    self._set_color(x.parent, "R")
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "B" and w.right.color == "B":
                    self._set_color(w, "R")
                    x = x.parent
                else:
                    if w.right.color == "B":
                        self._set_color(w.left, "B")
                        self._set_color(w, "R")
                        self.right_rotate(w)
                        w = x.parent.right
                    self._set_color(w, x.parent.color)
                    self._set_color(x.parent, "B")
                    self._set_color(w.right, "B")
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "R":
                    self._set_color(w, "B")
                    self._set_color(x.parent, "R")
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "B" and w.left.color == "B":
                    self._set_color(w, "R")
                    x = x.parent
                else:
                    if w.left.color == "B":
                        self._set_color(w.right, "B")
                        self._set_color(w, "R")
                        self.left_rotate(w)
                        w = x.parent.left
                    self._set_color(w, x.parent.color)
                    self._set_color(x.parent, "B")
                    self._set_color(w.left, "B")
                    self.right_rotate(x.parent)
                    x = self.root
        self._set_color(x, "B")
