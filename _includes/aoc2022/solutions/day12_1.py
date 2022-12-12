from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        # parse input
        input = inputs[0]
        start: tuple[int, int]
        end: tuple[int, int]

        grid: list[list[int]] = []

        for y, line in enumerate(input.splitlines()):

            row: list[int] = []
            # start has elevation a, end has elevation z
            for x, c in enumerate(line):
                if c == 'S':
                    c = 'a'
                    start = (x, y)
                elif c == 'E':
                    c = 'z'
                    end = (x, y)

                row.append(ord(c) - ord('a'))

            grid.append(row)

        # Dijkstra's algorithm
        unvisited: set[tuple[int, int]] = {
            (x, y) for x, _ in enumerate(row)
            for y, row in enumerate(grid)
        }

        tentative_distances = [[float('inf') for _ in row] for row in grid]
        tentative_distances[start[1]][start[0]] = 0

        current = start
        while True:

            current_x, current_y = current
            current_distance = tentative_distances[current_y][current_x]

            for neighbor_x, neighbor_y in (
                (current_x + 1, current_y),
                (current_x - 1, current_y),
                (current_x, current_y + 1),
                    (current_x, current_y - 1)):

                if (neighbor_x, neighbor_y) not in unvisited:
                    continue

                try:
                    if neighbor_x < 0 or neighbor_y < 0:
                        raise IndexError
                    if grid[neighbor_y][neighbor_x] - grid[current_y][current_x] > 1:
                        neighbor_distance = float('inf')
                    else:
                        neighbor_distance = current_distance + 1
                except IndexError:
                    continue

                if tentative_distances[neighbor_y][neighbor_x] > neighbor_distance:
                    tentative_distances[neighbor_y][neighbor_x] = neighbor_distance

            unvisited.remove(current)
            if current == end:
                return str(current_distance)

            current = min(
                unvisited, key=lambda coord: tentative_distances[coord[1]][coord[0]])
