import fileinput
from collections import Counter
from functools import reduce
from operator import and_, or_

# --- Day 6: Custom Customs ---
# --- Part one ---

sample_group = """abcx
abcy
abcz"""


def get_answers(dat: str, function=or_):
    splitted = dat.split("\n")
    counter_list = [Counter(_) for _ in splitted]

    return len(reduce(function, counter_list))


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


def count_yes_answers(dat: str, function=or_):
    return sum([get_answers(_, function=function) for _ in dat.split("\n\n")])


assert count_yes_answers(sample_input) == 11

day6_input = "".join([_ for _ in fileinput.input()])

solution_part1 = count_yes_answers(day6_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 6612


# --- Part two ---

assert get_answers(sample_group, function=and_) == 3
assert get_answers("abc", function=and_) == 3
assert get_answers("a\nb\nc", function=and_) == 0
assert get_answers("ab\nac", function=and_) == 1
assert get_answers("a\na\na\na", function=and_) == 1
assert get_answers("b", function=and_) == 1


solution_part2 = count_yes_answers(day6_input, function=and_)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 3268
