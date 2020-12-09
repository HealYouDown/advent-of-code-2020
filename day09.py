import collections
import typing
from utils import timer


def get_input_data() -> typing.List[int]:
    with open("inputs/day09.txt", "r") as fp:
        return [int(line) for line in fp.readlines()]


def get_sums(preamble: typing.Iterable[int]) -> typing.List[int]:
    sums = []

    for num1 in preamble:
        for num2 in preamble:
            if num1 != num2:
                sums.append(num1 + num2)

    return sums


@timer
def puzzle_1(maxlen=25) -> int:
    numbers = get_input_data()
    preamble = collections.deque(numbers[0:maxlen], maxlen=maxlen)

    for num in numbers[maxlen:]:
        # Check if any pair in the preamble can
        # be summed to the num.
        if num in get_sums(preamble):
            preamble.append(num)
        else:
            return num


@timer
def puzzle_2(invalid_num: int) -> int:
    numbers = get_input_data()

    for index, num in enumerate(numbers):
        numset = [num]
        counter = index

        while sum(numset) < invalid_num:
            counter += 1
            numset.append(numbers[counter])

        if sum(numset) == invalid_num:
            return min(numset) + max(numset)


if __name__ == "__main__":
    invalid_num = puzzle_1()
    print(invalid_num)
    print(puzzle_2(invalid_num))
