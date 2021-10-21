"""
Problem 112 of Project Euler.

https://projecteuler.net/problem=112
"""

from itertools import count


def problem112(p=0.99):
    n = 100
    bouncy_number_count = 0
    for n in count(101):
        if is_bouncy(n):
            bouncy_number_count += 1
        if bouncy_number_count >= n * p:
            return n
    return None


def is_increasing(n):
    last_digit = n % 10
    n = n // 10
    while n > 0:
        if n % 10 > last_digit:
            return False
        last_digit = n % 10
        n = n // 10
    return True


def is_decreasing(n):
    last_digit = n % 10
    n = n // 10
    while n > 0:
        if n % 10 < last_digit:
            return False
        last_digit = n % 10
        n = n // 10
    return True


def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)
