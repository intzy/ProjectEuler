"""
Problem 041 of Project Euler.

https://projecteuler.net/problem=041
"""

from lib.primes import list_primes


def problem041():
    primes = list_primes(7_654_321)
    for prime in reversed(primes):
        if is_pandigital(prime):
            return prime
    return None


def is_pandigital(n):
    n = str(n)
    for d in range(1, len(n) + 1):
        if str(d) not in n:
            return False
    return True
