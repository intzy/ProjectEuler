"""
Problem 351 of Project Euler.

https://projecteuler.net/problem=351

The solution is

    6 * ∑ (n - phi(n)) from 1 to N,

where phi is the euler-totient function.
"""

from functools import cache
from math import isqrt

from lib.euler_lib import list_totients, sum_to_n


def problem351(N=10 ** 8):
    totients = list_totients(10 ** 5)
    for i in range(2, len(totients)):
        totients[i] += totients[i - 1]

    @cache
    def S(n):
        if n < 10 ** 5:
            return totients[n]
        dmax = isqrt(n) if isqrt(n) == n // isqrt(n) else isqrt(n) + 1
        x = 0
        for d in range(2, isqrt(n) + 1):
            u = n // d
            x += S(u)
        for d in range(1, dmax):
            c = n // d - n // (d + 1)
            x += c * S(d)
        return sum_to_n(n) - x

    return 6 * (sum_to_n(N) - S(N))
