"""
Problem 149 of Project Euler.

https://projecteuler.net/problem=149
"""


def problem149():
    M = get_random_matrix()
    size = len(M)
    row_max = max(max_sublist(M[i]) for i in range(size))
    column_max = max(max_sublist([M[i][j] for i in range(size)]) for j in range(size))
    right_diagonal_from_top_max = max(
        max_sublist([M[j][i + j] for j in range(size - i)]) for i in range(size)
    )
    right_triangle_from_left_max = max(
        max_sublist([M[i + j][j] for j in range(size - i)]) for i in range(1, size)
    )
    left_triangle_from_top_max = max(
        max_sublist([M[j][i - j] for j in range(i + 1)]) for i in range(size)
    )
    left_triangle_from_right_max = max(
        max_sublist([M[i + j][size - 1 - j] for j in range(size - i)])
        for i in range(1, size)
    )

    return max(
        row_max,
        column_max,
        right_diagonal_from_top_max,
        right_triangle_from_left_max,
        left_triangle_from_top_max,
        left_triangle_from_right_max,
    )


def get_random_matrix():
    s = psuedo_random_generator()
    return [[s[2000 * i + j] for j in range(2000)] for i in range(2000)]


def psuedo_random_generator():
    s = []
    for k in range(1, 56):
        s.append((100003 - 200003 * k + 300007 * (k ** 3)) % 1000000 - 500000)
    for k in range(56, 4000001):
        s.append((s[-24] + s[-55]) % 1000000 - 500000)
    return s


def max_sublist(a):
    # Variatioin of Kadane's algorithm.
    best = cur = a[0]
    for n in a:
        cur = max(cur + n, n)
        best = max(best, cur)
    return best
