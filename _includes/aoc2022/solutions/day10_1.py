from BaseSolution import BaseSolution


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        signal_strength_sum = 0
        cycle = 0
        register_x = 1

        def increment_cycle() -> None:
            nonlocal cycle, signal_strength_sum
            cycle += 1

            if cycle % 40 == 20:
                signal_strength_sum += cycle * register_x
                

        for instruction in inputs[0].splitlines():
            if instruction == 'noop':
                increment_cycle()
            elif instruction.startswith('addx'):
                increment_cycle()
                increment_cycle()

                increment = int(instruction.split(' ')[1])
                register_x += increment

        return str(signal_strength_sum)

       
