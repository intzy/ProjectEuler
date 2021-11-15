"""
Problem 150 of Project Euler.

https://projecteuler.net/problem=150
"""

from math import inf


def problem150(size=1000):
    triangle_sums = get_triangle(size)

    ans = inf
    for i in range(size):
        for j in range(i + 1):
            sub_triangle_sum = 0
            for k in range(i, size):
                sub_triangle_sum += (
                    triangle_sums[k][k - i + j + 1] - triangle_sums[k][j]
                )
                ans = min(ans, sub_triangle_sum)
    return ans


def get_triangle(size):
    triangle = []
    t = 0
    for i in range(size):
        row = [0 for _ in range(i + 2)]
        for j in range(1, i + 2):
            t = (615949 * t + 797807) % (2 ** 20)
            s = t - 2 ** 19
            row[j] = row[j - 1] + s
        triangle.append(row)
    return triangle
