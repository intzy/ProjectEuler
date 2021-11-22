"""
Problem 159 of Project Euler.

https://projecteuler.net/problem=159
"""


def problem159(limit=1000000):
    mdrs = [0 for _ in range(limit)]
    for n in range(2, limit):
        mdrs[n] = max(mdrs[n], n - (n - 1) // 9 * 9)
        for k in range(2, min(n + 1, (limit - 1) // n + 1)):
            mdrs[k * n] = max(mdrs[k * n], mdrs[k] + mdrs[n])
    return sum(mdrs)
