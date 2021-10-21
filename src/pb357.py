"""
Problem 357 of Project Euler.

https://projecteuler.net/problem=357
"""

from math import isqrt

from lib.euler_lib import list_primes


def problem357(limit=10 ** 8):
    primes = list_primes(limit + 2)
    prime_set = set(primes)

    summation = 0
    for p in primes:
        n = p - 1
        if all(n % d != 0 or d + n // d in prime_set for d in range(2, isqrt(n) + 1)):
            summation += n
    return summation
