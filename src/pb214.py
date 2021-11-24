"""
Problem 214 of Project Euler.

https://projecteuler.net/problem=214
"""

from functools import cache

from lib.number_theory import list_totients
from lib.primes import list_primes


def problem214(limit=4 * 10 ** 7, length=25):
    phi = list_totients(limit // 2)
    primes = list_primes(limit)

    @cache
    def cycle_length(n):
        if n == 1:
            return 1
        return 1 + cycle_length(phi[n])

    def phiphi(p):
        return phi[(p - 1) // 2] * (2 if p % 4 == 1 else 1)

    return sum(p for p in primes[1:] if cycle_length(phiphi(p)) == length - 2)
