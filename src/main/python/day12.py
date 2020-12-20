from dataclasses import dataclass
from typing import List


# --- Day 12: Rain Risk ---
# --- Part one ---


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Instruction:
    action: str
    value: int


sample_input = """F10
N3
F7
R90
F11""".split(
    "\n"
)

print(sample_input)

instructions = [Instruction(_[0], int(_[1:])) for _ in sample_input]
print(instructions)


def detect_final_position(instructions: List[Instruction]):
    position: Position = Position(0, 0)
    direction: int = 0

    for instruction in instructions:
        if instruction.action == "N":
            position.y += instruction.value
        elif instruction.action == "S":
            position.y -= instruction.value
        elif instruction.action == "E":
            position.x += instruction.value
        elif instruction.action == "W":
            position.x -= instruction.value

    return position

print(detect_final_position(instructions))

# puzzle_input = [_.strip() for _ in fileinput.input()]
# solution_part1 = StableStateDetector(puzzle_input).num_occupied_seats
# print(f"solution part1: {solution_part1}")
# assert solution_part1 == 2418


# --- Part two ---

# assert (
#     StableStateDetector(
#         grid_input=sample_input, visible_occupied_seats_limit=5, find_first_mode=True
#     ).num_occupied_seats
#     == 26
# )
#
# solution_part2 = StableStateDetector(
#     grid_input=puzzle_input, visible_occupied_seats_limit=5, find_first_mode=True
# ).num_occupied_seats
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 2144
