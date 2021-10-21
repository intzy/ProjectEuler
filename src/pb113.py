"""
Problem 113 of Project Euler.

https://projecteuler.net/problem=113

Let f(n) be the number of increasing non-negative integers less than n.
Let F(n, d) be the number of increasing non-negative integers less than n
whose first digit is d (where d is possibly 0).
Clearly f(n) = sum(F(n, d) for 0 <= d <= 9).
We also get the recurrence relation F(n, d) = sum(F(n-1), i) for d <= i <= 9).

Let g(n) be the number of decreasing non-negative integers less than n.
Note that we don't consider leading zeros when deciding if a number is decreasing.
A number is decreasing if when written in reverse, it is an increasing number
Therefore, g(n) = sum(f(i) for 1 <= i <= n)

A number is both increasing and decreasing if all its digits are the same.
To prevent double counting, we must subtract this from our total.
"""


def problem113(n=100):
    F = [1 for _ in range(10)]
    decreasing = 10
    for _ in range(1, n):
        for digit in range(10):
            F[digit] = sum(F[digit:])
        decreasing += sum(F)
    increasing = sum(F)
    both = 10 * n

    # subtract one since we don't include 0
    return increasing + decreasing - both - 1
