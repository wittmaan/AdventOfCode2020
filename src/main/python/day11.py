import fileinput
from copy import deepcopy
from typing import List

import numpy as np
from numba import njit

# --- Day 11: Seating System ---
# --- Part one ---


sample_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split(
    "\n"
)

EMPTY_SEAT_ORIG = "L"
OCCUPIED_SEAT_ORIG = "#"
FLOOR_ORIG = "."


EMPTY_SEAT = 0
OCCUPIED_SEAT = 1
FLOOR = 2


POSITIONS_MAPPING = {EMPTY_SEAT_ORIG: EMPTY_SEAT, OCCUPIED_SEAT_ORIG: OCCUPIED_SEAT, FLOOR_ORIG: FLOOR}


class StableStateDetector:
    def __init__(self, grid_input: List[str]):
        self.grid = np.array(
            [[POSITIONS_MAPPING[act_position] for act_position in list(_.strip())] for _ in grid_input]
        )
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        self.num_occupied_seats = self.run()

    def run(self):

        while True:
            # self.show_grid()

            new_grid = self.step()
            if (new_grid == self.grid).all():
                break

            self.grid = new_grid

        num_occupied_seats = sum(seat == OCCUPIED_SEAT for row in self.grid for seat in row)
        return num_occupied_seats

    def step(self):
        grid_copy = deepcopy(self.grid)

        for idx_row, val_row in enumerate(grid_copy):
            for idx_col, val_col in enumerate(val_row):
                grid_copy[idx_row][idx_col] = get_new_value(self.grid, idx_row, idx_col, self.num_rows, self.num_cols)
        return grid_copy

    def show_grid(self):
        print("\n".join(["".join([str(col) for col in row]) for row in self.grid]))
        print("-------------------------------")


@njit
def count_occupied_neighbor_seats(grid: np.ndarray, idx_row: int, idx_col: int, num_rows: int, num_cols: int) -> int:
    count = 0
    for delta_row in [-1, 0, 1]:
        for delta_col in [-1, 0, 1]:
            if delta_row or delta_col:
                new_row = idx_row + delta_row
                new_col = idx_col + delta_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == OCCUPIED_SEAT:
                    count += 1

    return count


@njit
def get_new_value(grid: np.ndarray, idx_row: int, idx_col: int, num_rows: int, num_cols: int):
    actual_value = grid[idx_row][idx_col]

    count = count_occupied_neighbor_seats(grid, idx_row, idx_col, num_rows, num_cols)

    if actual_value == EMPTY_SEAT and count == 0:
        return OCCUPIED_SEAT
    elif actual_value == OCCUPIED_SEAT and count >= 4:
        return EMPTY_SEAT
    else:
        return actual_value


assert StableStateDetector(sample_input).num_occupied_seats == 37

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = StableStateDetector(puzzle_input).num_occupied_seats
print(f"solution part1: {solution_part1}")
assert solution_part1 == 2418


# --- Part two ---


# def detect_arrangements(dat: List[int]) -> int:
#     dat.append(max(dat) + 3)
#     dat.sort()
#
#     count_dict = defaultdict(int)
#     count_dict[0] = 1
#
#     for d in dat[1:]:
#         count_dict[d] = count_dict[d - 3] + count_dict[d - 2] + count_dict[d - 1]
#
#     return max(count_dict.values())
#
#
# assert detect_arrangements(sample_input1) == 8
#
# solution_part2 = detect_arrangements(day10_input)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 3543369523456
