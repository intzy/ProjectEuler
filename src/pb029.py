"""
Problem 029 of Project Euler.

https://projecteuler.net/problem=029
"""


def problem029(bound=100):
    powers = set()
    for a in range(2, bound + 1):
        for b in range(2, bound + 1):
            powers.add(a ** b)
    return len(powers)
