"""
Problem 027 of Project Euler.

https://projecteuler.net/problem=027
"""

from itertools import count

from lib.euler_lib import is_prime, list_primes


def problem027(limit=1_000):
    """
    The quadratic n^2 + an + b can only produce a chain of b primes (let n = b).
    Also b must be prime (let n = 0).
    A downward search on this reduced subspace with the terminating condition
    solves it fast enough.
    """
    primes = list_primes(limit + 1)
    max_seq, max_a, max_b = 0, None, None
    for b in reversed(primes):
        if max_seq >= b:
            return max_a * max_b
        for a in range(-limit + 1, limit, 2):
            seq = prime_generator_quadratric(a, b)
            if seq > max_seq:
                max_seq, max_a, max_b = seq, a, b
    return max_a * max_b


def prime_generator_quadratric(a, b):
    for n in count(1):
        y = n ** 2 + a * n + b
        if not is_prime(y):
            return n - 1
    return None
