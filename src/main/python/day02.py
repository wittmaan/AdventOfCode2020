import fileinput
from collections import Counter
from dataclasses import dataclass
from typing import List


# --- Day 2: Password Philosophy ---
# --- Part one ---


@dataclass
class PasswordData:
    position_first: int
    position_second: int
    target_letter: str
    password_to_check: str


class PasswordValidation:
    def __init__(self, line: str):
        self.input_data = self.line_to_data(line)
        # print(f"input_data={self.input_data}")

    @staticmethod
    def line_to_data(line: str):
        from_to, target_letter, password_to_check = line.split(" ")

        occurrence_minimal, occurrence_maximal = from_to.split("-")
        return PasswordData(
            position_first=int(occurrence_minimal),
            position_second=int(occurrence_maximal),
            target_letter=target_letter[:-1],
            password_to_check=password_to_check,
        )

    def check(self):
        counter = Counter(self.input_data.password_to_check)
        target_occurrence = counter[self.input_data.target_letter]
        return self.input_data.position_first <= target_occurrence <= self.input_data.position_second

    def check2(self):
        is_first_position_matched = (
            self.input_data.password_to_check[self.input_data.position_first - 1] == self.input_data.target_letter
        )
        is_second_position_matched = (
            self.input_data.password_to_check[self.input_data.position_second - 1] == self.input_data.target_letter
        )

        return is_first_position_matched != is_second_position_matched


sample_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

assert PasswordValidation(sample_input[0]).check() is True
assert PasswordValidation(sample_input[1]).check() is False
assert PasswordValidation(sample_input[2]).check() is True


def get_number_valid_passwords_part1(dat: List[str]):
    return sum([PasswordValidation(_).check() for _ in dat])


assert get_number_valid_passwords_part1(sample_input) == 2

day2_input = [_.strip() for _ in fileinput.input()]

solution_part1 = get_number_valid_passwords_part1(day2_input)
assert solution_part1 == 550
print(f"solution part1: {solution_part1}")


# --- Part two ---

assert PasswordValidation(sample_input[0]).check2() is True
assert PasswordValidation(sample_input[1]).check2() is False
assert PasswordValidation(sample_input[2]).check2() is False


def get_number_valid_passwords_part2(dat: List[str]):
    return sum([PasswordValidation(_).check2() for _ in dat])


assert get_number_valid_passwords_part2(sample_input) == 1

solution_part2 = get_number_valid_passwords_part2(day2_input)
assert solution_part2 == 634
print(f"solution part2: {solution_part2}")
