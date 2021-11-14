"""
Problem 243 of Project Euler.

https://projecteuler.net/problem=243

The answer is the smallest n for which phi(n) / (n - 1) < a / b.
"""

from math import ceil, prod

from lib.primes import list_primes


def problem243(a=15499, b=94744):
    primes = list_primes(100)
    totient = 1
    i = 0
    for i, p in enumerate(primes):
        totient *= 1 - 1 / p
        if totient < a / b:
            break
    else:
        raise ValueError("Ratio too small")
    n = prod(primes[: i + 1])
    x = ceil(a / (n * (a - b * totient)))
    return n * x
