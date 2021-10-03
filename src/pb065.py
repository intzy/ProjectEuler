"""
Problem 065 of Project Euler.

https://projecteuler.net/problem=065
"""


def problem065(n=100):
    """
    For a continued fraction [a0, a1, ..., a_{n - 1}],
    with i'th convergents p_i / q_i,
    for i >= 2, we have p_i = a_i * p_{i - 1} + p_{i - 2}.
    """
    a = [2, 1]
    for i in range(2, n):
        x = ((i + 1) * 2) // 3 if i % 3 == 2 else 1
        a.append(x)
    p = [a[0], a[1] * a[0] + 1]
    for i in range(2, n):
        p.append(a[i] * p[-1] + p[-2])
    return sum(int(d) for d in str(p[-1]))
