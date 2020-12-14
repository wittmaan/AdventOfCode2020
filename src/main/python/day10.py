import fileinput
from collections import defaultdict

from typing import List

# --- Day 10: Adapter Array ---
# --- Part one ---

sample_input1 = """16
10
15
5
1
11
7
19
6
12
4""".split(
    "\n"
)

sample_input1 = [int(_) for _ in sample_input1]

sample_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split(
    "\n"
)
sample_input2 = [int(_) for _ in sample_input2]


def calc_differences(dat: List[int]) -> int:
    dat.append(0)
    dat.append(max(dat) + 3)
    dat.sort()

    differences = [(val2 - val1) for val1, val2 in zip(dat, dat[1:])]
    return differences.count(1) * differences.count(3)


assert calc_differences(sample_input1) == 35
assert calc_differences(sample_input2) == 220


day10_input = [int(_.strip()) for _ in fileinput.input()]
solution_part1 = calc_differences(dat=day10_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 1984


# --- Part two ---


def detect_arrangements(dat: List[int]) -> int:
    dat.append(max(dat) + 3)
    dat.sort()

    count_dict = defaultdict(int)
    count_dict[0] = 1

    for d in dat[1:]:
        count_dict[d] = count_dict[d - 3] + count_dict[d - 2] + count_dict[d - 1]

    return max(count_dict.values())


assert detect_arrangements(sample_input1) == 8

solution_part2 = detect_arrangements(day10_input)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 3543369523456
