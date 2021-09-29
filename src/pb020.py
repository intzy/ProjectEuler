"""
Problem 020 of Project Euler.

https://projecteuler.net/problem=020
"""

from math import factorial


def problem020(n=100):
    return sum(int(x) for x in str(factorial(n)))
