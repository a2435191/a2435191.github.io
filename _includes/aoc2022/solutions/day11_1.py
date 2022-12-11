from BaseSolution import BaseSolution
from .day11_common import Monkey


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        ROUNDS = 20
        monkeys = [Monkey.from_string(chunk)
                   for chunk in inputs[0].split('\n\n')]

        for _ in range(ROUNDS):
            for monkey in monkeys:
                worries_copy = list(monkey.worries)
                monkey.worries = []
                for worry in worries_copy:
                    monkey.items_inspected += 1

                    updated_worry = monkey.operation(worry)
                    updated_worry //= 3

                    if updated_worry % monkey.test_divisor == 0:
                        index = monkey.test_true
                    else:
                        index = monkey.test_false

                    monkeys[index].worries.append(updated_worry)

        items_inspected_sorted = sorted(
            [m.items_inspected for m in monkeys], reverse=True)

        monkey_business = items_inspected_sorted[0] * items_inspected_sorted[1]
        return str(monkey_business)
