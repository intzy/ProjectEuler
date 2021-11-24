"""
Problem 095 of Project Euler.

https://projecteuler.net/problem=095
"""

from lib.number_theory import list_sum_proper_divisors


def problem095(limit=1000000):
    d = list_sum_proper_divisors(limit + 1)

    def amicable_chain(n):
        amicable_chain = {n}
        m = d[n]
        while m <= limit and m not in amicable_chain:
            amicable_chain.add(m)
            m = d[m]
        return amicable_chain if m == n else set()

    longest_chain = max((amicable_chain(n) for n in range(limit)), key=len)
    return min(longest_chain)
