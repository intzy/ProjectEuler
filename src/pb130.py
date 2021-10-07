"""
Problem 130 of Project Euler.

https://projecteuler.net/problem=130
"""

from itertools import count, islice
from math import gcd

from lib.euler_lib import is_prime


def problem130(terms=25):
    return sum(islice((n for n in count(4) if check(n) and not (n - 1) % A(n)), terms))


def check(n):
    return not is_prime(n) and gcd(10, n) == 1


def A(n):
    c = 1
    x = 1
    while x:
        x = (10 * x + 1) % n
        c += 1
    return c
