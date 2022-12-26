import re

import random
from collections import defaultdict
from BaseSolution import BaseSolution


class Solution(BaseSolution):
    _INPUT_REGEX = re.compile(
        r'Valve (.{2}) has flow rate=(\d+); tunnels? leads? to (?:valves (.+)|valve (.+))')

    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        TIME = 26
        START = "AA"

        valves: dict[str, tuple[int, set[str]]] = {}

        for line in inputs[0].splitlines():
            valve_name, flow_rate_str, neighbors_str, neighbor_str = cls._INPUT_REGEX.match(
                line).groups()

            flow_rate = int(flow_rate_str)
            neighbors = set((neighbors_str or neighbor_str).split(', '))

            valves[valve_name] = (flow_rate, neighbors)

        for valve, (_, neighbors) in valves.items():
            for neighbor in neighbors:
                assert valve in valves[neighbor][1], (valve, neighbor)

        nonzero_rate_valves = {valve for valve,
                             (rate, _) in valves.items() if rate != 0}

        max_pressure: int = 0

        max_pressure_cache_so_far: dict[tuple[tuple[str, ...], str, str, int], int] = {
        }

        def search(
            already_on: set[str],
            current_me: str, current_elephant: str,
            this_path_score_so_far: int,
            minutes_taken_so_far: int
        ):
            nonlocal max_pressure

            if minutes_taken_so_far == TIME or already_on == nonzero_rate_valves:
                max_pressure = max(max_pressure, this_path_score_so_far)
                return

            # Optimization 1 (this time standardizing keys by lexicographic order)
            if current_me < current_elephant:
                key = (tuple(sorted(already_on)), current_me,
                       current_elephant, minutes_taken_so_far)
            else:
                key = (tuple(sorted(already_on)), current_elephant,
                       current_me, minutes_taken_so_far)

            prev_record_for_this_state = max_pressure_cache_so_far.get(key, -1)
            if this_path_score_so_far <= prev_record_for_this_state:
                return
            max_pressure_cache_so_far[key] = this_path_score_so_far

            # Optimization 2, but taking rates two at a time

            maximum_change_in_score: int = 0

            score_change_time = minutes_taken_so_far

            sorted_rates = sorted(
                [valves[remaining][0] for remaining in nonzero_rate_valves.difference(already_on)], reverse=True)

            for i in range(0, len(sorted_rates), 2):
                rate1 = sorted_rates[i]
                try:
                    rate2 = sorted_rates[i + 1]
                except IndexError:
                    rate2 = 0

                maximum_change_in_score += (TIME -
                                            score_change_time - 1) * (rate1 + rate2)

                score_change_time += 1
                if score_change_time == TIME:
                    break

            if this_path_score_so_far + maximum_change_in_score <= max_pressure:
                return

            my_rate, my_neighbors = valves[current_me]
            elephant_rate, elephant_neighbors = valves[current_elephant]

            if my_rate != 0 and current_me not in already_on:

                # flip on with me and flip on with the elephant in different places
                if (elephant_rate != 0) and (current_elephant not in already_on) and (current_me != current_elephant):
                    search(
                        already_on | {current_me, current_elephant},
                        current_me, current_elephant,
                        this_path_score_so_far +
                        (TIME - minutes_taken_so_far - 1) *
                        (my_rate + elephant_rate),
                        minutes_taken_so_far + 1
                    )

                # if in the same place or already had elephant turn on switch, elephant must move, but I flip switch
                for elephant_neighbor in elephant_neighbors:
                    search(
                        already_on | {current_me},
                        current_me, elephant_neighbor,
                        this_path_score_so_far +
                        (TIME - minutes_taken_so_far - 1) * my_rate,
                        minutes_taken_so_far + 1
                    )

            # or I move and the elephant flips the switch
            if elephant_rate != 0 and current_elephant not in already_on:

                for my_neighbor in my_neighbors:
                    search(
                        already_on | {current_elephant},
                        my_neighbor, current_elephant,
                        this_path_score_so_far +
                        (TIME - minutes_taken_so_far - 1) * elephant_rate,
                        minutes_taken_so_far + 1
                    )

            # both move
            for elephant_neighbor in elephant_neighbors:
                for my_neighbor in my_neighbors:
                    # this check is tricky:
                    # if both me and elephant originate from the same node, we don't want to have
                    # me check neighbor1 and elephant check neighbor2 AND me check neighbor2 and elephant check neighbor1
                    # use lexicographic ordering of the neighbor strings to avoid this
                    if current_me == current_elephant and elephant_neighbor <= my_neighbor:
                        continue

                    search(
                        already_on,
                        my_neighbor, elephant_neighbor,
                        this_path_score_so_far,
                        minutes_taken_so_far + 1
                    )

        search(set(), START, START, 0, 0)

        return str(max_pressure)
