import json

from BaseSolution import BaseSolution

from .day14_common import parse_input


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        SAND_START = (500, 0)

        rocks = parse_input(inputs[0].splitlines())

        # map of the HIGHEST y for each x
        lowest_height_map: dict[int, int] = {}
        for x, y in rocks:
            lowest_height_map[x] = max(
                y, lowest_height_map.get(x, float('-inf')))

        floor_height = max(lowest_height_map.values()) + 2

        all_sand: set[tuple[int, int]] = set()

        while True:  # one grain of sand moves per cycle of outer loop
            sand = SAND_START
            while True:  # one grain of sand moves one pixel per cycle of inner loop
                if sand[1] + 1 == floor_height:  # on top of floor
                    break

                below = (sand[0], sand[1] + 1)
                if below not in all_sand and below not in rocks:
                    sand = below
                    continue

                down_left = (sand[0] - 1, sand[1] + 1)
                if down_left not in all_sand and down_left not in rocks:
                    sand = down_left
                    continue

                down_right = (sand[0] + 1, sand[1] + 1)
                if down_right not in all_sand and down_right not in rocks:
                    sand = down_right
                    continue

                break

            all_sand.add(sand)

            if sand == SAND_START:
                return str(len(all_sand))
