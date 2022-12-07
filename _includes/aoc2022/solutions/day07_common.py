# day07_common.py

from typing import TypeVar

Node = TypeVar("Node")  # just so type hints work


class Node:
    def __init__(self,
                 children: set[tuple[int, str] | Node],
                 dirname: str | None,
                 parent: Node | None
                 ):
        self.children = children
        self.dirname = dirname
        self.parent = parent

    @staticmethod
    def from_lines(lines: list[str]) -> Node:
        tree: Node | None = None  # initialized later in loop
        current_node: Node | None = None

        for line in lines:
            if line.startswith("$ cd"):
                dirname = line.split("$ cd ")[1]
                if tree is None:
                    tree = Node(set(), dirname, None)
                    current_node = tree
                    continue

                if dirname == "..":
                    current_node = current_node.parent
                else:
                    child = Node(set(), dirname, current_node)
                    current_node.children.add(child)
                    current_node = child
            elif line.startswith("$ ls"):
                pass
            elif line.startswith("dir"):
                pass
            else:  # file
                filelength_str, filename = line.split(" ")
                current_node.children.add((int(filelength_str), filename))

        return tree
