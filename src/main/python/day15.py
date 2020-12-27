from collections import defaultdict

# --- Day 15: Rambunctious Recitation ---
# --- Part one ---

sample_input = "0,3,6"


class Memory:
    def __init__(self, numbers):
        self.new_value = None

        self.indices = defaultdict(list)
        for idx, val in enumerate(numbers):
            self.indices[val].append(idx)

    def is_seen_before(self, number_to_check: int):
        indices = self.indices[number_to_check]
        if len(indices) == 0:
            return False
        elif len(indices) == 1:
            self.new_value = 0
            return True
        elif len(indices) > 1:
            self.new_value = indices[-1] - indices[-2]
            self.indices[number_to_check] = indices[-2:]
            return True

    def update(self, number: int, idx: int):
        self.indices[number].append(idx)


def get_number_spoken(dat: str, at_turn: int = None) -> int:
    numbers = [int(_) for _ in dat.split(",")]
    turn = len(numbers) - 1
    memory = Memory(numbers)

    [numbers.append(-1) for _ in range(at_turn - len(numbers))]

    last_number = None
    while turn < at_turn:
        if turn % 100000 == 0:
            print(f" {turn} / {at_turn}")

        if memory.is_seen_before(last_number):
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

assert get_number_spoken(sample_input, at_turn=30000000) == 175594

solution_part2 = get_number_spoken("7,12,1,0,16,2", at_turn=30000000)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 238
