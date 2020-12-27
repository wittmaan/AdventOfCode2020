import fileinput
from typing import List

# --- Day 16: Ticket Translation ---
# --- Part one ---


FIELD_RANGES = "FIELD_RANGES"
YOUR_TICKET = "YOUR_TICKET"
NEARBY_TICKETS = "NEARBY_TICKETS"

sample_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split(
    "\n"
)


class Field:
    def __init__(self, name, input_str):
        self.name = name
        self.values: List[int] = Field.create_list(input_str)

    @staticmethod
    def create_list(input_str: str) -> List[int]:
        part1, part2 = input_str.split(" or ")
        result = []
        for p in [part1, part2]:
            splitted = p.split("-")
            result.extend([int(_) for _ in range(int(splitted[0]), int(splitted[1]) + 1)])

        return result


def get_error_rate(dat: List[str]) -> int:
    mode = FIELD_RANGES
    nearby_tickets = []
    fields = []

    for d in dat:
        if d == "":
            continue
        elif d.startswith("your ticket"):
            mode = YOUR_TICKET
            continue
        elif d.startswith("nearby tickets"):
            mode = NEARBY_TICKETS
            continue

        if mode == FIELD_RANGES:
            field_name, value_range = d.split(": ")
            fields.append(Field(field_name, value_range))

        elif mode == YOUR_TICKET:
            your_tickets = [int(_) for _ in d.split(",")]
            # print(f"your_tickets {your_tickets}")
        elif mode == NEARBY_TICKETS:
            sub_nearby_tickets = [int(_) for _ in d.split(",")]
            nearby_tickets.extend(sub_nearby_tickets)

    # print(f"nearby_tickets {nearby_tickets}")

    invalid_nearby_tickets = []
    for nearby_ticket in nearby_tickets:
        if not any([nearby_ticket in field.values for field in fields]):
            invalid_nearby_tickets.append(nearby_ticket)

    return sum(invalid_nearby_tickets)


assert get_error_rate(sample_input) == 71

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = get_error_rate(puzzle_input)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 25895


# --- Part two ---

# assert get_number_spoken(sample_input, at_turn=30000000) == 175594
#
# solution_part2 = get_number_spoken("7,12,1,0,16,2", at_turn=30000000)
# print(f"solution part2: {solution_part2}")
# assert solution_part2 == 238
