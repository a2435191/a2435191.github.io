# day11_common.py

from typing import Callable
from dataclasses import dataclass
import re
import operator


@dataclass
class Monkey:
    worries: list[int]
    operation: Callable[[int], int]

    test_divisor: int
    test_true: int
    test_false: int

    items_inspected: int = 0

    _OPERATION_REGEX = re.compile(r'Operation: new = old (.) (\d+|old)')
    _OPERATION_MAP = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    @staticmethod
    def from_string(s: str) -> 'Monkey':
        _, items_str, op_str, test_str, true_str, false_str = s.splitlines()
        worries = [int(n) for n in items_str.split(
            'Starting items: ')[1].split(', ')]

        # assuming operation is always a binary arithmetic operation and the first operand is always `old`
        binary_op_str, second_operand = Monkey._OPERATION_REGEX.search(
            op_str).groups()
        binary_op = Monkey._OPERATION_MAP[binary_op_str]
        if second_operand == 'old':
            def operation(n): return binary_op(n, n)
        else:
            def operation(n): return binary_op(n, int(second_operand))

        # assuming the test is always "divisble by {integer}"
        test_divisor = int(test_str.split('divisible by ')[1])
        test_true = int(true_str.split('throw to monkey ')[1])
        test_false = int(false_str.split('throw to monkey ')[1])

        return Monkey(worries, operation, test_divisor, test_true, test_false)
