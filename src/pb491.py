"""
Problem 491 of Project Euler.

https://projecteuler.net/problem=491
"""

from itertools import combinations
from math import factorial, prod


def problem491():
    digits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    count = 0
    for even_pos_digits in set(combinations(digits, r=10)):
        if (2 * sum(even_pos_digits) - 90) % 11 != 0:
            continue
        denominator = prod(factorial(even_pos_digits.count(d)) for d in range(10))
        perms = factorial(10) // denominator
        count += perms * perms
    return 9 * count // 10
