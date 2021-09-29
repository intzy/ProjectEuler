"""
Problem 037 of Project Euler.

https://projecteuler.net/problem=037
"""

from itertools import count, product

from lib.euler_lib import is_prime


def problem037():
    return sum(list(filter(is_left_truncatable, get_right_truncatables())))


def get_right_truncatables():
    rt = []
    rt.append({2, 3, 5, 7})
    digits = [1, 3, 7, 9]
    for i in count(1):
        rt.append(
            {10 * p + d for d, p in product(digits, rt[i - 1]) if is_prime(10 * p + d)}
        )
        if not rt[i]:
            break
    return set().union(*rt[1:])


def is_left_truncatable(n):
    truncations = [int(str(n)[i:]) for i in range(1, len(str(n)))]
    return all(is_prime(x) for x in truncations)
