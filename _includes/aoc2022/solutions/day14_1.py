import json

from BaseSolution import BaseSolution

from .day14_common import parse_input


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        SAND_START = (500, 0)

        rocks = parse_input(inputs[0].splitlines())

        # map of the LARGEST y for each x
        lowest_height_map: dict[int, int] = {}
        for x, y in rocks:
            lowest_height_map[x] = max(
                y, lowest_height_map.get(x, float('-inf')))

        all_sand: set[tuple[int, int]] = set()

        while True:  # one grain of sand moves per cycle of outer loop
            sand = SAND_START
            while True:  # one grain of sand moves one pixel per cycle of inner loop

                # check if sand is lower down than the lowest (largest) rock y coordinate—
                # if so, we've reached the end
                if lowest_height_map.get(sand[0], float('-inf')) < sand[1]:
                    return str(len(all_sand))

                is_stopped = True
                potential_y = sand[1] + 1

                # try moving straight down, down left, then down right
                for potential_x_delta in (0, -1, 1):
                    potential_move = (sand[0] + potential_x_delta, potential_y)

                    if potential_move not in all_sand and potential_move not in rocks:
                        sand = potential_move
                        is_stopped = False
                        break

                if is_stopped:
                    break

            all_sand.add(sand)
