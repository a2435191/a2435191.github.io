from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @staticmethod
    def _parse_input(lines: list[str]) -> list[list[int]]:
        return [[int(n) for n in line] for line in lines]

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        heights = Solution._parse_input(inputs[0].splitlines())

        array_width = len(heights[0])
        array_height = len(heights)

        visible: set[tuple[int, int]] = set()

        for i, row in enumerate(heights):
            # visible from the left
            max_height_so_far = -1
            for j, height in enumerate(row):
                if height > max_height_so_far:
                    visible.add((i, j))
                max_height_so_far = max(max_height_so_far, height)
            
            # visible from the right
            max_height_so_far = -1
            for j, height in reversed(list(enumerate(row))):
                if height > max_height_so_far:
                    visible.add((i, j))
                max_height_so_far = max(max_height_so_far, height)

        for j in range(array_width):
            # visible from the top
            max_height_so_far = -1
            for i in range(array_height):
                height = heights[i][j]
                if height > max_height_so_far:
                    visible.add((i, j))
                max_height_so_far = max(max_height_so_far, height)

            # visible from the bottom
            max_height_so_far = -1
            for i in reversed(range(array_height)):
                height = heights[i][j]
                if height > max_height_so_far:
                    visible.add((i, j))
                max_height_so_far = max(max_height_so_far, height)

        return str(len(visible))