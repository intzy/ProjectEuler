"""
Problem 016 of Project Euler.

https://projecteuler.net/problem=016
"""


def problem016(exp=1000):
    return sum(int(digit) for digit in str(2 ** exp))
