"""
Problem 070 of Project Euler.

https://projecteuler.net/problem=070
"""


from lib.euler_lib import is_digit_permutation, list_totients


# TODO Optimize
def problem070(limit=10 ** 7):
    """
    You can use a sieve to calculate the totients.
    """
    totient = list_totients(limit)
    totient_perm = {
        n: n / phi
        for n, phi in enumerate(totient[2:], 2)
        if is_digit_permutation(n, phi)
    }
    return min(totient_perm, key=totient_perm.get)
