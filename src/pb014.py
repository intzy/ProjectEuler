"""
Problem 014 of Project Euler.

https://projecteuler.net/problem=014
"""


def problem014(bound=1_000_000):
    """
    Use dynamic programming.
    """
    cache = {0: 0, 1: 1}
    for n in range(bound // 2, bound):
        collatz_length(n, cache)
    return max(cache, key=cache.get)


def collatz_length(n, cache):
    if n in cache:
        return cache[n]
    cache[n] = collatz_length(collatz(n), cache) + 1
    return cache[n]


def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1
