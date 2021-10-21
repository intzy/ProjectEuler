"""
Problem 155 of Project Euler.

https://projecteuler.net/problem=155
"""

from functools import reduce
from itertools import product
from math import gcd


def problem155(n=18):
    capacitance = [set() for _ in range(n + 1)]
    capacitance[1].add((60, 1))
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            k = i - j
            for c1, c2 in product(capacitance[j], capacitance[k]):
                capacitance[i].add(capacitance_in_parallel(c1, c2))
                capacitance[i].add(capacitance_in_series(c1, c2))
    return len(reduce(set.union, capacitance))


def capacitance_in_parallel(c1, c2):
    p, q = c1
    r, s = c2
    x = p * s + q * r
    y = q * s
    g = gcd(x, y)
    return (x // g, y // g)


def capacitance_in_series(c1, c2):
    p, q = c1
    r, s = c2
    x = p * r
    y = q * r + p * s
    g = gcd(x, y)
    return (x // g, y // g)
