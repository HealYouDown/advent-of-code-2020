import math


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


def puzzle_1():
    data = get_input_data()
    needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    valid_count = 0
    for passport in data:
        if all(key in passport for key in needed_keys):
            valid_count += 1

    return valid_count


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
                if not (int(value) >= 2020 and int(value) < 2030):
                    break

            elif key == "hgt":
                height = value[:-2]
                unit = value[-2:]
                if not unit in ["in", "cm"]:
                    break

                try:
                    int(height)
                except ValueError:
                    break

            elif key == "hcl":
                if len(value) != 7:
                    break

                if value[0] != "#":
                    break

                color = value[1:]
                # TODO: Regex

            elif key == "ecl":
                if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    break

            elif key == "pid":
                if len(value) != 9:
                    break

                try:
                    int(value)
                except ValueError:
                    break

        else:
            valid_count += 1

    return valid_count


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())