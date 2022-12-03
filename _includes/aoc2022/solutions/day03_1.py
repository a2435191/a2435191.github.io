from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        total_priority = 0
        for line in input.splitlines():
            first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
            in_common = list(set.intersection(set(first_half), set(second_half)))[0]

            priority = ord(in_common)
            if ord('a') <= priority <= ord('z'):
                priority = priority - ord('a') + 1
            elif ord('A') <= priority <= ord('Z'):
                priority = priority - ord('A') + 27
            
            total_priority += priority

        return str(total_priority)