from BaseSolution import BaseSolution
from .day17_common import ROCK_SHAPES, calculate_height, print_rocks
from math import lcm

class Solution(BaseSolution):

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        WIDTH = 7
        NUM_ROCKS = 2022#1_000_000_000_000
        
        jets = inputs[0]


