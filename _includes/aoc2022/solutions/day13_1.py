import json

from BaseSolution import BaseSolution
from .day13_common import packets_in_order


class Solution(BaseSolution):
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        in_order_packets_index_sum = 0
        for i, pair_str in enumerate(inputs[0].split('\n\n')):
            packet_str_1, packet_str_2 = pair_str.splitlines()

            left:  list[list | int] = json.loads(packet_str_1)
            right: list[list | int] = json.loads(packet_str_2)

            in_order = packets_in_order(left, right)
            assert in_order is not None, str(i + 1)

            if in_order:
                in_order_packets_index_sum += i + 1  # 1-based indexing

        return str(in_order_packets_index_sum)
