import os
import sys
from typing import List, Set, Tuple


def move(pos: Tuple[int, int], direction: str) -> Tuple[int, int]:
    if direction == "^":
        return (pos[0] + 1, pos[1])
    elif direction == "v":
        return (pos[0] - 1, pos[1])
    elif direction == ">":
        return (pos[0], pos[1] + 1)
    elif direction == "<":
        return (pos[0], pos[1] - 1)
    else:
        return pos


def deliver(directions: str) -> Set[Tuple[int, int]]:
    pos = (0, 0)
    houses: Set[Tuple[int, int]] = {pos}
    for i in directions:
        pos = move(pos, i)
        houses.add(pos)

    return houses


assert len(deliver(">")) == 2
assert len(deliver("^>v<")) == 4
assert len(deliver("^v^v^v^v^v")) == 2

input_path = os.path.join(sys.path[0], "input.txt")
solution_1 = len(deliver(open(input_path).read()))
print(solution_1)


def deliver_w_robo(directions: str) -> Set[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = [(0, 0), (0, 0)]
    houses: Set[Tuple[int, int]] = {*positions}
    for i, direction in enumerate(directions):
        idx = i % len(positions)
        positions[idx] = move(positions[idx], direction)
        houses.add(positions[idx])

    return houses


assert len(deliver_w_robo("^v")) == 3
assert len(deliver_w_robo("^>v<")) == 3
assert len(deliver_w_robo("^v^v^v^v^v")) == 11

solution_2 = len(deliver_w_robo(open(input_path).read()))
print(solution_2)
