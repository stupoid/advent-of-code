import os
import sys
from typing import Iterable


def follow_instructions(instructions: Iterable[str]) -> int:
    d = {"(": 0, ")": 0}
    for i in instructions:
        d[i] += 1
    return d["("] - d[")"]


assert follow_instructions("(())") == 0
assert follow_instructions("()()") == 0
assert follow_instructions("(((") == 3
assert follow_instructions("(()(()(") == 3
assert follow_instructions("))(((((") == 3
assert follow_instructions("())") == -1
assert follow_instructions("))(") == -1
assert follow_instructions(")))") == -3
assert follow_instructions(")())())") == -3

input_path = os.path.join(sys.path[0], "input.txt")

solution_1 = follow_instructions(open(input_path).read())
print(solution_1)


# part 2
def find_position(instructions: Iterable[str], target: int = -1) -> int:
    floor = 0
    for position, i in enumerate(instructions):
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        if floor == target:
            return position + 1
    return floor


assert find_position(")") == 1
assert find_position("()())") == 5

solution_2 = find_position(open(input_path).read())
print(solution_2)
