"""
Problem 038 of Project Euler.

https://projecteuler.net/problem=038
"""

from itertools import count

from lib.euler_lib import concat_ints


def problem038():
    pandigitals = set()
    for n in range(1, 9876):
        x = n
        for i in count(2):
            x = concat_ints(x, i * n)
            if len(str(x)) == 9 and "".join(sorted(str(x))) == "123456789":
                pandigitals.add(x)
            if len(str(x)) >= 9:
                break
    return max(pandigitals)
