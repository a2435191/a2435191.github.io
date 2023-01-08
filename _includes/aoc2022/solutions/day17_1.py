from BaseSolution import BaseSolution
from .day17_common import calculate_height

class Solution(BaseSolution):

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        WIDTH = 7
        NUM_ROCKS = 2022

        # stores state: 0th row is floor, last row is top of rock structure (to make appending fast)
        floor = [["#"] * WIDTH]

        jets: str = inputs[0]
        
        rocks, _ = calculate_height(floor, WIDTH, NUM_ROCKS, jets, 0)

        # -1 because one row is the floor, which we don't count
        return str(len(rocks) - 1)
