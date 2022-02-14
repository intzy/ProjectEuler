"""
Problem 164 of Project Euler.

https://projecteuler.net/problem=164

Use dynamic programming.

Let f[m][i] be the number of m-digit numbers such that the sum of
3 consecutive digits doesn't exceed 9 given that the last two
digits of these numbers are the digits of i.
"""


def problem164(n=20):
    f = [[0] * 100 for _ in range(n + 1)]
    for i in range(10, 100):
        f[2][i] = 1
    for m in range(3, n + 1):
        for i in range(100):
            for j in range(i // 10, 100, 10):
                if (j // 10) + (j % 10) + (i % 10) <= 9:
                    f[m][i] += f[m - 1][j]
    return sum(f[n])
