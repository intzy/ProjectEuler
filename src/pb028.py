"""
Problem 028 of Project Euler.

https://projecteuler.net/problem=028
"""


def problem028(spiral_size=1001):
    """
    An O(1) solution exists by recalling that 1 + 2 + ... + n and 1^2 + 2^2 + ... + n^2
    have closed form expression.
    By putting each diagonal into a summation,
    you can find a closed form of the diagonals using the above identities.
    """
    n = (spiral_size - 1) // 2
    return (16 * n ** 3 + 30 * n ** 2 + 26 * n + 3) // 3
