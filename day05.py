import typing
from utils import timer


def get_input_data():
    with open("inputs/day05.txt", "r") as fp:
        return [line for line in fp.readlines() if line]


def resolve_binary(
    string: str,
    lower_char: str,
    upper_char: str,
    max_: int
) -> int:
    current_min = 0
    current_max = max_ - 1

    for char in string:
        diff = current_max - current_min
        if char == lower_char:
            current_max -= int(diff / 2) + 1
        elif char == upper_char:
            current_min += int(diff / 2) + 1

    assert current_min == current_max

    return current_max


def get_seat_ids() -> typing.List[int]:
    seat_ids = []

    for line in get_input_data():
        row_string = line[0:7]
        col_string = line[7:]

        row = resolve_binary(row_string, "F", "B", 128)
        col = resolve_binary(col_string, "L", "R", 8)

        seat_id = row * 8 + col
        seat_ids.append(seat_id)

    return seat_ids


@timer
def puzzle_1():
    return max(get_seat_ids())


@timer
def puzzle_2():
    seat_ids = sorted(get_seat_ids())

    return set(range(seat_ids[0], seat_ids[-1]+1)).difference(set(seat_ids))


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
