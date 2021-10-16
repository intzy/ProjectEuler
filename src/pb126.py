"""
Problem 126 of Project Euler.

https://projecteuler.net/problem=126
"""

from itertools import count


def problem126(y=1000):
    limit = 40000
    C = [0] * limit
    for a in count(1):
        if num_cubes(a, a, a, 1) >= limit:
            break
        for b in count(a):
            if num_cubes(a, b, b, 1) >= limit:
                break
            for c in count(b):
                if num_cubes(a, b, c, 1) >= limit:
                    break
                for i in count(1):
                    n = num_cubes(a, b, c, i)
                    if n >= limit:
                        break
                    C[n] += 1
    return min((n for n in range(limit) if C[n] == y))


def num_cubes(a, b, c, layer):
    u = 2 * (a * b + b * c + c * a)
    v = 4 * (a + b + c)
    return u + (layer - 1) * v + 4 * (layer - 1) * (layer - 2)
