"""
Problem 085 of Project Euler.

https://projecteuler.net/problem=085

The number of rectangles in a a*b grid is a * (a + 1) * b * (b + 1) // 4.
"""

from itertools import count
from math import ceil, floor, sqrt


def problem085(n=2_000_000):
    area = 0
    diff = n
    for a in count(1):
        b = (-1 + sqrt(1 + 16 * n / (a * (a + 1)))) / 2
        if b < 1:
            break
        for b in [floor(b), ceil(b)]:
            num_rectangles = a * (a + 1) * b * (b + 1) // 4
            if abs(num_rectangles - n) < diff:
                area = a * b
                diff = abs(num_rectangles - n)
    return area
