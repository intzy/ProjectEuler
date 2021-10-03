"""
Problem 058 of Project Euler.

https://projecteuler.net/problem=058
"""

from itertools import count

from lib.euler_lib import is_prime


def problem058(ratio=0.1):
    n = 1
    prime_count = 0
    for spiral_size in count(2, 2):
        for _ in range(4):
            n += spiral_size
            if is_prime(n):
                prime_count += 1
        if prime_count < ratio * (2 * spiral_size + 1):
            return spiral_size + 1
