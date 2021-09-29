"""
Problem 003 of Project Euler.

https://projecteuler.net/problem=003
"""

from itertools import count


def problem003(n=600_851_475_143):
    for m in count(2):
        if m >= n:
            return n
        while n % m == 0:
            n //= m
