"""
Problem 007 of Project Euler.

https://projecteuler.net/problem=007
"""

from lib.primes import list_n_primes


def problem007(nth=10_001):
    """
    Use the Sieve of Eratosthenes.
    """
    return list_n_primes(nth)[nth - 1]
