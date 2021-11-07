"""
Problem 203 of Project Euler.

https://projecteuler.net/problem=203
"""

from math import comb, isqrt

from lib.euler_lib import list_primes


def problem203(rows=51):
    primes = list_primes(isqrt(comb(rows - 1, (rows - 1) // 2)) + 1)

    squarefree = set([1])
    for n in range(rows):
        for k in range(1, n):
            x = comb(n, k)
            is_square_free = True
            for p in primes:
                if p * p > x:
                    break
                if not x % (p * p):
                    is_square_free = False
                    break
            if is_square_free:
                squarefree.add(x)

    return sum(squarefree)
