import fileinput
from typing import List

# --- Day 13: Shuttle Search ---
# --- Part one ---

sample_input = """939
7,13,x,x,59,x,31,19""".split(
    "\n"
)


def find_earliest_bus(dat: List[str]) -> int:
    earliest_timestamp_departure = int(dat[0])
    bus_ids = [int(_) for _ in dat[1].split(",") if _ != "x"]
    print(f"earliest_timestamp_departure {earliest_timestamp_departure} bus_ids {bus_ids}")

    minimal_minutes = 100000
    minimal_bus_id = None
    for bus_id in bus_ids:
        bus_id_timestamp = 0

        while bus_id_timestamp < earliest_timestamp_departure:
            bus_id_timestamp += bus_id
            diff = bus_id_timestamp - earliest_timestamp_departure

            if 0 < diff < minimal_minutes:
                minimal_minutes = diff
                minimal_bus_id = bus_id

    print(f"minimal_minutes {minimal_minutes} minimal_bus_is {minimal_bus_id}")
    return minimal_minutes * minimal_bus_id


assert find_earliest_bus(sample_input) == 295

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = find_earliest_bus(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 104


# --- Part two ---

# @dataclass


def find_matching_order(dat: List[str]) -> int:
    bus_id_departures = [(int(val), idx) for idx, val in enumerate(dat[1].split(",")) if val != "x"]
    print(bus_id_departures)

    target_order = [_[0] for _ in bus_id_departures]
    print(target_order)

    actual_timestamps = dict.fromkeys(target_order, 0)
    print(actual_timestamps)

    for val in range(1000000):

        for bus_id in target_order:
            if val % bus_id == 0:
                actual_timestamps[bus_id] += bus_id

        tmp = [val % _ == 0 for _ in target_order]

        tmp2 = sorted(actual_timestamps.items(), key=lambda item: item[1])

        is_target_order_match = [_[0] for _ in tmp2] == target_order

        if val > 0 and tmp[0] is True and tmp[-1] is True and is_target_order_match:
            break

    print(tmp)
    print(val)
    print(actual_timestamps)

    # for _ in range(10):
    #     for bus_id, departure_minutes in bus_id_departures:
    #         actual_timestamps[bus_id] += departure_minutes
    #
    #     tmp = sorted(actual_timestamps.items(), key=lambda item: item[1])
    #     print(tmp)
    #
    # print(actual_timestamps)

    return 0


find_matching_order(sample_input)


# solution_part2 = detect_final_position_with_waypoint(build_instructions(puzzle_input))
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 24769
