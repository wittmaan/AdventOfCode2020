import fileinput

import numpy as np


def detect_position(dat: str, max_position=127, lower_movement="F", higher_movement="B"):
    actual_limits = (0, max_position)

    for direction in dat:
        middle = (actual_limits[0] + actual_limits[1]) // 2

        if direction == lower_movement:
            actual_limits = (actual_limits[0], middle)
        if direction == higher_movement:
            actual_limits = (middle + 1, actual_limits[1])

    assert actual_limits[0] == actual_limits[1]
    return actual_limits[0]


sample_input = "FBFBBFFRLR"
row = detect_position(sample_input[:7])

columns = detect_position(sample_input[7:], max_position=7, lower_movement="L", higher_movement="R")


def calc_seat_id(dat: str):
    return detect_position(dat[:7]) * 8 + detect_position(
        dat[7:], max_position=7, lower_movement="L", higher_movement="R"
    )


day5_input = [_.strip() for _ in fileinput.input()]

seat_ids = [calc_seat_id(boarding_pass) for boarding_pass in day5_input]
solution_part1 = np.max(seat_ids)
assert solution_part1 == 842
print(f"solution part1: {solution_part1}")


# part 2

seat_ids.sort()

solution_part2 = None
for x in range(min(seat_ids), max(seat_ids)):
    if x not in seat_ids:
        solution_part2 = x

assert solution_part2 == 617
print(f"solution part2: {solution_part2}")
