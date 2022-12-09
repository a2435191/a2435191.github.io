from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        head: tuple[int, int] = (0, 0)
        tail: tuple[int, int] = (0, 0)

        visited: set[tuple[int, int]] = {tail}

        for instruction in inputs[0].splitlines():
            direction = instruction.split(' ')[0]
            distance = int(instruction.split(' ')[1])

            if direction == 'L':
                head = (head[0] - distance, head[1])
            elif direction == 'R':
                head = (head[0] + distance, head[1])
            elif direction == 'U':
                head = (head[0], head[1] + distance)
            elif direction == 'D':
                head = (head[0], head[1] - distance)

            while abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:  # not touching
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1])
                if head[0] < tail[0]:
                    tail = (tail[0] - 1, tail[1])

                if head[1] > tail[1]:
                    tail = (tail[0], tail[1] + 1)
                if head[1] < tail[1]:
                    tail = (tail[0], tail[1] - 1)

                visited.add(tail)

        return str(len(visited))
