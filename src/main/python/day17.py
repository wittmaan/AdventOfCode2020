from itertools import combinations

# --- Day 17: Conway Cubes ---
# --- Part one ---


sample_input = """.#.
..#
###"""

NUM_CYCLES = 6
ACTIVE_STATE = "#"


def build_grid(dat: str, dim):
    lines = dat.split("\n")
    padding = (0,) * (dim - 2)
    grid = [(i, j) + padding for j, row in enumerate(lines) for i, cell in enumerate(row) if cell == ACTIVE_STATE]
    return set(grid)


def build_neighbors(point):
    dim = len(point)
    neighbors = set()
    for deltas in set(combinations([-1, 0, 1] * dim, dim)):
        if any(delta != 0 for delta in deltas):
            neighbors.add(tuple(pos + delta for pos, delta in zip(point, deltas)))
    return neighbors


def get_neighbors_not_grid(grid):
    new_grid = set()
    for point in grid:
        for neighbor in build_neighbors(point):
            if neighbor not in grid:
                new_grid.add(neighbor)

    return new_grid


def count_active_neighbors(neighbors, grid):
    return sum(p in grid for p in neighbors)


def run_one_cycle(input_grid):
    new_grid = set()
    add_new_points(input_grid, new_grid, valid_active_values=[2, 3])
    add_new_points(input_grid, new_grid, valid_active_values=[3], extend_grid=True)
    return new_grid


def add_new_points(input_grid, new_grid, valid_active_values, extend_grid: bool = False):
    grid = get_neighbors_not_grid(input_grid) if extend_grid else input_grid

    for point in grid:
        neighbors = build_neighbors(point)
        active_neighbors = count_active_neighbors(neighbors, input_grid)
        if active_neighbors in valid_active_values:
            new_grid.add(point)


def run(dat: str, dim: int):
    grid = build_grid(dat, dim)

    for _ in range(NUM_CYCLES):
        grid = run_one_cycle(grid)

    return len(grid)


assert run(dat=sample_input, dim=3) == 112

puzzle_input = """####...#
......#.
#..#.##.
.#...#.#
..###.#.
##.###..
.#...###
.##....#"""

solution_part1 = run(dat=puzzle_input, dim=3)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 286

# --- Part two ---

assert run(dat=sample_input, dim=4) == 848

solution_part2 = run(dat=puzzle_input, dim=4)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 960
