"""
Problem 206 of Project Euler

https://projecteuler.net/problem=206

It is mainly a brute force method,
though one optimization was recognizing that the first underscore
in the number 1_2_3_4_5_6_7_8_9_0 must be 0
(its square root must be a multiple of 10, which means
its square must be a multiple of 100).
This reduces the search density by a factor of 10.
Further analysis shows that n / 10 is either 3 or 7 mod 10.

This algorithm also proves that the number is unique.
"""

from itertools import chain
from math import isqrt


def problem206():
    upper = isqrt(1_92_93_94_95_96_97_98_99_90 // 100) + 1
    lower = isqrt(1_02_03_04_05_06_07_08_09_00 // 100)
    numbers = [
        n * 10
        for n in chain(
            range(upper - (upper % 10) + 3, lower, -10),
            range(upper - (upper % 10) + 7, lower, -10),
        )
        if check(n * n)
    ]
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0]
    return numbers


def check(n):
    for d in range(9, 0, -1):
        if n % 10 != d:
            return False
        n //= 100
    return True
