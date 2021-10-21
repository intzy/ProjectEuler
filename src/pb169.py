"""
Problem 169 of Project Euler.

https://projecteuler.net/problem=169

Consider the binary string representation of n.
Let count = (x, y, j), where
    x is the total number of representations of the number so far,
    y is the total number of representations of the number so far
        with a leading zero, and
    j is the index of the last zero.
"""


def problem169(n=10 ** 25):
    one_pos = [i for i, d in enumerate(bin(n)[:1:-1]) if d == "1"]

    count = (1, 0, -1)
    for i in one_pos:
        x, y, j = count
        x, y = (i - j) * x + y, (i - j - 1) * x + y
        count = (x, y, i)

    return count[0]
