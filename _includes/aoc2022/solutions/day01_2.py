from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        calories = []
        for elf in input.split("\n\n"):
            total_calories = sum([int(cal) for cal in elf.splitlines()])
            calories.append(total_calories)
        
        top_three_calories_total = sum(sorted(calories, reverse=True)[:3])
        return str(top_three_calories_total)