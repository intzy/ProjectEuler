"""
Problem 068 of Project Euler.

https://projecteuler.net/problem=068
"""

from itertools import combinations
from itertools import permutations as perm
from itertools import product


def problem068():
    inner_outer_pairs = get_possible_inner_outer_pairs()

    return max(
        [
            magic_5gon(list(inner), [outer_circle[0]] + list(outer), total)
            for inner_circle, outer_circle, total in inner_outer_pairs
            for inner, outer in product(perm(inner_circle), perm(outer_circle[1:]))
            if magic_5gon(list(inner), [outer_circle[0]] + list(outer), total)
            is not None
        ]
    )


def get_possible_inner_outer_pairs():
    inner_outer_pairs = []
    digits = set(range(1, 10))
    for inner_circle in combinations(range(1, 10), r=5):
        outer_circle = sorted(digits - set(inner_circle))
        inner_circle = sorted(inner_circle)
        total = 10 + sum(outer_circle) + 2 * sum(inner_circle)
        if total % 5 == 0 and 10 + inner_circle[0] + inner_circle[1] <= total // 5:
            inner_outer_pairs.append((inner_circle, outer_circle + [10], total // 5))
    return inner_outer_pairs


def magic_5gon(inner, outer, total):
    if all(outer[i] + inner[i] + inner[(i + 1) % 5] == total for i in range(5)):
        x = str(outer[0]) + str(inner[0]) + str(inner[1])
        x += str(outer[1]) + str(inner[1]) + str(inner[2])
        x += str(outer[2]) + str(inner[2]) + str(inner[3])
        x += str(outer[3]) + str(inner[3]) + str(inner[4])
        x += str(outer[4]) + str(inner[4]) + str(inner[0])
        return int(x)
    return None
