import re
from utils import timer


def get_input_data():
    passports_as_dicts = []

    with open("inputs/day04.txt", "r") as fp:
        passports = fp.read().split("\n\n")
        for passport in passports:
            if not passport:
                continue

            passport = passport.replace("\n", " ").split(" ")

            passport_as_dict = {}
            for split in passport:
                if split:
                    key, value = split.split(":")
                    passport_as_dict[key] = value

            passports_as_dicts.append(passport_as_dict)

    return passports_as_dicts


@timer
def puzzle_1():
    data = get_input_data()
    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid_count = 0
    for passport in data:
        if all(key in passport for key in needed_keys):
            valid_count += 1

    return valid_count


@timer
def puzzle_2():
    data = get_input_data()
    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid_count = 0

    for passport in data:
        if not all(key in passport for key in needed_keys):
            continue

        for key, value in passport.items():
            if key == "byr":
                if not (int(value) >= 1920 and int(value) <= 2002):
                    break

            elif key == "iyr":
                if not (int(value) >= 2010 and int(value) <= 2020):
                    break

            elif key == "eyr":
                if not (int(value) >= 2020 and int(value) <= 2030):
                    break

            elif key == "hgt":
                if not re.match(r"(\d*)(cm|in)$", value):
                    break

                unit = value[-2:]
                height = int(value[:-2])

                if unit == "cm" and not (height >= 150 and height <= 193):
                    break
                elif unit == "in" and not (height >= 59 and height <= 76):
                    break

            elif key == "hcl":
                if not re.match(r"#[a-f0-9]{6}$", value):
                    break

            elif key == "ecl":
                if value not in ["amb", "blu", "brn",
                                 "gry", "grn", "hzl", "oth"]:
                    break

            elif key == "pid":
                if not re.match(r"\A[0-9]{9}$", value):
                    break

        else:
            valid_count += 1

    return valid_count


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
