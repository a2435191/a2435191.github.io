from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        cycle = 0
        register_x = 1
        
        screen = [['' for _ in range(40)] for _ in range(6)] 

        def increment_cycle() -> None:
            nonlocal cycle

            x_pos = cycle % 40
            y_pos = (cycle // 40) % 6

            if register_x - 1 <= x_pos <= register_x + 1:
                screen[y_pos][x_pos] = '#'
            else:
                screen[y_pos][x_pos] = '.'

            cycle += 1

        for instruction in inputs[0].splitlines():
            if instruction == 'noop':
                increment_cycle()
            elif instruction.startswith('addx'):
                increment_cycle()
                increment_cycle()

                increment = int(instruction.split(' ')[1])
                register_x += increment

        for line in screen:
            print(''.join(line))
        print()

        output = input("What are the eight capital letters? ").upper()

        return output

       
