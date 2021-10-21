"""
Problem 148 of Project Euler.

https://projecteuler.net/problem=148

Write n in base 7 as dk,d(k-1),...,d2,d1,d0,
where each d_i is a digit between 0 and 6.

Let f(n) be the number of entries in the first n rows of Pascal's triangle
not divisible by 7.

Then f(n) = (1 + 2 + ... + (d_k - 1) + dk) 28^k + (dk + 1) f(n - dk * 7^(k))
"""

SUM_TO_D = [0, 1, 3, 6, 10, 15, 21]


def problem148(n=1_000_000_000):
    base_7 = decimal_to_base7(n)
    count = 0
    for k, d in enumerate(base_7):
        count = SUM_TO_D[d] * 28 ** k + (d + 1) * count
    return count


def decimal_to_base7(n):
    base7 = []
    while n > 0:
        base7.append(n % 7)
        n = n // 7
    return base7
