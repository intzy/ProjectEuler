"""
Problem 346 of Project Euler.

https://projecteuler.net/problem=346

Every number n > 2 is a repunit 11 in base n - 1.
Therefore, it suffices to find the sum of repunits 111 in any base
b < sqrt(limit).
"""

from math import isqrt, log


def problem346(limit=10 ** 12):
    strong_repunits = {1}
    for n in range(2, isqrt(limit)):
        for k in range(3, int(log((n - 1) * limit + 1, n) + 1)):
            strong_repunits.add((n ** k - 1) // (n - 1))
    return sum(strong_repunits)
