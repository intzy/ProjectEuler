"""
Problem 117 of Project Euler.

https://projecteuler.net/problem=117

If f(n) is the number of configurations of on a row of n tiles
then it is easy to prove that

    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)

along with a correct base-case.
"""


def problem117(n=50):
    f = [None] * (n + 1)
    f[0] = 1
    f[1] = f[0]
    f[2] = f[1] + f[0]
    f[3] = f[2] + f[1] + f[0]
    for m in range(4, n + 1):
        f[m] = f[m - 1] + f[m - 2] + f[m - 3] + f[m - 4]
    return f[n]
