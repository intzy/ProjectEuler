"""
Problem 160 of Project Euler.

https://projecteuler.net/problem=160

If the prime decomposition of x! is

    x! = 2^{k2} * 3^{k3} * 5^{k5} * 7^{k7} * ...,

then

    f(x) = 2^{k2 - k5} * 3^{k3} * 7^{k7} * ...
"""

from math import log


def problem160(N=10 ** 12, digits=5):
    """
    This algorithm only works if 10^digits <= N.
    """
    ans = 1
    modulo = 10 ** digits

    # Find 1 * (2 / 2) * 3 * (4 / 2) * (6 / 2) * 7 * ... * (modulo - 1)
    for start in [1, 3, 7, 9]:
        for n in range(start, modulo, 10):
            ans = ans * n % modulo
    for start in [2, 4, 6, 8]:
        for n in range(start, modulo, 10):
            ans = ans * (n // 2) % modulo
    ans = pow(ans, N // modulo, modulo)

    # x[n] = n! / 5^k, where k is the number of 5's in the decomposition of n!.
    x = [1 for _ in range(modulo + 1)]
    for n in range(1, modulo + 1):
        if not n % 5:
            x[n] = x[n - 1]
        else:
            x[n] = n * x[n - 1] % modulo

    # For each iteration, we calculate the contribution of each n to f(x)
    # for all n such that 5^k divides n but 5^{k + 1} does not divide n.
    for k in range(1, int(log(N, 5)) + 1):
        y = 5 ** k
        q, r = divmod(N, modulo * y)
        ans = ans * pow(x[modulo], q, modulo) * x[r // y] % modulo

    # Finally, multiply the 2's that don't belong with a 5.
    num_fives = sum(N // (5 ** k) for k in range(1, int(log(N + 1, 5)) + 1))
    num_missing_twos = N // 2 - N // 10
    ans = ans * pow(2, num_missing_twos - num_fives, modulo) % modulo
    return ans
