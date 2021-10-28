"""
Problem 138 of Project Euler.

https://projecteuler.net/problem=138
"""

from itertools import count
from math import inf, isqrt, sqrt

from lib.euler_lib import is_square


def problem138():
    tally = 0
    summ = 0
    for v in count(1):
        if is_square(5 * v * v + 1):
            u = 2 * v + isqrt(5 * v * v + 1)
            b = 4 * u * v
            h = u * u - v * v
            L = u * u + v * v
            print(b, h, L)
            print("a")
            summ += L
            tally += 1
            if tally == 12:
                return summ
        if is_square(5 * v * v - 1):
            u = 2 * v + isqrt(5 * v * v - 1)
            b = 4 * u * v
            h = u * u - v * v
            L = u * u + v * v
            print(b, h, L)
            print("b")
            summ += L
            tally += 1
            if tally == 12:
                return summ
