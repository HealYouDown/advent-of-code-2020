import typing
import re
from utils import timer


class Instruction:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"<Instruction {repr(self.name)} {repr(self.value)}>"


class ProgrammCycle:
    def __init__(self):
        self._instructions: typing.List[Instruction] = []
        self._run_instructions: typing.List[Instruction] = []
        self._accumulator: int = 0
        self._instruction_index = 0

        self.load_instructions()

    @property
    def accumulator_value(self) -> int:
        return self._accumulator

    def reset(self) -> None:
        self._run_instructions: typing.List[Instruction] = []
        self._accumulator: int = 0
        self._instruction_index = 0

    def load_instructions(self) -> None:
        with open("inputs/day08.txt", "r") as fp:
            for line in fp.readlines():
                match = re.match(r"(.{3}) (.*)", line)
                self._instructions.append(Instruction(
                    name=match.group(1), value=int(match.group(2))
                ))

    def run(self) -> None:
        while True:
            instruction = self._instructions[self._instruction_index]
            # Check if instruction has already be run
            if instruction in self._run_instructions:
                break

            if instruction.name == "nop":
                self._instruction_index += 1

            elif instruction.name == "acc":
                self._accumulator += instruction.value
                self._instruction_index += 1

            elif instruction.name == "jmp":
                self._instruction_index += instruction.value

            self._run_instructions.append(instruction)

    def run2(self) -> None:
        for corrupt_instruction in filter(lambda i: i.name in ["jmp", "nop"],
                                          self._instructions):
            self.reset()

            while True:
                if self._instruction_index == len(self._instructions):
                    # Return ends the function
                    return

                instruction = self._instructions[self._instruction_index]

                if corrupt_instruction == instruction:
                    if instruction.name == "jmp":
                        instruction_name = "nop"
                    elif instruction.name == "nop":
                        instruction_name = "jmp"
                else:
                    instruction_name = instruction.name

                # Check if instruction has already be run
                if instruction in self._run_instructions:
                    break

                if instruction_name == "nop":
                    self._instruction_index += 1

                elif instruction_name == "acc":
                    self._accumulator += instruction.value
                    self._instruction_index += 1

                elif instruction_name == "jmp":
                    self._instruction_index += instruction.value

                self._run_instructions.append(instruction)


@timer
def puzzle_1():
    program = ProgrammCycle()
    program.run()
    return program.accumulator_value


@timer
def puzzle_2():
    program = ProgrammCycle()
    program.run2()
    return program.accumulator_value


if __name__ == "__main__":
    print(puzzle_1())
    print(puzzle_2())
