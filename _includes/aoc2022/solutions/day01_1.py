from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        max_calories = 0
        for elf in input.split("\n\n"):
            total_calories = sum([int(cal) for cal in elf.splitlines()])
            max_calories = max(max_calories, total_calories)
        
        return str(max_calories)