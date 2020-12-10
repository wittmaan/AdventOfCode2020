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


def build_instructions(dat: List[str]) -> List[Instruction]:
    instructions = []
    for d in dat:
        splitted = d.split()
        instructions.append(Instruction(splitted[0], int(splitted[1])))
    return instructions


def run(instructions: List[Instruction]):
    positions_seen = set()
    position = 0
    accumulator = 0

    while position not in positions_seen:
        if position == len(instructions):
            return position, accumulator, True

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

    return position, accumulator, False


sample_result = run(build_instructions(sample_input))
assert sample_result == (1, 5, False)

day8_input = [_.strip() for _ in fileinput.input()]
solution_part1 = run(build_instructions(day8_input))
print(f"solution part1: {solution_part1}")
assert solution_part1 == (439, 1709, False)


# --- Part two ---


def detect_termination(instructions: List[Instruction]):
    for idx, instruction in enumerate(instructions):
        instructions_copy = instructions[:]

        if instruction.operation == "nop":
            instructions_copy[idx] = Instruction(operation="jmp", argument=instructions_copy[idx].argument)
        elif instruction.operation == "jmp":
            instructions_copy[idx] = Instruction(operation="nop", argument=instructions_copy[idx].argument)

        tmp_result = run(instructions_copy)

        if tmp_result[2]:
            return tmp_result


sample_result_part2 = detect_termination(build_instructions(sample_input))
assert sample_result_part2 == (9, 8, True)

solution_part2 = detect_termination(build_instructions(day8_input))
print(f"solution part2: {solution_part2}")
assert solution_part2 == (617, 1976, True)
