import fileinput
import re
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


def extract_passports(dat: str):
    passport_list = []
    for entry in dat.split("\n\n"):
        entry_splitted = entry.strip().replace("\n", " ").split(" ")

        passport = {}
        for val in entry_splitted:
            key, value = val.split(":")
            passport[key] = value

        passport_list.append(passport)

    return passport_list


sample_passports = extract_passports(sample_input)

BIRTH_YEAR = "byr"

REQUIRED_FIELDS = (BIRTH_YEAR, "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


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

passports = extract_passports(day4_input)

solution_part1 = count_valid_passports(passports)
print(f"solution part1: {solution_part1}")
assert solution_part1 == 256


# --- Part two ---


def is_valid_birth_year(year: str) -> bool:
    return 1920 <= int(year) <= 2002


assert is_valid_birth_year(2002) is True
assert is_valid_birth_year(2003) is False


def is_valid_issue_year(year: str) -> bool:
    return 2010 <= int(year) <= 2020


assert is_valid_issue_year(2019) is True


def is_valid_expiration_year(year: str) -> bool:
    return 2020 <= int(year) <= 2030


def is_valid_height(height: str) -> bool:
    pattern = re.compile("(\\d+)\\s*(\\w*)")
    value, unit = pattern.match(height).groups() if pattern.match(height) is not None else (0, "")
    if unit == "cm":
        return 150 <= int(value) <= 193
    elif unit == "in" or unit == "":
        return 59 <= int(value) <= 76


assert is_valid_height("60in") is True
assert is_valid_height("190cm") is True
assert is_valid_height("190in") is False
assert is_valid_height("190") is False
assert is_valid_height("") is False


def is_valid_hair_color(color: str) -> bool:
    pattern = re.compile("^#[0-9a-f]{6}$")
    return pattern.match(color) is not None


assert is_valid_hair_color("#123abc") is True
assert is_valid_hair_color("#123abz") is False
assert is_valid_hair_color("123abc") is False


def is_valid_eye_color(color: str) -> bool:
    return color in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


assert is_valid_eye_color("brn") is True
assert is_valid_eye_color("wat") is False


def is_valid_passport_id(id: str) -> bool:
    pattern = re.compile("^[0-9]{9}$")
    return pattern.match(id) is not None


assert is_valid_passport_id("000000001") is True
assert is_valid_passport_id("0123456789") is False


def is_valid_passport_part2(passport: Dict[str, str]) -> bool:
    validation_dict = {
        "byr": is_valid_birth_year,
        "iyr": is_valid_issue_year,
        "eyr": is_valid_expiration_year,
        "hgt": is_valid_height,
        "hcl": is_valid_hair_color,
        "ecl": is_valid_eye_color,
        "pid": is_valid_passport_id,
    }

    checks = []
    for required_field in REQUIRED_FIELDS:
        field_value = passport.get(required_field)
        if field_value is not None:
            checks.append(validation_dict[required_field](field_value))
        else:
            checks.append(False)

    return all(checks)


invalid_passports = extract_passports(
    """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

hcl:#7d3b0c
pid:307828343 byr:2001
cid:317 iyr:2013
eyr:2029
"""
)

for invalid_passport in invalid_passports:
    assert is_valid_passport_part2(invalid_passport) is False

valid_passports = extract_passports(
    """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
)

for valid_passport in valid_passports:
    assert is_valid_passport_part2(valid_passport) is True


def count_valid_passports_part2(passports_input: List[Dict[str, str]]):
    return sum([is_valid_passport_part2(passport) for passport in passports_input])


solution_part2 = count_valid_passports_part2(passports)
print(f"solution part2: {solution_part2}")
assert solution_part2 == 198
