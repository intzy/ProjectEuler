"""
Problem 090 of Project Euler.

https://projecteuler.net/problem=090
"""

from itertools import combinations, combinations_with_replacement


def problem090():
    """
    It is feasible to do brute-force since we need to check
    (10 choose 6)^2 = 44100 dice configurations, which is easily managable.
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sum(
        1
        for x, y in combinations_with_replacement(combinations(digits, 6), r=2)
        if valid_config(x, y)
    )


def valid_config(x, y):
    return (
        # 01
        ((0 in x and 1 in y) or (1 in x and 0 in y))
        # 04
        and ((0 in x and 4 in y) or (4 in x and 0 in y))
        # 09
        and (
            (0 in x and 6 in y)
            or (6 in x and 0 in y)
            or (0 in x and 9 in y)
            or (9 in x and 0 in y)
        )
        # 16
        and (
            (1 in x and 6 in y)
            or (6 in x and 1 in y)
            or (1 in x and 9 in y)
            or (9 in x and 1 in y)
        )
        # 25
        and ((2 in x and 5 in y) or (5 in x and 2 in y))
        # 36
        and (
            (3 in x and 6 in y)
            or (6 in x and 3 in y)
            or (3 in x and 9 in y)
            or (9 in x and 3 in y)
        )
        # 49 and 64
        and (
            (4 in x and 6 in y)
            or (6 in x and 4 in y)
            or (4 in x and 9 in y)
            or (9 in x and 4 in y)
        )
        # 81
        and ((8 in x and 1 in y) or (1 in x and 8 in y))
    )
