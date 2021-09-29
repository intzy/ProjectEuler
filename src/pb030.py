"""
Problem 030 of Project Euler.

https://projecteuler.net/problem=030
"""

from itertools import combinations_with_replacement, count


def problem030(power=5):
    digit_powers = [i ** power for i in range(10)]
    digit_power_sums = [
        sum(d) for d in combinations_with_replacement(digit_powers, upper_bound(power))
    ]
    digit_power_sums.remove(1)

    return sum(n for n in digit_power_sums if n == sum(int(d) ** power for d in str(n)))


def upper_bound(power):
    return next(i for i in count(1) if len(str(i * (9 ** power))) <= i)
