"""
Problem 017 of Project Euler.

https://projecteuler.net/problem=017
"""


def problem017(limit=1000):
    return sum(len(int_to_english_word(n)) for n in range(1, limit + 1))


def int_to_english_word(n):
    if n in range(100, 1000):
        if n % 100 == 0:
            return ONES[n // 100] + "Hundred"
        if (n // 10) % 10 in {0, 1}:
            return ONES[n // 100] + "Hundred" + "And" + ONES[n % 100]
        return ONES[n // 100] + "Hundred" + "And" + TENS[(n // 10) % 10] + ONES[n % 10]
    if n in range(20, 100):
        return TENS[(n // 10)] + ONES[n % 10]
    if n in range(1, 20):
        return ONES[n]
    if n == 1000:
        return "OneThousand"
    raise ValueError()


ONES = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]

TENS = [
    None,
    None,
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]
