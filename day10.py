import typing

from utils import timer


def get_input_data() -> typing.List[int]:
    with open("inputs/day10.txt", "r") as fp:
        return [int(line) for line in fp.readlines()]


@timer
def puzzle_1():
    adapters = sorted(get_input_data())
    diffs = []

    # Add the power outlet to adapters
    adapters.insert(0, 0)
    # Add our device with max + 3 to the adapter list
    adapters.append(max(adapters)+3)

    for index, adapter in enumerate(adapters):
        if (index+1) == len(adapters):
            break

        diffs.append(adapters[index+1] - adapter)

    return diffs.count(1) * diffs.count(3)


def puzzle_2():
    pass


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
