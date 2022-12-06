from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        data = inputs[0]
        for i in range(len(data) - 4):
            substr = data[i:i+4]
            if len(set(substr)) == 4:
                return str(i + 3 + 1) # + 3 to move to end of substring, + 1 to make 1-indexed
        raise