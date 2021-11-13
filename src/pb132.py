"""
Problem 132 of Project Euler.

https://projecteuler.net/problem=132
"""

from math import gcd

from lib.primes import list_primes


def problem132(n=10 ** 9, num=40):
    limit = 1024
    i = 3
    prime_factors = []
    while limit < n:
        primes = list_primes(min(limit, n))[i:]
        i += len(primes)
        for p in primes:
            if pow(10, gcd(n, p - 1), p) - 1:
                continue
            prime_factors.append(p)
            if len(prime_factors) == num:
                return sum(prime_factors)
        limit *= 4
    return None
