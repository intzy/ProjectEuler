"""
Problem 145 of Project Euler.

https://projecteuler.net/problem=145

A number can't be reversible if its length is 1 mod 4.
You can come up with (seperate) closed form expressions for how many
reversible numbers there are of length n if n = 0 mod 2 or n = 3 mod 4.
"""


def problem145(n=9):
    count = 0
    for m in range(2, n, 2):
        count += 20 * pow(30, m // 2 - 1)
    for m in range(3, n, 4):
        count += 5 * pow(25, (m - 3) // 4) * pow(20, (m + 1) // 4)
    return count
