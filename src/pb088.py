"""
Problem 088 of Project Euler.

https://projecteuler.net/problem=088
"""

from math import isqrt


def problem088(kmax=12000):

    limit = 2 * kmax
    minimal_product_sums = {k: 2 * k for k in range(2, kmax + 1)}

    def find_product_sum_numbers(product, summation, a_max, length):
        for n in range(a_max, limit // product + 1):
            N = product * n
            s = summation + n
            k = N - s + length
            if k <= kmax and minimal_product_sums[k] > N:
                minimal_product_sums[k] = N
            find_product_sum_numbers(N, s, n, length + 1)

    for a in range(2, isqrt(limit) + 1):
        find_product_sum_numbers(a, a, a, 2)
    return sum(set(minimal_product_sums.values()))
