"""
Problem 119 of Project Euler.

https://projecteuler.net/problem=119
"""

from itertools import count
from math import ceil, log10

from lib.euler_lib import digit_sum


def problem119(n=30):
    terms = set()
    for length in count(2):
        if len(terms) >= n:
            return sorted(list(terms))[n - 1]
        for base in range(2, 9 * length + 1):
            for k in range(
                ceil((length - 1) / log10(base)),
                int((length) // log10(base)) + 1,
            ):
                a = base ** k
                if digit_sum(a) == base:
                    terms.add(a)
