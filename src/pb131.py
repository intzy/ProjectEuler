"""
Problem 131 of Project Euler.

https://projecteuler.net/problem=131
"""

from math import isqrt

from lib.euler_lib import is_prime


def problem131(limit=1000000):
    """
    The prime p is in a prime-cube partnership with n
    if p is the consecutive difference of cubes m^3 - (m - 1)^3,
    in which case n = (m - 1)^3.
    """
    stop = int(2 + isqrt(9 - 12 * (1 - limit)) / 6)
    return sum(1 for m in range(2, stop) if is_prime(3 * m * m - 3 * m + 1))
