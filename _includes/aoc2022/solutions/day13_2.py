import json

from BaseSolution import BaseSolution
from .day13_common import packets_in_order


class Solution(BaseSolution):
    @staticmethod
    def _merge(left: list[list[list | int]], right: list[list[list | int]]) -> list[list[list | int]]:
        left_idx = 0
        right_idx = 0

        out: list[list[list | int]] = []
        while left_idx < len(left) and right_idx < len(right):
            left_value = left[left_idx]
            right_value = right[right_idx]
            if packets_in_order(left_value, right_value):  # left < right
                out.append(left_value)
                left_idx += 1
            else:
                out.append(right_value)
                right_idx += 1
        if left_idx == len(left):
            out += right[right_idx:]
        if right_idx == len(right):
            out += left[left_idx:]

        return out

    @staticmethod
    def _merge_sort(packets: list[list[list | int]]) -> list[list[list | int]]:
        if len(packets) == 1:
            return packets
        middle_idx = len(packets) // 2

        left_sorted = Solution._merge_sort(packets[:middle_idx])
        right_sorted = Solution._merge_sort(packets[middle_idx:])

        sorted_merged = Solution._merge(left_sorted, right_sorted)
        return sorted_merged

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        SPECIAL_PACKETS = ([[2]], [[6]])

        packets: list[list[list | int]] = list(SPECIAL_PACKETS)
        for packet_str in inputs[0].splitlines():
            if packet_str == '':
                continue
            packet: list[list | int] = json.loads(packet_str)
            packets.append(packet)

        sorted_ = Solution._merge_sort(packets)
        idx1 = sorted_.index(SPECIAL_PACKETS[0]) + 1
        idx2 = sorted_.index(SPECIAL_PACKETS[1]) + 1

        return str(idx1 * idx2)
