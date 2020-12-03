import fileinput
from typing import List

import numpy as np


# --- Day 1: Report Repair ---
# --- Part one ---


def get_matching_product_result(dat: List[int]):
    product_result = np.outer(a=dat, b=dat)
    sum_result = np.add.outer(dat, dat)

    ind_match = np.where(sum_result == 2020)
    return np.unique(product_result[ind_match]).tolist()[0]


sample_input = [1721, 979, 366, 299, 675, 1456]
assert get_matching_product_result(sample_input) == 514579

day1_input = [int(_.strip()) for _ in fileinput.input()]
solution_part1 = get_matching_product_result(day1_input)

assert solution_part1 == 326211
print(f"solution part1: {solution_part1}")


# --- Part two ---


def get_three_way_product_result(dat: List[int]):
    for idx1, val1 in enumerate(dat):
        for idx2, val2 in enumerate(dat):
            if val1 == val2:
                continue

            for idx3, val3 in enumerate(dat):
                if val1 + val2 + val3 == 2020:
                    return val1 * val2 * val3


assert get_three_way_product_result(sample_input) == 241861950

solution_part2 = get_three_way_product_result(day1_input)
assert solution_part2 == 131347190
print(f"solution part2: {solution_part2}")
