import fileinput
from typing import List

# --- Day 14: Docking Data ---
# --- Part one ---

sample_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split(
    "\n"
)


def program(dat: List[str]) -> int:
    memory = {}

    for line in dat:
        prefix, value = line.split(" = ")
        if prefix == "mask":
            mask = value
        else:
            memory_idx = prefix[4:-1]
            binary_value = list(str(bin(int(value)))[2:].zfill(36))

            for idx, val in enumerate(mask):
                if val != "X":
                    binary_value[idx] = val

            memory[memory_idx] = int("".join(binary_value), 2)

    return sum(memory.values())


assert program(sample_input) == 165

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = program(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 10452688630537


# --- Part two ---


# solution_part2 = find_matching_order(puzzle_input)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 842186186521918
