"""
Problem 126 of Project Euler.

https://projecteuler.net/problem=126
"""

from itertools import count
from math import ceil, isqrt


def problem126(y=1000):
    def solve(limit):
        C = [0] * limit
        for a in range(1, ceil(isqrt(limit // 6))):
            for b in range(a, ceil(-a + isqrt(4 * a * a + 2 * limit) // 2)):
                for c in range(b, ceil((limit - 2 * a * b) // (2 * (a + b)))):
                    u = 2 * (a * b + b * c + c * a)
                    v = 4 * (a + b + c)
                    for layer in count(1):
                        n = u + (layer - 1) * v + 4 * (layer - 1) * (layer - 2)
                        if n >= limit:
                            break
                        C[n] += 1
        return min((n for n in range(limit) if C[n] == y), default=None)

    limit = 10 * y
    while True:
        soln = solve(limit)
        if soln is not None:
            return soln
        limit *= 2
