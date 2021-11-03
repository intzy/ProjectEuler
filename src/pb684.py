"""
Problem 684 of Project Euler.

https://projecteuler.net/problem=684
"""


def problem684(modulo=1000000007):
    fib = [0, 1]
    for i in range(2, 91):
        fib.append(fib[i - 1] + fib[i - 2])

    def S(n):
        q = n // 9
        r = n - 9 * q
        return (6 + (r * (r + 3)) // 2) * pow(10, q, modulo) - 6 - r - 9 * q

    return sum(S(n) for n in fib[2:]) % modulo
