"""
Problem 104 of Project Euler.

https://projecteuler.net/problem=104

We generate the last 9 digits of the fibonacci sequence by definition.
Then if needed, we generate the last 9 digits by calculating the log
of the fibonacci by the phi definition, extract the first 9 digits,
and test for pandigitality.
"""


from itertools import count
from math import log10, modf, sqrt


def problem104():
    f = [0, 1, 1]
    phi = (1 + sqrt(5)) / 2
    for k in count(3):
        f.append((f[-1] + f[-2]) % 10 ** 9)
        if is_pandigital(f[-1]):
            x, _ = modf(k * log10(phi) - 1 / 2 * log10(5))
            mantissa = 10 ** x
            if is_pandigital(int(mantissa * 10 ** 8)):
                return k
    return None


def is_pandigital(n):
    return sorted(str(n)) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
