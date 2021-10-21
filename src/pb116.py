"""
Problem 116 of Project Euler.

https://projecteuler.net/problem=116

If f(n) is the number of configurations of (say) the red blocks
on a row of n tiles,
then it is easy to prove that f(m) = 0 for m = 0, ..., s; and

    f(m) = f(m - 1) + f(m - s)

where s = 2 is the size of the red block.
"""

RED_BLOCK_LENGTH = 2
GREEN_BLOCK_LENGTH = 3
BLUE_BLOCK_LENGTH = 4


def problem116(n=50):
    return (
        count_block_configurations(n, RED_BLOCK_LENGTH)
        + count_block_configurations(n, GREEN_BLOCK_LENGTH)
        + count_block_configurations(n, BLUE_BLOCK_LENGTH)
    )


def count_block_configurations(n, s):
    f = [0] * (n + 1)
    for m in range(s, n + 1):
        f[m] = 1 + f[m - 1] + f[m - s]
    return f[n]
