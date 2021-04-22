import os
import sys


def calculate_wrapping_paper(dimensions: str) -> int:
    l, w, h = (int(x) for x in dimensions.split("x"))
    sides = [l * w, w * h, h * l]
    surface_area = sum((2 * s for s in sides))
    slack = min(sides)
    return surface_area + slack


assert calculate_wrapping_paper("2x3x4") == 58
assert calculate_wrapping_paper("1x1x10") == 43

input_path = os.path.join(sys.path[0], "input.txt")
solution_1 = sum(calculate_wrapping_paper(x) for x in open(input_path))
print(solution_1)


def calculate_ribbon(dimensions: str) -> int:
    l, w, h = sorted([int(x) for x in dimensions.split("x")])
    smallest_perimeter = l + l + w + w
    volume = l * w * h
    return smallest_perimeter + volume


assert calculate_ribbon("2x3x4") == 34
assert calculate_ribbon("1x1x10") == 14

solution_2 = sum(calculate_ribbon(x) for x in open(input_path))
print(solution_2)
