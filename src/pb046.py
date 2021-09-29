"""
Problem 046 of Project Euler.

https://projecteuler.net/problem=046
"""

from itertools import count
from math import isqrt

from lib.euler_lib import is_prime


def problem046():
    primes = {2, 3, 5, 7}
    for n in count(9, 2):
        if is_prime(n):
            primes.add(n)
        elif all(n - (2 * m ** 2) not in primes for m in range(1, isqrt(n // 2) + 1)):
            return n
