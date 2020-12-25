import fileinput
from functools import reduce
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
    # print(f"earliest_timestamp_departure {earliest_timestamp_departure} bus_ids {bus_ids}")

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

    # print(f"minimal_minutes {minimal_minutes} minimal_bus_id {minimal_bus_id}")
    return minimal_minutes * minimal_bus_id


assert find_earliest_bus(sample_input) == 295

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = find_earliest_bus(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 104


# --- Part two ---

# we need
# (t + 0) % 7 == 0
# (t + 1) % 13 == 0
# (t + 4) % 59 == 0
# (t + 6) % 31 == 0
# (t + 7) % 19 == 0
#
# therefore
# t % 7 == (7 - 0) % 7     -> t % 7 == 0
# t % 13 == (13 - 1) % 13  -> t % 13 == 12
# t % 59 == (59 - 4) % 59  -> t % 59 == 55
# t % 31 == (31 - 6) % 36  -> t % 31 == 25
# t % 19 == (19 - 7) % 19  -> t % 19 == 12

# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def find_matching_order(dat: List[str]) -> int:
    mods, remainders = zip(
        *[(int(val), int(val) - idx % int(val)) for idx, val in enumerate(dat[1].split(",")) if val != "x"]
    )
    # print(f"mods={mods}, remainders={remainders}")

    return chinese_remainder(n=mods, a=remainders)


assert find_matching_order(sample_input) == 1068781

solution_part2 = find_matching_order(puzzle_input)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 842186186521918
