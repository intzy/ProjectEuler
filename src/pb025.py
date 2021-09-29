"""
Problem 025 of Project Euler.

https://projecteuler.net/problem=025
"""

from math import ceil, log10, sqrt


def problem025(num_digits=1000):
    """
    Recall that F_n = floor(phi^n / sqrt(5) + 1/2).  Take the inverse and log10.
    """
    phi = (1 + sqrt(5)) / 2
    return ceil((num_digits - 1 + 0.5 * log10(5)) / log10(phi))
