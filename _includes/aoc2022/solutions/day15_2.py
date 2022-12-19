import json
import re
from matplotlib import pyplot as plt

from BaseSolution import BaseSolution


def _remove_interval(intervals: list[range], to_remove: range):
    reduced_and_filtered = []
    for range_ in intervals:
        # range_ is fully to left of to_remove
        if range_.stop < to_remove.start:
            reduced_and_filtered.append(range_)
        # range_ is fully to right of to_remove
        elif range_.start > to_remove.stop:
            reduced_and_filtered.append(range_)
        # range_ is fully contained by to_remove
        else:
            new_range_left = range(range_.start, to_remove.start - 1)
            new_range_right = range(to_remove.stop + 1, range_.stop)

            if new_range_left.start <= new_range_left.stop:
                reduced_and_filtered.append(new_range_left)
            if new_range_right.start <= new_range_right.stop:
                reduced_and_filtered.append(new_range_right)

    return reduced_and_filtered


class Solution(BaseSolution):
    _INPUT_REGEX = re.compile(r'Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)')
    
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        SIZE = 4_000_000
    
        points: dict[int, list[range]] = {y: [range(SIZE)] for y in range(SIZE + 1)}
        
        for line in inputs[0].splitlines():
            sensor_x, sensor_y, closest_beacon_x, closest_beacon_y = \
                [int(n) for n in cls._INPUT_REGEX.match(line).groups()] 

            distance = abs(closest_beacon_y - sensor_y) + abs(closest_beacon_x - sensor_x)
        
            for y in range(max(sensor_y - distance, 0), min(sensor_y + distance + 1, SIZE)):
                distance_so_far = abs(y - sensor_y)
                distance_remaining = distance - distance_so_far

                no_points_x = range(sensor_x - distance_remaining, sensor_x + distance_remaining)
                points[y] = _remove_interval(points[y], no_points_x)
        
        for y, xs in points.items():
            if len(xs) == 1:
                tuning_frequency = xs[0].start * 4_000_000 + y
                return str(tuning_frequency)
                











            
