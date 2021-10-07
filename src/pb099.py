"""
Problem 099 of Project Euler.

https://projecteuler.net/problem=099
"""

from math import log


def problem099(filename="txt/pb099.txt"):
    """
    Calculate a*log(b) instead of b^a.
    """
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()

    base_exponent_pairs = []
    for string in strings:
        (base, exponenet) = string.split(",")
        base_exponent_pairs.append((int(base), int(exponenet)))

    return 1 + max((a * log(b), i) for i, (b, a) in enumerate(base_exponent_pairs))[1]
