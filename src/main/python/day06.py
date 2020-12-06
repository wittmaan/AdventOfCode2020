import fileinput
from collections import Counter

# --- Day 6: Custom Customs ---
# --- Part one ---

sample_group = """abcx
abcy
abcz"""


def get_answers(dat: str):
    splitted = dat.split("\n")
    counter_list = [Counter(_) for _ in splitted]

    counter_total = Counter()
    for counter in counter_list:
        counter_total += counter

    return len(counter_total)


assert get_answers(sample_group) == 6
assert get_answers("abc") == 3
assert get_answers("a\nb\nc") == 3
assert get_answers("ab\nac") == 3
assert get_answers("a\na\na\na") == 1
assert get_answers("b") == 1


sample_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def count_yes_answers(dat: str):
    return sum([get_answers(_) for _ in dat.split("\n\n")])


assert count_yes_answers(sample_input) == 11

day6_input = "".join([_ for _ in fileinput.input()])

solution_part1 = count_yes_answers(day6_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 6612


# --- Part two ---


# assert solution_part2 == 2224913600
# print(f"solution part2: {solution_part2}")
