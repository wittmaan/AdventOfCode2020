from dataclasses import dataclass
from collections import Counter
from typing import List, Set
import fileinput

# --- Day 3: Toboggan Trajectory ---
# --- Part one ---

sample_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Slope:
    trees: List[Position]
    width: int
    height: int


def build_slope(lines: List[str]) -> Slope:
    trees = []
    for idx1, line in enumerate(lines):
        for idx2, actual_char in enumerate(line):
            if actual_char == "#":
                trees.append((Position(idx2, idx1)))

    return Slope(trees=trees, height=len(lines), width=len(line))


def count_trees(delta_x: int, delta_y: int, slope: Slope):
    count = 0
    x = 0
    y = 0

    while y < slope.height:
        x = x % slope.width
        y = y % slope.height
        if Position(x, y) in slope.trees:
            count += 1

        x += delta_x
        y += delta_y

    return count


sample_slope = build_slope(sample_input.split("\n"))
assert count_trees(delta_x=3, delta_y=1, slope=sample_slope) == 7

day3_input = [_.strip() for _ in fileinput.input()]

input_slope = build_slope(day3_input)

counted_trees = count_trees(delta_x=3, delta_y=1, slope=input_slope)
assert counted_trees == 259
print(f"solution part1: {counted_trees}")


# --- Part two ---

movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for movement in movements:
    result *= count_trees(delta_x=movement[0], delta_y=movement[1], slope=input_slope)

assert result == 2224913600
print(f"solution part2: {result}")
