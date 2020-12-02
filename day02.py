import sys
import re

def get_input_data():
    p = re.compile(r"(?P<min>\d*)-(?P<max>\d*) (?P<char>.): (?P<pw>.*)")
    with open("inputs/day02.txt", "r") as fp:
        return [match.groupdict()
                for match in re.finditer(p, fp.read())]


def puzzle_1():
    data = get_input_data()
    valid_passwords = 0

    for line in data:
        count = line["pw"].count(line["char"])
        min_ = int(line["min"])
        max_ = int(line["max"])

        if count >= min_ and count <= max_:
            valid_passwords += 1

    return valid_passwords

def puzzle_2():
    data = get_input_data()
    valid_passwords = 0

    for line in data:
        pw = line["pw"]
        char = line["char"]
        min_ = int(line["min"])
        max_ = int(line["max"])

        min_char = pw[min_-1]
        max_char = pw[max_-1]

        if (not (min_char == char and max_char == char)
               and (min_char == char or max_char == char)):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
