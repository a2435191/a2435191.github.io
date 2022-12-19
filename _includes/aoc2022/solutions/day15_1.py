import json
import re

from BaseSolution import BaseSolution


class Solution(BaseSolution):
    _INPUT_REGEX = re.compile(r'Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)')
    @classmethod
    def solve(cls, inputs: list[str]) -> str:
        ROW = 2_000_000

        no_beacon_locations: list[range] = []

        # parse input
        for line in inputs[0].splitlines():
            sensor_x, sensor_y, closest_beacon_x, closest_beacon_y = \
                [int(n) for n in cls._INPUT_REGEX.match(line).groups()]

            # Manhattan distance— no beacons will be closer than this
            nearest_beacon_distance = abs(closest_beacon_x - sensor_x) + abs(closest_beacon_y - sensor_y) 
            # compute which beacons with `y == ROW` have this distance or less
            """ 
            Say `nearest_beacon_distance = 12` with the the sensor and row as shown (sensor is 7 units away).
            Then part of row that is guaranteed to not have beacons is the sensor x coordinate ± (12 - 7 - 1)
            x x x x x x[x x x x x x x x x x x]x x x x x x x x x x x   <- y == ROW
                                  |          ^- guaranteed to not have beacons in this 
                                  |             (inclusive) range at `y == ROW`
                                  |
                                  |  <- distance to row
                                  |
                                  |
                                  x  <- sensor
            """

            distance_to_row = abs(ROW - sensor_y)

            if distance_to_row > nearest_beacon_distance:
                continue

            no_beacons_range = range(
                sensor_x - (nearest_beacon_distance - distance_to_row),
                sensor_x + (nearest_beacon_distance - distance_to_row)
                # range is right-exclusive, but that's fine— we're only using it as a struct here
            )

            # special case: if beacon has y-coordinate `ROW`, 
            # then obviously it's not a beaconless location
            if closest_beacon_y == ROW:
                left_range = range(no_beacons_range.start, closest_beacon_x - 1) 
                right_range = range(closest_beacon_x + 1, no_beacons_range.stop)

                # must account for corner cases with the beacon being at the end of the range, too
                # this causes left_range or right_range to get "out of order," so we check for that
                if left_range.start <= left_range.stop:
                    no_beacon_locations.append(left_range)
                if right_range.start <= right_range.stop:
                    no_beacon_locations.append(right_range)
            else:
                no_beacon_locations.append(no_beacons_range)


        
        # merge overlapping intervals
        # sort by start value— then mergeable ranges will appear as a block
        no_beacon_locations.sort(key=lambda range_: range_.start)

        no_beacon_locations_reduced: list[range] = []

        for range_ in no_beacon_locations:
            prev = no_beacon_locations_reduced[-1] if no_beacon_locations_reduced else None

            # no overlap
            if prev is None or prev.stop < range_.start:
                no_beacon_locations_reduced.append(range_)
            else: # otherwise combine
                new_stop = max(
                    no_beacon_locations_reduced[-1].stop, 
                    range_.stop
                )
                no_beacon_locations_reduced[-1] = range(no_beacon_locations_reduced[-1].start, new_stop)
        

        no_beacon_locations_count = sum([range_.stop - range_.start + 1 
            for range_ in no_beacon_locations_reduced])


        return str(no_beacon_locations_count)

            
