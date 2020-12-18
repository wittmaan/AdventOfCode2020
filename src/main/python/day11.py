import fileinput
from copy import deepcopy

from typing import List

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

EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


def show_grid(grid: List[List[str]]):
    print("\n".join(["".join([col for col in row]) for row in grid]))
    print("-------------------------------")


def detect_stable_state(grid_input: List[str]):
    grid = [list(_.strip()) for _ in grid_input]

    num_rows = len(grid)
    num_cols = len(grid[0])

    while True:
        # show_grid(grid)

        new_grid = step(grid, num_rows, num_cols)
        if new_grid == grid:
            break

        grid = new_grid

    num_occupied_seats = sum(seat == OCCUPIED_SEAT for row in grid for seat in row)
    return num_occupied_seats


def count_occupied_neighbor_seats(
    grid: List[List[str]], idx_row: int, idx_col: int, num_rows: int, num_cols: int
) -> int:
    count = 0
    for delta_row in [-1, 0, 1]:
        for delta_col in [-1, 0, 1]:
            if delta_row or delta_col:
                new_row = idx_row + delta_row
                new_col = idx_col + delta_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == OCCUPIED_SEAT:
                    count += 1

    return count


def get_new_value(grid: List[List[str]], idx_row: int, idx_col: int, num_rows: int, num_cols: int):
    actual_value = grid[idx_row][idx_col]

    count = count_occupied_neighbor_seats(grid, idx_row, idx_col, num_rows, num_cols)

    if actual_value == EMPTY_SEAT and count == 0:
        return OCCUPIED_SEAT
    elif actual_value == OCCUPIED_SEAT and count >= 4:
        return EMPTY_SEAT
    else:
        return actual_value


def step(grid: List[List[str]], num_rows: int, num_cols: int):
    grid_copy = deepcopy(grid)

    for idx_row, val_row in enumerate(grid):
        for idx_col, val_col in enumerate(val_row):
            grid_copy[idx_row][idx_col] = get_new_value(grid, idx_row, idx_col, num_rows, num_cols)

    return grid_copy


assert detect_stable_state(sample_input) == 37


puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = detect_stable_state(puzzle_input)
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
