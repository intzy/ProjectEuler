"""
Problem 040 of Project Euler.

https://projecteuler.net/problem=040
"""

from math import prod


def problem040(power_limit=7):
    champernowne = ""
    i = 1
    while len(champernowne) < 10 ** power_limit:
        champernowne += str(i)
        i += 1
    return prod([int(champernowne[10 ** i - 1]) for i in range(power_limit)])
