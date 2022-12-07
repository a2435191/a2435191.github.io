from BaseSolution import BaseSolution
from typing import TypeVar
from .day07_common import *


class Solution(BaseSolution):

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        TOTAL_SPACE = 70_000_000
        NEEDED_SPACE = 30_000_000

        lines = inputs[0]

        tree = Node.from_lines(lines.splitlines())

        # calculate size of the outermost directory
        total_dir_size = 0

        def recurse_total_dir_size(tree: Node) -> int:
            nonlocal total_dir_size
            for child in tree.children:
                if isinstance(child, tuple):
                    total_dir_size += child[0]
                else:
                    recurse_total_dir_size(child)

        recurse_total_dir_size(tree)

        target_deletion_size = -(TOTAL_SPACE - total_dir_size - NEEDED_SPACE)
        deletion_size = float('inf')  # small as possible

        def recurse_deletion_size(tree: Node) -> int:
            nonlocal deletion_size
            this_size = 0

            for child in tree.children:
                if isinstance(child, tuple):
                    this_size += child[0]
                else:
                    this_size += recurse_deletion_size(child)

            if target_deletion_size <= this_size < deletion_size:
                deletion_size = this_size

            return this_size

        recurse_deletion_size(tree)

        return str(deletion_size)
