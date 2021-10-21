"""
Problem 121 of Project Euler.

https://projecteuler.net/problem=121
"""


from itertools import combinations
from math import factorial, prod


def problem121(turns=15):
    count = 1 + sum(
        prod(c)
        for n in range(1, (turns + 1) // 2)
        for c in combinations(range(1, turns + 1), n)
    )
    return factorial(turns + 1) // count
