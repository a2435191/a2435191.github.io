from BaseSolution import BaseSolution

class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        input = inputs[0]
        
        overlapping_count = 0
        for line in input.splitlines():
            range1, range2 = line.split(",")

            left1, right1 = [int(n) for n in range1.split("-")]
            left2, right2 = [int(n) for n in range2.split("-")]

            if left2 <= right1 <= right2 or left2 <= left1 <= right2\
                or left1 <= right2 <= right1 or left1 <= left2 <= right1:
                overlapping_count += 1
            
        return str(overlapping_count)