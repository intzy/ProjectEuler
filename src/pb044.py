"""
Problem 044 of Project Euler.

https://projecteuler.net/problem=044
"""

from itertools import count
from math import isqrt

from lib.euler_lib import is_pentagonal


def problem044():
    """
    Suppose Pn - Pm = Pd = D/2.
    Then d(3d - 1) = n(3n - 1) - m(3m - 1) = (n - m)(3n + 3m - 1) = xy,
    where x = n - m and y = 3n + 3m - 1.
    One can then prove n = (3x + y + 1) / 6, and m = n - x.
    Then suffices to check Pn + Pm is pentagonal.
    """
    for d in count(1):
        D = d * (3 * d - 1)
        for x in range(1, isqrt(D)):
            if D % x != 0:
                continue
            y = D // x
            n = 3 * x + y + 1
            if n % 6 != 0:
                continue
            n //= 6
            m = n - x
            Pn = n * (3 * n - 1) // 2
            Pm = m * (3 * m - 1) // 2
            if m > 0 and is_pentagonal(Pn + Pm):
                return D // 2
