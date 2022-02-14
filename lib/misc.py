"""
Project Euler Library

A collection of functions that are used in multiple project euler problems.
"""

from math import isqrt, log10

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
DIGIT_STRINGS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def digit_sum(n):
    """
    Returns the sum of the digits of the integer n.
    """
    summation = 0
    while n != 0:
        summation += n % 10
        n //= 10
    return summation


def int_len(n):
    """
    Returns the number of digits the positive integer n has.
    """
    if n > 999999999999997:
        return len(str(n))
    return int(log10(n)) + 1


def is_square(n):
    """
    Return True if and only if n is a perfect square.
    """
    return isqrt(n) ** 2 == n


def is_pentagonal(n):
    """
    Return True if and only if n is a pentagonal number,
    i.e., n = m(3m - 1)/2 for some integer m
    """
    m = 1 + 24 * n
    return is_square(m) and isqrt(m) % 6 == 5


def is_digit_permutation(n, m):
    """
    Return True if and only if n and m are, in base 10, permutations of the same digits.
    Does not consider leading zeros
    """
    return sorted(str(n)) == sorted(str(m))


def sum_to_n(n):
    """
    Takes an integer, outputs 1 + 2 + ... + (n-1) + n
    """
    return n * (n + 1) // 2


def is_palindrome(number):
    """
    Takes an integer, outputs True if and only if the integer is a palindrome number
    """
    return int(str(number)[::-1]) == number


def concat_ints(*args):
    """
    Takes one or more digits, concatenates their digits,
    and returns the resulting integer
    """
    n = ""
    for arg in args:
        n = f"{n}{arg}"
    return int(n)


def digit_factorial(number):
    digit_fact = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
    answer = 0
    while number > 0:
        digit, number = number % 10, number // 10
        answer += digit_fact[digit]
    return answer


def file_to_matrix(filename, separator):
    with open(filename, "r", encoding="utf-8") as f:
        strings = f.readlines()
    array = []
    for string in strings:
        array.append(list(map(int, string.split(separator))))
    return array
