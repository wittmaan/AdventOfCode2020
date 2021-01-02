# --- Day 18: Operation Order ---
# --- Part one ---


class Expression:
    def __init__(self):
        self.content = []

    def add(self, val):
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


def calculate(input_dat: str):
    dat = input_dat.replace(" ", "")

    expression_depth = 0
    expressions = {expression_depth: Expression()}

    for idx, val in enumerate(dat):
        if val == "(":
            expression_depth += 1
            expressions[expression_depth] = Expression()
            expressions[expression_depth - 1].add(expressions[expression_depth])
        elif val == ")":
            expressions[expression_depth - 1].content[-1] = expressions[expression_depth].calc()
            expression_depth -= 1
        else:
            expressions[expression_depth].add(val)

    return expressions[expression_depth].calc()


assert calculate("1 + 2 * 3 + 4 * 5 + 6") == 71
assert calculate("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert calculate("2 * 3 + (4 * 5)") == 26
assert calculate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert calculate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

# solution_part1 = run(dat=puzzle_input, dim=3)
# print(f"solution part1: {solution_part1}")
# assert solution_part1 == 286

# --- Part two ---

# assert run(dat=sample_input, dim=4) == 848
#
# solution_part2 = run(dat=puzzle_input, dim=4)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 960
