from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        N_LINKS = 10
        links = [(0, 0) for _ in range(N_LINKS)]  # head at start, tail at end

        visited: set[tuple[int, int]] = {links[-1]}
        for instruction in inputs[0].splitlines():
            direction = instruction.split(' ')[0]
            distance = int(instruction.split(' ')[1])

            # update head as before, but this time update all links once per timestep
            if direction == 'L':
                delta = (-1, 0)
            elif direction == 'R':
                delta = (1, 0)
            elif direction == 'U':
                delta = (0, 1)
            elif direction == 'D':
                delta = (0, -1)

            # move head one step at a time, propagating changes through links
            for step in range(distance):
                links[0] = (links[0][0] + delta[0], links[0][1] + delta[1])
                for i, link in list(enumerate(links))[1:]:
                    next_link = links[i - 1]

                    # same rules as before, now link-wise
                    while abs(link[0] - next_link[0]) > 1 or abs(link[1] - next_link[1]) > 1:
                        if next_link[0] > link[0]:
                            link = (link[0] + 1, link[1])
                        if next_link[0] < link[0]:
                            link = (link[0] - 1, link[1])

                        if next_link[1] > link[1]:
                            link = (link[0], link[1] + 1)
                        if next_link[1] < link[1]:
                            link = (link[0], link[1] - 1)

                        links[i] = link

                        # add tail to set
                        if i == N_LINKS - 1:
                            visited.add(link)

        return str(len(visited))
