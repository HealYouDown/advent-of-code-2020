from collections import defaultdict
from utils import timer


def get_input_data():
    with open("inputs/day06.txt", "r") as fp:
        return fp.read().split("\n\n")


@timer
def puzzle_1():
    count = 0

    for group in get_input_data():
        group = group.replace("\n", "")
        count += len(set(group))

    return count


@timer
def puzzle_2():
    count = 0

    for group in get_input_data():
        group_member_count = len(group.splitlines())
        group_counter = defaultdict(int)
        for member_answers in group.splitlines():
            for char in member_answers:
                group_counter[char] += 1

        for char, answer_count in group_counter.items():
            if answer_count == group_member_count:
                count += 1

    return count


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
