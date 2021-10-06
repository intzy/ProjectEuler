"""
Problem 103 of Project Euler.

https://projecteuler.net/problem=103
"""

from itertools import combinations

from lib.euler_iterables import nonempty_subsets


# TODO optimize and make correct
def problem103():
    A = min(
        (A for A in combinations(range(1, 50), 7) if is_special_sum_set(list(A))),
        key=sum,
    )
    return "".join(str(k) for k in A)


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
