import fileinput
from typing import List, Dict

# --- Day 4: Passport Processing ---
# --- Part one ---

sample_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


def extract_passports(dat: List[str]):
    passport_list = []
    for entry in dat:
        entry_splitted = entry.strip().replace("\n", " ").split(" ")

        passport = {}
        # print(f"entry_splitted {entry_splitted}")
        for val in entry_splitted:
            key, value = val.split(":")
            passport[key] = value

        passport_list.append(passport)

    return passport_list


sample_passports = extract_passports(sample_input.split("\n\n"))

REQUIRED_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # , "cid")


def is_valid_passport(passport: Dict[str, str]) -> bool:
    return all([required_field in passport.keys() for required_field in REQUIRED_FIELDS])


assert is_valid_passport(sample_passports[0]) is True
assert is_valid_passport(sample_passports[1]) is False
assert is_valid_passport(sample_passports[2]) is True
assert is_valid_passport(sample_passports[3]) is False


def count_valid_passports(passports_input: List[Dict[str, str]]):
    return sum([is_valid_passport(passport) for passport in passports_input])


assert count_valid_passports(sample_passports) == 2


day4_input = "".join([_ for _ in fileinput.input()])

passports = extract_passports(day4_input.split("\n\n"))

solution_part1 = count_valid_passports(passports)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 256


# --- Part two ---


# solution_part2 = count_trees_multiple_movements()
# assert solution_part2 == 2224913600
# print(f"solution part2: {solution_part2}")
