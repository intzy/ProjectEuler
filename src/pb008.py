"""
Problem 008 of Project Euler.

https://projecteuler.net/problem=008
"""

from math import prod


def problem008(length=13, filename="txt/pb008.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        string = f.read().replace("\n", "")
    digits = [int(x) for x in string]

    return max(prod(digits[i - length : i]) for i in range(length, len(digits) + 1))
