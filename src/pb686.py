"""
Problem 686 of Project Euler.

https://projecteuler.net/problem=686
"""

from itertools import count
from math import log10


def problem686(L=123, n=678910):
    log2 = log10(2)
    lower = log10(L / 100)
    upper = log10((L + 1) / 100)
    tally = 0
    for j in count(1):
        x = j * log2 % 1
        if lower <= x < upper:
            tally += 1
            if tally == n:
                return j
