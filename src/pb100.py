"""
Problem 100 of Project Euler.

https://projecteuler.net/problem=100

If b represents the number of blue balls and red represents the number of red balls,
then

    b(b-1)/((b + r)(b + r - 1)) = 1/2.

Solving for b yields

    b = (1 + 2r + sqrt(8r^2 + 1))/2.

Therefore, we require 8r^2 + 1 be an odd perfect square.
We use Pell's equation to solve x^2 - 8r^2 = 1.
"""

from itertools import count


def problem100(L=10 ** 12):
    x, r = 3, 1
    for _ in count():
        x, r = 3 * x + 8 * r, 3 * r + x
        total = 2 * r + (1 + x) // 2
        if x % 2 and total > L:
            return total - r
