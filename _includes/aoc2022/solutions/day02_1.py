from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        total_score = 0
        for line in input.splitlines():
            opponent = ord(line[0]) - ord('A') # A, B, C
            mine     = ord(line[2]) - ord('X') # X, Y, Z

            strategy_score = mine + 1 # (0, 1, 2) -> (1, 2, 3)
            
            if mine == opponent:
                win_score = 3
            elif (mine == 0 and opponent == 2) \
                or (mine == 1 and opponent == 0) \
                or (mine == 2 and opponent == 1):
                win_score = 6
            else:
                win_score = 0

            total_score += strategy_score + win_score

        return total_score