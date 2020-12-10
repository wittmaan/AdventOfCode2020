import fileinput

from dataclasses import dataclass
from typing import List

# --- Day 8: Handheld Halting ---
# --- Part one ---

sample_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split(
    "\n"
)


@dataclass
class Instruction:
    operation: str
    argument: int

    def __init__(self, input_line: str):
        splitted = input_line.split()
        self.operation, self.argument = splitted[0], int(splitted[1])


def run(dat: List[str]):
    instructions = [Instruction(line) for line in dat]
    positions_seen = set()
    position = 0
    accumulator = 0

    while position not in positions_seen:
        positions_seen.add(position)
        instruction = instructions[position]

        if instruction.operation == "acc":
            accumulator += instruction.argument
            position += 1
        elif instruction.operation == "jmp":
            position += instruction.argument
        elif instruction.operation == "nop":
            position += 1
        else:
            raise ValueError(f"unknown operation: {instruction.operation}")

    return position, accumulator


sample_result = run(sample_input)
assert sample_result == (1, 5)

day8_input = [_.strip() for _ in fileinput.input()]
solution_part1 = run(day8_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == (439, 1709)


# --- Part two ---
