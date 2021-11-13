"""
Problem 105 of Project Euler.

https://projecteuler.net/problem=105
"""

from lib.combinatorics import nonempty_subsets


def problem105(filename="txt/pb105.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()
        strings = [string.replace("\n", "").split(",") for string in strings]
        sets = [[int(n) for n in string] for string in strings]

    return sum(sum(A) for A in sets if is_special_sum_set(A))


def is_special_sum_set(A):
    A.sort()
    if sum(A[: len(A) // 2 + len(A) % 2]) < sum(A[len(A) // 2 + 1 :]):
        return False
    sums = set()
    for B in nonempty_subsets(A):
        if sum(B) in sums:
            return False
        sums.add(sum(B))
    return True
