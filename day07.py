import re
import typing
from utils import timer


def get_bags() -> typing.Dict[str, typing.List[dict]]:
    bags = {}

    with open("inputs/day07.txt", "r") as fp:
        for line in fp.readlines():
            # Bag without any other bags in it
            # 'dotted black bags contain no other bags.'
            if match := re.match(r"^(.*) bags contain no other bags.$", line):
                bags[match.group(1)] = []

            else:
                line_split = re.sub(r"(\.|\,)", "", line).split(" ")

                color = " ".join(line_split[:2])

                children_line = " ".join(line_split[4:])
                children = []
                for (num, c_color) in re.findall(r"(\d) (\w* \w*)",
                                                 children_line):
                    children.append({
                        "amount": int(num),
                        "color": c_color,
                    })

                bags[color] = children

    return bags


@timer
def puzzle_1():
    def get_parent_colors(bags, bag_color: str):
        """
        Goes tree up from children to last parent.
        """
        colors = set()

        for parent, children in bags.items():
            for child in children:
                if child["color"] == bag_color:
                    colors.add(parent)
                    colors.update(get_parent_colors(bags, parent))

        return colors

    return len(get_parent_colors(get_bags(),
                                 "shiny gold"))


@timer
def puzzle_2():
    def get_children_amounts(bags, parent_color: str):
        nums = []

        for child in bags[parent_color]:
            nums.append(child["amount"])
            nums.append(
                child["amount"] * sum(get_children_amounts(bags,
                                                           child["color"]))
            )

        return nums

    return sum(get_children_amounts(get_bags(), "shiny gold"))


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
