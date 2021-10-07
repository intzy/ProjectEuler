"""
Problem 091 of Project Euler.

https://projecteuler.net/problem=091
"""

from itertools import product


def problem091(n=50):
    """
    Brute force.  (There are more clever and faster solutions than mine.)
    """
    count = 0
    for x1, y1, x2, y2 in product(range(n + 1), repeat=4):
        # Check angle to prevent double counting.
        if x1 * y2 >= x2 * y1:
            continue
        a = x1 * x1 + y1 * y1
        b = x2 * x2 + y2 * y2
        c = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
        if a == b + c or b == a + c or c == a + b:
            count += 1
    return count
