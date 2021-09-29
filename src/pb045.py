"""
Problem 045 of Project Euler.

https://projecteuler.net/problem=045
"""


from lib.euler_lib import is_pentagonal


def problem045(count=3):
    n = 0
    while count > 0:
        n += 1
        hexg = n * (2 * n - 1)
        if is_pentagonal(hexg):
            count -= 1
    return hexg
