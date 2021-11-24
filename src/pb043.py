"""
Problem 043 of Project Euler.

https://projecteuler.net/problem=043
"""

from itertools import permutations

from lib.misc import concat_ints

DIVISORS = [1, 2, 3, 5, 7, 11, 13, 17]


def problem043():
    pandigitals = []
    for digits in permutations(range(10)):
        for i in reversed(range(len(DIVISORS))):
            num = 100 * digits[i] + 10 * digits[i + 1] + digits[i + 2]
            if num % DIVISORS[i] != 0:
                break
        else:
            pandigitals.append(concat_ints(*digits))
    return sum(pandigitals)
