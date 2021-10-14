"""
Problem 124 of Project Euler.

https://projecteuler.net/problem=124
"""

from lib.euler_lib import list_primes


def problem124(limit=100000, t=10000):
    primes = list_primes(limit)
    rad = [1] * (limit + 1)
    for p in primes:
        for n in range(p, limit + 1, p):
            rad[n] *= p
    E = sorted(list(range(1, limit + 1)), key=lambda n: rad[n])
    return E[t - 1]
