"""
Problem 018 of Project Euler.

https://projecteuler.net/problem=018
"""

from lib.euler_lib import file_to_matrix


def problem018(filename="txt/pb018.txt"):
    """
    Use bottom-up dymanic programming.
    """
    triangle = file_to_matrix(filename, " ")
    for i in reversed(range(len(triangle) - 1)):
        for j in reversed(range(i + 1)):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]
