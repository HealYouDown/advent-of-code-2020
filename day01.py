import typing
import sys

def get_input_data() -> typing.List[int]:
    with open("inputs/day01.txt", "r") as fp:
        return [int(line) for line in fp.readlines() if line]


def puzzle_1():
    data = get_input_data()

    for number in data:
        for number2 in data:
            if number + number2 == 2020:
                return number * number2


def puzzle_2():
    data = get_input_data()

    for number in data:
        for number2 in data:
            if number + number2 < 2020:  # Saves a lot of looping
                for number3 in data:
                    if number + number2 + number3 == 2020:
                        return number * number2 * number3


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
