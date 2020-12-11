import numpy as np

from utils import timer


def get_input_data() -> np.ndarray:
    with open("inputs/day11.txt", "r") as fp:
        return np.array([list(line.strip())
                         for line in fp.readlines()])


def get_adjacent_seats_count(
    grid: np.ndarray,
    x: int,
    y: int,
    char: str
) -> int:
    y_start = y - 1 if (y - 1) > 0 else 0
    y_end = y + 2 if (y + 2) < len(grid) else len(grid) + 1

    x_start = x - 1 if (x - 1) > 0 else 0
    x_end = x + 2 if (x + 2) < len(grid[0]) else len(grid[0]) + 1

    section = grid[y_start:y_end, x_start:x_end]
    section

    count = (section == char).sum()
    # Remove current seat from count if chars match
    if grid[y, x] == char:
        count -= 1

    return count


@timer
def puzzle_1():
    grid = get_input_data()

    while True:
        new_grid = grid.copy()

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                current_seat = grid[y, x]

                # Empty seat
                if current_seat == "L":
                    count = get_adjacent_seats_count(grid, x, y, "#")
                    if count == 0:
                        new_grid[y, x] = "#"

                elif current_seat == "#":
                    count = get_adjacent_seats_count(grid, x, y, "#")
                    if count >= 4:
                        new_grid[y, x] = "L"

        # If nothing was changed, return the amount of occupied seats
        if np.array_equal(grid, new_grid):
            return (grid == "#").sum()
        else:
            # Run again with updated grid
            grid = new_grid


def puzzle_2():
    grid = get_input_data()

    while True:
        new_grid = grid.copy()

        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                current_seat = grid[y, x]
                can_see_fields = []

                # I am way to lazy to abstract that into a function..

                # top
                for y_i in range(y, 0, -1):
                    if grid[y_i, x] != ".":
                        can_see_fields.append(grid[y_i, x])
                        break

                # top right
                try:
                    x_i = x + 1
                    for y_i in range(y-1, 0, -1):
                        if grid[y_i, x_i] != ".":
                            can_see_fields.append(grid[y_i, x_i])
                            break
                        else:
                            x_i += 1
                except IndexError:
                    pass

                # right
                try:
                    for x_i in range(x, len(grid[0]), 1):
                        if grid[y, x_i] != ".":
                            can_see_fields.append(grid[y, x_i])
                            break
                except IndexError:
                    pass

                # bottom right
                try:
                    x_i = x + 1
                    for y_i in range(y+1, len(grid), 1):
                        if grid[y_i, x_i] != ".":
                            can_see_fields.append(grid[y_i, x_i])
                            break
                        else:
                            x_i += 1
                except IndexError:
                    pass

                # bottom
                try:
                    for y_i in range(y, len(grid), 1):
                        if grid[y_i, x] != ".":
                            can_see_fields.append(grid[y_i, x])
                            break
                except IndexError:
                    pass

                # bottom left
                try:
                    x_i = x - 1
                    for y_i in range(y+1, len(grid), -1):
                        if grid[y_i, x_i] != ".":
                            can_see_fields.append(grid[y_i, x_i])
                            break
                        else:
                            x_i -= 1
                except IndexError:
                    pass

                # left
                try:
                    for x_i in range(x, len(grid[0]), -1):
                        if grid[y, x_i] != ".":
                            can_see_fields.append(grid[y, x_i])
                            break
                except IndexError:
                    pass

                # top left
                try:
                    x_i = x - 1
                    for y_i in range(y-1, 0, -1):
                        if grid[y_i, x_i] != ".":
                            can_see_fields.append(grid[y_i, x_i])
                            break
                        else:
                            x_i -= 1
                except IndexError:
                    pass

                if current_seat == "L":
                    if can_see_fields.count("#") == 0:
                        new_grid[y, x] = "#"

                elif current_seat == "#":
                    if can_see_fields.count("#") >= 5:
                        new_grid[y, x] = "L"

        # If nothing was changed, return the amount of occupied seats
        if np.array_equal(grid, new_grid):
            return (grid == "#").sum()
        else:
            # Run again with updated grid
            grid = new_grid
            print(grid)


if __name__ == "__main__":
    print(puzzle_1())
    # DOES NOT WORK print(puzzle_2())
