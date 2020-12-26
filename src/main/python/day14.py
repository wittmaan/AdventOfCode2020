import fileinput
from copy import deepcopy
from itertools import product
from typing import List

# --- Day 14: Docking Data ---
# --- Part one ---

sample_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split(
    "\n"
)


def program(dat: List[str], floating_mode: bool = False) -> int:
    memory = {}

    for line in dat:
        prefix, value = line.split(" = ")
        if prefix == "mask":
            mask = value
        else:
            memory_idx = int(prefix[4:-1])
            if floating_mode:
                binary_memory_idx = list(str(bin(int(memory_idx)))[2:].zfill(36))
                update_mask_to_one(binary_memory_idx, mask)
                floating_idx_list = [idx for idx, val in enumerate(mask) if val == "X"]

                for floating_bit_combinations in product("01", repeat=len(floating_idx_list)):
                    binary_memory_idx_copy = deepcopy(binary_memory_idx)

                    for idx, val in enumerate(floating_idx_list):
                        binary_memory_idx_copy[val] = floating_bit_combinations[idx]

                    memory[int("".join(binary_memory_idx_copy), 2)] = int(value)
            else:
                binary_value = list(str(bin(int(value)))[2:].zfill(36))
                update_mask_not_x(binary_value, mask)
                memory[memory_idx] = int("".join(binary_value), 2)

    return sum(memory.values())


def update_mask_not_x(binary_value, mask):
    for idx, val in enumerate(mask):
        if val != "X":
            binary_value[idx] = val


def update_mask_to_one(binary_memory_idx, mask):
    for idx, val in enumerate(mask):
        if val == "1":
            binary_memory_idx[idx] = val


assert program(sample_input) == 165

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = program(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 10452688630537


# --- Part two ---

sample_input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split(
    "\n"
)

assert program(sample_input2, floating_mode=True) == 208
solution_part2 = program(puzzle_input, floating_mode=True)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 2881082759597
