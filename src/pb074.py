"""
Problem 074 of Project Euler.

https://projecteuler.net/problem=074
"""

from lib.euler_lib import digit_factorial


def problem074(limit=1_000_000):
    """
    Use dynamic programming.

    A possible optimization would be using the cache by the digits of a number
    instead of the number itself (though you would need to account for the base cases
    seperatley (eg. 145: 1, but 154: 2).
    """
    cache = {}
    count = 0
    for n in range(1, limit):
        if n in cache and cache[n] == 60:
            count += 1
            continue
        m = n
        chain = []
        while m not in chain and m not in cache:
            chain.append(m)
            m = digit_factorial(m)
        offset = cache[m] + 1 if m in cache else 1
        for i, m in enumerate(reversed(chain)):
            cache[m] = i + offset
        if cache[n] == 60:
            count += 1
    return count
