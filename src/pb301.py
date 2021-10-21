"""
Problem 301 of Project Euler.

https://projecteuler.net/problem=301

You are in a losing position if and only if n XOR 2n XOR 3n == 0.
This is equivalent to n & 2 * n == 0,
or n not having consecutive zeros in its binary expansion.
From this, you can prove that it is the (power_of_2 + 2)'th Fibonacci number.
"""

from math import sqrt


def problem301(power_of_2=30):
    phi = (1 + sqrt(5)) / 2
    return int(phi ** (power_of_2 + 2) / sqrt(5) + 1 / 2)
