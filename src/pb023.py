"""
Problem 023 of Project Euler.

https://projecteuler.net/problem=023
"""

from lib.number_theory import list_sum_proper_divisors


def problem023():
    """
    For each n,
    suffices to find all abundant m < n and check n - m is not abundant.
    """
    limit = 28123
    d = list_sum_proper_divisors(limit)

    abundant = set()
    not_sum_of_abundunts = []
    for n in range(1, limit):
        if not any((n - m in abundant) for m in abundant):
            not_sum_of_abundunts.append(n)
        if d[n] > n:
            abundant.add(n)

    return sum(not_sum_of_abundunts)
