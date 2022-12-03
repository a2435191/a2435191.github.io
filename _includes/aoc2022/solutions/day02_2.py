from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        total_score = 0
        for line in input.splitlines():
            opponent = ord(line[0]) - ord('A') # A, B, C
            outcome  = ord(line[2]) - ord('X') # X, Y, Z

            win_score = outcome * 3 # (0, 1, 2) -> (0, 3, 6)

            if outcome == 1: # draw
                strategy = opponent
            elif outcome == 2: # win
                strategy = (opponent + 1) % 3 # shift (rock, paper, scissors) right by 1
            else: # loss
                strategy = (opponent + 2) % 3 # shift left by 1

            strategy_score = strategy + 1 # (0, 1, 2) -> (1, 2, 3)

            total_score += win_score + strategy_score

        return str(total_score)