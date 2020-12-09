import math
from utils import timer


def get_input_data():
    with open("inputs/day03.txt", "r") as fp:
        rows = [list(row.rstrip()) for row in fp.readlines()]

    # Rows have to be 3 (puzzle 1) and 7 times (puzzle 2) times as
    # width as height
    h = len(rows)
    w = len(rows[0])

    extend_factor = math.ceil((h*7) / w)

    extended_rows = [row*extend_factor for row in rows]

    return extended_rows


@timer
def puzzle_1(field):
    visited_fields = []

    x = 0
    # y goes from 0 all the way down to the maximum
    for y in range(0, len(field)):
        char = field[y][x]
        visited_fields.append(char)

        x += 3

    # . = Open Square, # = Tree
    return visited_fields.count("#")


@timer
def puzzle_2(field):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    slopes_trees = []

    for x_increment, y_increment in slopes:
        x = 0
        visited_fields = []

        # y goes from 0 all the way down to the maximum
        for y in range(0, len(field), y_increment):
            char = field[y][x]
            visited_fields.append(char)

            x += x_increment

        slopes_trees.append(visited_fields.count("#"))

    # . = Open Square, # = Tree
    return math.prod(slopes_trees)


if __name__ == "__main__":
    field = get_input_data()

    print(puzzle_1(field))
    print(puzzle_2(field))
