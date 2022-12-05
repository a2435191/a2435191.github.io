from BaseSolution import BaseSolution
import re

class Solution(BaseSolution):
    @staticmethod
    def _extract_initial_state(lines: list[str]) -> list[list[str]]:
        width = len(lines[-1].replace(" ", "")) # number of stacks, between 1 and 9
        stacks = [[] for _ in range(width)]

        lines = list(reversed(lines[:-1])) # remove last line— only column numbers

        for col in range(width):
            x = col * 4 + 1 # each `[A] ` is four characters
            for line in lines:
                char = line[x]
                if char != ' ':
                    stacks[col].append(char)

        return stacks


    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        pattern = re.compile(r"move (\d+) from (\d) to (\d)")

        initial_state_str, steps = inputs[0].split("\n\n")
        state = Solution._extract_initial_state(initial_state_str.splitlines())

        for step in steps.splitlines():
            quantity, start, end = (int(n) for n in pattern.match(step).groups())

            start -= 1 # zero-index
            end -= 1

            to_move = state[start][-quantity:] # last `quantity` crates from the `start` column
            state[start] = state[start][:-quantity]
            to_move.reverse() # tail end of `start` column is at front end of `end` column
            state[end].extend(to_move)

        # not sure what happens if a column is empty— just in case
        top_of_stack = ''.join([col[-1] if col != [] else '' for col in state])
        return top_of_stack