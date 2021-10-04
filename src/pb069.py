"""
Problem 069 of Project Euler.

https://projecteuler.net/problem=069
"""

from lib.euler_lib import list_primes


def problem069(bound=1_000_000):
    """
    Recall that phi(n) = n * prod(1 - 1 / p for p in primes dividing n).
    Therefore, n / phi(n) = prod(p / (p - 1) for p in primes dividing n)...
    """
    primes = list_primes(100)  # 100 should suffice for any bound below 10^30
    n = 1
    for p in primes:
        if n * p > bound:
            return n
        n *= p
    raise ValueError("Input to problem 069 too large")
