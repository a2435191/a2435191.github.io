import re

from BaseSolution import BaseSolution
from collections import defaultdict


class Solution(BaseSolution):
    _INPUT_REGEX = re.compile(
        r'Valve (.{2}) has flow rate=(\d+); tunnels? leads? to (?:valves (.+)|valve (.+))')

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        TIME = 30
        START = "AA"

        valves: dict[str, tuple[int, set[str]]] = {}

        for line in inputs[0].splitlines():
            valve_name, flow_rate_str, neighbors_str, neighbor_str = cls._INPUT_REGEX.match(
                line).groups()

            flow_rate = int(flow_rate_str)
            neighbors = set((neighbors_str or neighbor_str).split(', '))

            valves[valve_name] = (flow_rate, neighbors)

        nonzero_rate_valves = {valve for valve,
                             (rate, _) in valves.items() if rate != 0}

        # DFS
        max_pressure: int = 0

        max_pressure_cache_so_far: dict[tuple[tuple[str, ...], str, int], int] = {
        }

        def search(already_on: set[str], current: str, this_path_score_so_far: int, minutes_taken_so_far: int):
            nonlocal max_pressure

            # first check if we're out of time or if all the valuable valves are turned on
            if minutes_taken_so_far == TIME or already_on == nonzero_rate_valves:
                max_pressure = max(max_pressure, this_path_score_so_far)

                return

            # Optimization 1: if the current state of valve positions, location, and time is suboptimal
            # (i.e. the same state tuple has previously led to a higher score), abort
            key = (tuple(sorted(already_on)), current, minutes_taken_so_far)
            prev_record_for_this_state = max_pressure_cache_so_far.get(key, -1)
            if this_path_score_so_far <= prev_record_for_this_state:
                return
            max_pressure_cache_so_far[key] = this_path_score_so_far

            # Optimization 2: more complicated elimination heuristic
            # maximum possible score can be reached by hitting remaining
            # nodes in decreasing rate order. If this maximum attainable score
            # is less than the current maximum, abort.

            sorted_rates = sorted(
                [valves[remaining][0] for remaining in nonzero_rate_valves.difference(already_on)], reverse=True)

            maximum_change_in_score: int = 0
            score_change_time: int = minutes_taken_so_far

            for rate in sorted_rates:
                maximum_change_in_score += (TIME -
                                            score_change_time - 1) * rate

                score_change_time += 1
                if score_change_time == TIME:
                    break

            if this_path_score_so_far + maximum_change_in_score <= max_pressure:
                return

            this_rate, neighbors = valves[current]

            # either turn on this valve (and possibly hit neighbors later)
            # or move on to neighbor

            if this_rate != 0 and current not in already_on:
                search(
                    already_on | {current},
                    current,
                    this_path_score_so_far +
                    (TIME - minutes_taken_so_far - 1) * this_rate,
                    minutes_taken_so_far + 1
                )

            for neighbor in neighbors:
                search(
                    already_on,
                    neighbor,
                    this_path_score_so_far,
                    minutes_taken_so_far + 1
                )

        search(set(), START, 0, 0)

        return str(max_pressure)
