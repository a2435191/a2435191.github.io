from BaseSolution import BaseSolution
from .day07_common import *


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        MAX_SIZE = 100_000
        lines = inputs[0]

        tree = Node.from_lines(lines.splitlines())

        total_directory_sizes = 0

        def recurse(tree: Node) -> int:
            # returns total size of only this `tree` variable, stored in `this_size`

            nonlocal total_directory_sizes
            this_size = 0

            for child in tree.children:
                if isinstance(child, tuple):  # leaf node
                    this_size += child[0]
                else:
                    this_size += recurse(child)

            if this_size <= MAX_SIZE:
                total_directory_sizes += this_size

            return this_size

        recurse(tree)

        return str(total_directory_sizes)
