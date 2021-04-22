import os
import sys


def is_nice(string: str):
    vowel_count = 0
    twice = False
    vowels = {"a", "e", "i", "o", "u"}

    for i in range(len(string) - 1):
        c = string[i]
        n = string[i + 1]

        if c == n:
            twice = True

        if c in vowels:
            vowel_count += 1

        if c + n in ["ab", "cd", "pq", "xy"]:
            return False

    if string[-1] in vowels:
        vowel_count += 1

    if vowel_count >= 3 and twice:
        return True
    else:
        return False


assert is_nice("ugknbfddgicrmopn")
assert is_nice("aaa")
assert not is_nice("jchzalrnumimnmhp")
assert not is_nice("haegwjzuvuyypxyu")
assert not is_nice("dvszwmarrgswjxmb")


input_path = os.path.join(sys.path[0], "input.txt")
solution_1 = sum(is_nice(x) for x in open(input_path))
print(solution_1)
