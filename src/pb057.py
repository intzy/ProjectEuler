"""
Problem 057 of Project Euler.

https://projecteuler.net/problem=057
"""


def problem057(limit=1000):
    """
    If the n'th continued fraction expansion of sqrt(2) is p_n/q_n,
    then for n >= 2 we have p_n = 2 * p_{n - 1} + p_{n - 2}, and similarily for q.
    """
    p = [1, 3]
    q = [1, 2]
    for _ in range(2, limit + 1):
        p.append(2 * p[-1] + p[-2])
        q.append(2 * q[-1] + q[-2])
    return sum(1 for i in range(1, limit + 1) if len(str(p[i])) > len(str(q[i])))
