"""
Problem 010 of Project Euler.

https://projecteuler.net/problem=010
"""

from lib.euler_lib import list_primes


def problem010(limit=2_000_000):
    """
    Use the Sieve of Eratosthenes.
    """
    return sum(list_primes(limit))
