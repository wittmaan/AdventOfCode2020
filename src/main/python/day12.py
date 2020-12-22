import fileinput
from dataclasses import dataclass
from math import cos, radians, sin
from typing import List
import numpy as np


# --- Day 12: Rain Risk ---
# --- Part one ---


@dataclass
class Position:
    x: float
    y: float


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


def build_instructions(dat: List[str]) -> List[Instruction]:
    return [Instruction(_[0], int(_[1:])) for _ in dat]


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
        elif instruction.action == "L":
            direction += instruction.value
        elif instruction.action == "R":
            direction -= instruction.value
        elif instruction.action == "F":
            position.x += int(cos(radians(direction))) * instruction.value
            position.y += int(sin(radians(direction))) * instruction.value

    return abs(position.x) + abs(position.y)


assert detect_final_position(build_instructions(sample_input)) == 25

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = detect_final_position(build_instructions(puzzle_input))
print(f"solution part1: {solution_part1}")
assert solution_part1 == 923


# --- Part two ---


def rotate(position, degrees):
    theta = np.radians(degrees)
    c = cos(theta)
    s = sin(theta)
    R = np.array(((c, -s), (s, c)))
    result = np.matmul(R, np.array([position.x, position.y]))
    return Position(result[0], result[1])


def detect_final_position_with_waypoint(instructions: List[Instruction]):
    position: Position = Position(0, 0)
    waypoint_position: Position = Position(10, 1)

    for instruction in instructions:
        if instruction.action == "N":
            waypoint_position.y += instruction.value
        elif instruction.action == "S":
            waypoint_position.y -= instruction.value
        elif instruction.action == "E":
            waypoint_position.x += instruction.value
        elif instruction.action == "W":
            waypoint_position.x -= instruction.value
        elif instruction.action == "L":
            waypoint_position = rotate(waypoint_position, instruction.value)
        elif instruction.action == "R":
            waypoint_position = rotate(waypoint_position, -instruction.value)
        elif instruction.action == "F":
            position.x += waypoint_position.x * instruction.value
            position.y += waypoint_position.y * instruction.value

    return round(abs(position.x) + abs(position.y))


assert detect_final_position_with_waypoint(build_instructions(sample_input)) == 286

solution_part2 = detect_final_position_with_waypoint(build_instructions(puzzle_input))
print(f"solution part2: {solution_part2}")
assert solution_part2 == 24769
