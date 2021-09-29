"""
Problem 031 of Project Euler.

https://projecteuler.net/problem=031
"""


def problem031(total=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    count = [1] + [0] * total
    for coin in coins:
        for n in range(coin, total + 1):
            count[n] += count[n - coin]
    return count[-1]
