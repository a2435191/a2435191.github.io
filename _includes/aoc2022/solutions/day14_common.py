# day14_common.py

from BaseSolution import BaseSolution


def parse_input(lines: list[str]) -> set[tuple[int, int]]:
    out: set[tuple[int, int]] = set()

    for structure in lines:
        # initialize these in loop
        prev_x: int | None = None
        prev_y: int | None = None

        for vertex_str in structure.split(' -> '):
            new_x_str, new_y_str = vertex_str.split(',')
            new_x = int(new_x_str)
            new_y = int(new_y_str)

            if prev_x is not None and prev_y is not None:
                if new_x == prev_x:  # vertical
                    for y in range(min(prev_y, new_y), max(prev_y, new_y) + 1):
                        out.add((new_x, y))
                if new_y == prev_y:  # horizontal
                    for x in range(min(prev_x, new_x), max(prev_x, new_x) + 1):
                        out.add((x, new_y))

            prev_x = new_x
            prev_y = new_y

    return out
