from BaseSolution import BaseSolution
import re

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        N = 14
        data = inputs[0]
        for i in range(len(data) - N):
            substr = data[i:i+N]
            if len(set(substr)) == N:
                return str(i + N)
        raise