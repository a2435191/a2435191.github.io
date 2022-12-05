from BaseSolution import BaseSolution
import re

class Solution(BaseSolution):
    @staticmethod
    def _extract_initial_state(lines: list[str]) -> list[list[str]]:
        width = len(lines[-1].replace(" ", ""))
        stacks = [[] for _ in range(width)]

        lines = list(reversed(lines[:-1]))

        for col in range(width):
            x = col * 4 + 1
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

            start -= 1
            end -= 1

            to_move = state[start][-quantity:]
            state[start] = state[start][:-quantity]
            # tail end of `start` column is now at TAIL end of `end` column— no reverse needed
            state[end].extend(to_move)

        top_of_stack = ''.join([col[-1] if col != [] else '' for col in state])
        return top_of_stack