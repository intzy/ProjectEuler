"""
Problem 128 of Project Euler.

https://projecteuler.net/problem=128
"""

from itertools import count, islice

from lib.primes import is_prime


def problem128(num=2000):
    return next(islice(generate(), num, None))


def generate():
    yield 1
    yield 2
    yield 4
    n = 2
    for r in count(2):
        n += 6 * (r - 1)

        diff = [6 * r - 1, 6 * r + 1, 6 * r + 6 * (r + 1) - 1]
        if all(is_prime(x) for x in diff):
            yield n

        diff = [6 * r - 1, 12 * r - 7, 6 * (r + 1) - 1]
        if all(is_prime(x) for x in diff):
            yield n + 6 * r - 1
