"""
Problem 050 of Project Euler.

https://projecteuler.net/problem=050
"""

from lib.primes import list_primes


# Uniqueness not proven.
def problem050(limit=1000000):
    primes = list_primes(limit)
    prime_set = set(primes)

    start = next(i for i in range(1, len(primes) + 1) if sum(primes[:i]) > limit)

    for length in range(start, 0, -1):
        for i in range(len(primes) - length + 1):
            n = sum(primes[i : i + length])
            if n > limit:
                break
            if n in prime_set:
                return n

    return None
