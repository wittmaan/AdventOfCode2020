import fileinput
from collections import Counter, defaultdict
from copy import deepcopy
from itertools import product
from typing import List

# --- Day 15: Rambunctious Recitation ---
# --- Part one ---

sample_input = "0,3,6"


class Memory:
    def __init__(self, numbers):
        self.counter = Counter(numbers)
        self.new_value = None

        self.indices = defaultdict(list)
        for idx, val in enumerate(numbers):
            self.indices[val].append(idx)

    def is_seen_first(self, number_to_check: int):
        return self.counter[number_to_check] == 1

    def is_seen_before(self, number_to_check: int):
        indices = self.indices[number_to_check]
        if len(indices) == 0:
            return False
        elif len(indices) > 1:
            self.new_value = indices[-1] - indices[-2]
            return True

    def update(self, number: int, idx: int):
        self.counter[number] += 1
        self.indices[number].append(idx)


def get_number_spoken(dat: str, at_turn: int = None) -> int:
    numbers = [int(_) for _ in dat.split(",")]
    turn = len(numbers) - 1
    memory = Memory(numbers)

    [numbers.append(-1) for _ in range(at_turn - len(numbers))]

    last_number = None
    while turn < at_turn:
        if memory.is_seen_first(last_number):
            numbers[turn] = 0
            memory.update(0, turn)
        elif memory.is_seen_before(last_number):
            numbers[turn] = memory.new_value
            memory.update(memory.new_value, turn)

        last_number = numbers[turn]
        turn += 1
    return numbers[at_turn - 1]


assert get_number_spoken(sample_input, at_turn=10) == 0
assert get_number_spoken(sample_input, at_turn=2020) == 436

assert get_number_spoken("1,3,2", at_turn=2020) == 1
assert get_number_spoken("2,1,3", at_turn=2020) == 10
assert get_number_spoken("1,2,3", at_turn=2020) == 27
assert get_number_spoken("2,3,1", at_turn=2020) == 78
assert get_number_spoken("3,2,1", at_turn=2020) == 438
assert get_number_spoken("3,1,2", at_turn=2020) == 1836


solution_part1 = get_number_spoken("7,12,1,0,16,2", at_turn=2020)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 410


# --- Part two ---

# sample_input2 = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1""".split(
#     "\n"
# )
#
# assert program(sample_input2, floating_mode=True) == 208
# solution_part2 = program(puzzle_input, floating_mode=True)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 2881082759597
