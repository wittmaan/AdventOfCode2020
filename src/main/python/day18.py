# --- Day 18: Operation Order ---
# --- Part one ---
import fileinput
from typing import List


class Expression:
    def __init__(self):
        self.content = []

    def append(self, val):
        self.content.append(val)

    def calc(self):
        value = None
        act_operator = None
        for idx, val in enumerate(self.content):
            if val == "+":
                act_operator = "+"
            elif val == "*":
                act_operator = "*"
            else:
                if not value:
                    value = int(val)
                else:
                    if act_operator == "+":
                        value += int(val)
                    elif act_operator == "*":
                        value *= int(val)

        # print(f"value={value}")
        return value


class Calculator:
    def __init__(self, input_dat: str):
        self.dat = input_dat.replace(" ", "")
        self.expression_depth = 0
        self.expressions = {self.expression_depth: Expression()}
        self.result = self.run()

    def run(self):
        for idx, val in enumerate(self.dat):
            if val == "(":
                self.expression_depth += 1
                self.expressions[self.expression_depth] = Expression()
                self.expressions[self.expression_depth - 1].append(self.expressions[self.expression_depth])
            elif val == ")":
                self.expressions[self.expression_depth - 1].content[-1] = self.expressions[self.expression_depth].calc()
                self.expression_depth -= 1
            else:
                self.expressions[self.expression_depth].append(val)

        return self.expressions[self.expression_depth].calc()


assert Calculator("1 + 2 * 3 + 4 * 5 + 6").result == 71
assert Calculator("1 + (2 * 3) + (4 * (5 + 6))").result == 51
assert Calculator("2 * 3 + (4 * 5)").result == 26
assert Calculator("5 + (8 * 3 + 9 + 3 * 4 * 3)").result == 437
assert Calculator("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))").result == 12240
assert Calculator("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2").result == 13632


def sum_up_expressions(dat: List[str]):
    value = 0
    for d in dat:
        value += Calculator(d).result

    return value


puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = sum_up_expressions(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 21347713555555

# --- Part two ---

# assert run(dat=sample_input, dim=4) == 848
#
# solution_part2 = run(dat=puzzle_input, dim=4)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 960
