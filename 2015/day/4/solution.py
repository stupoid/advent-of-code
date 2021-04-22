import hashlib


def mine(key: str, target: str) -> int:
    upper_bound = 1_000_000_000

    for i in range(upper_bound):
        if hashlib.md5(f"{key}{i}".encode("utf-8")).hexdigest().startswith(target):
            return i

    raise Exception(f"Reached upper bound of {upper_bound}")


assert mine("abcdef", "00000") == 609043
assert mine("pqrstuv", "00000") == 1048970

solution_1 = mine("ckczppom", "00000")
print(solution_1)

solution_2 = mine("ckczppom", "000000")
print(solution_2)
