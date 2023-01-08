# day17_common.py

from BaseSolution import BaseSolution

ROCK_SHAPES: tuple[tuple[str]] = (
    ("####",),
    (".#.",
     "###",
     ".#."),
    ("..#",
     "..#",
     "###"),
    ("#",
     "#",
     "#",
     "#"),
    ("##",
     "##")
)

def print_rocks(rocks: list[list[str]]) -> None:
    width = len(rocks[0])
    for row in reversed(rocks[1:]): # print the rock formation
        print('|' + ''.join(row) + '|')
    print('+' + '-' * width + '+')


def calculate_height(floor: list[list[str]], width: int, num_rocks: int, jets: str, jet_pointer: int) -> tuple[list[list[str]], int]:
    rocks = [list(row) for row in floor]
    
    def can_move_horizontally(rock: tuple[str], bottom_left_pos: tuple[int, int], left: bool) -> bool:
        left_side_x, bottom_y = bottom_left_pos
        if left and left_side_x == 0:  # hits left wall
            return False

        # hits right wall
        if not left and left_side_x + len(rock[0]) == width:
            return False

        for y, row in enumerate(reversed(rock)):
            height = bottom_y + y
            if height < len(rocks):  # don't go over top
                for x, char in enumerate(row):
                    possible_collision_x = left_side_x + x - 1 if left else left_side_x + x + 1
                    if char == '#' and rocks[height][possible_collision_x] == '#':
                        return False
        return True

    def can_fall(rock: tuple[str], bottom_left_pos: tuple[int, int]) -> bool:
        left_side_x, bottom_y = bottom_left_pos

        if bottom_y == 1:  # hits floor
            return False

        for y, row in enumerate(reversed(rock)):
            height = bottom_y + y
            if height - 1 < len(rocks):  # don't go over top
                for x, char in enumerate(row):
                    if char == '#' and rocks[height - 1][left_side_x + x] == '#':
                        return False
        return True

    for idx in range(num_rocks):
        rock = ROCK_SHAPES[idx % len(ROCK_SHAPES)]
        bottom_left_pos = [2, len(rocks) + 3]

        while True:
            jet = jets[jet_pointer]

            # first, gas pushes rock
            if jet == '<' and can_move_horizontally(rock, tuple(bottom_left_pos), True):
                bottom_left_pos[0] -= 1
            elif jet == '>' and can_move_horizontally(rock, tuple(bottom_left_pos), False):
                bottom_left_pos[0] += 1

            # then rock falls. if rock comes to rest, move to next rock
            if can_fall(rock, tuple(bottom_left_pos)):
                bottom_left_pos[1] -= 1
            else:
                jet_pointer = (jet_pointer + 1) % len(jets)
                break

            jet_pointer = (jet_pointer + 1) % len(jets)

        rock_top = bottom_left_pos[1] + len(rock)
        for _ in range(rock_top - len(rocks)):
            rocks.append(['.'] * width)

        for y, row in enumerate(reversed(rock)):
            height = bottom_left_pos[1] + y
            for x, char in enumerate(row):
                if char == '#':
                    rocks[height][x + bottom_left_pos[0]] = '#'


    return rocks, jet_pointer
