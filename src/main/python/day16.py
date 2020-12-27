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
        self.name: str = name
        self.values: List[int] = Field.create_list(input_str)
        self.position = None
        self.ticket = None

    @staticmethod
    def create_list(input_str: str) -> List[int]:
        part1, part2 = input_str.split(" or ")
        result = []
        for p in [part1, part2]:
            splitted = p.split("-")
            result.extend([int(_) for _ in range(int(splitted[0]), int(splitted[1]) + 1)])

        return result

    def __lt__(self, other):
        return self.position < other.position


class TicketTranslation:
    def __init__(self, dat: List[str]):
        self.fields = []
        self.nearby_tickets = []
        self.your_tickets = None
        self.invalid_values = []
        self.fill(dat)

    def get_error_rate(self) -> int:
        invalid_nearby_tickets = []
        valid_nearby_tickets = []
        for nearby_ticket in self.nearby_tickets:
            if not self.is_valid_ticket(nearby_ticket):
                invalid_nearby_tickets.append(nearby_ticket)
            else:
                valid_nearby_tickets.append(nearby_ticket)

        self.nearby_tickets = valid_nearby_tickets
        return sum(self.invalid_values)

    def is_valid_ticket(self, ticket):
        is_valid = []
        for t in ticket:
            checks = []
            for field in self.fields:
                checks.append(t in field.values)

            if not any(checks):
                self.invalid_values.append(t)

            is_valid.append(any(checks))

        return all(is_valid)

    def fill(self, dat: List[str]):
        mode = FIELD_RANGES

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
                self.fields.append(Field(field_name, value_range))
            elif mode == YOUR_TICKET:
                self.your_tickets = [int(_) for _ in d.split(",")]
            elif mode == NEARBY_TICKETS:
                sub_nearby_tickets = [int(_) for _ in d.split(",")]
                self.nearby_tickets.append(sub_nearby_tickets)

    def get_departure_values(self):
        TicketTranslation.assign_positions(self.nearby_tickets, self.fields)
        self.update_fields()
        TicketTranslation.assign_positions(self.your_tickets, self.fields)

        result = 1
        for field in self.fields:
            if field.name.startswith("departure"):
                result *= field.ticket
        return result

    @staticmethod
    def assign_positions(tickets, fields):
        position = 1
        for ticket in tickets:
            for field in fields:
                if all(t in field.values for t in ticket) and not field.position:
                    field.position = position
                    field.ticket = ticket
                    position += 1
                    break


    def update_fields(self):
        # check remaining fields
        position = -1
        for field in self.fields:
            if field.position and field.position > position:
                position = field.position

        for field in self.fields:
            if not field.position:
                position += 1
                field.position = position

        self.fields.sort()
        for field in self.fields:
            field.position = None
            field.ticket = None


tt_sample = TicketTranslation(sample_input)
assert tt_sample.get_error_rate() == 71
assert tt_sample.nearby_tickets == [[7, 3, 47]]

puzzle_input = [_.strip() for _ in fileinput.input()]
tt = TicketTranslation(puzzle_input)
solution_part1 = tt.get_error_rate()
print(f"solution part1: {solution_part1}")
assert solution_part1 == 25895


# --- Part two ---

sample_input2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split(
    "\n"
)

tt_sample2 = TicketTranslation(sample_input2)
assert tt_sample2.get_error_rate() == 0
assert tt_sample2.invalid_values == []
assert tt_sample2.get_departure_values() == 1

#solution_part2 = tt.get_departure_values()
#print(f"solution part2: {solution_part2}")
# assert solution_part1 == 25895
