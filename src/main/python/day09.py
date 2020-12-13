import fileinput
from collections import deque

from random import shuffle, seed
from typing import List

# --- Day 9: Encoding Error ---
# --- Part one ---


sample_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split(
    "\n"
)
sample_input = [int(_) for _ in sample_input]

sample_numbers = [_ + 1 for _ in range(25)]

seed(42)
shuffle(sample_numbers)


def is_valid(dat: List[int], number: int) -> bool:
    for idx1, d1 in enumerate(dat):
        for idx2, d2 in enumerate(dat):
            if idx1 < idx2:
                if d1 + d2 == number:
                    return True
    return False


assert is_valid(sample_numbers, 26) is True
assert is_valid(sample_numbers, 49) is True
assert is_valid(sample_numbers, 100) is False
assert is_valid(sample_numbers, 50) is False


def find_first_not_sum(dat: List[int], preamble_length: int = 5):
    queue = deque(dat[:preamble_length])

    for d in dat[preamble_length:]:
        if not is_valid(list(queue), d):
            return d
        else:
            queue.append(d)
            queue.popleft()


assert find_first_not_sum(sample_input) == 127

day9_input = [int(_.strip()) for _ in fileinput.input()]
solution_part1 = find_first_not_sum(dat=day9_input, preamble_length=25)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 552655238


# --- Part two ---


def find_encryption_weakness(dat: List[int], preamble_length: int = 5):
    invalid_number = find_first_not_sum(dat, preamble_length)

    solution = None
    for idx1, val in enumerate(dat):
        idx2 = 0
        while idx2 < idx1:
            if sum(dat[idx2:idx1]) == invalid_number:
                solution = dat[idx2:idx1]
                break
            idx2 += 1

        if solution is not None:
            break

    return min(solution) + max(solution)


assert find_encryption_weakness(sample_input) == 62

solution_part2 = find_encryption_weakness(dat=day9_input, preamble_length=25)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 70672245
