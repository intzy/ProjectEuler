"""
Problem 042 of Project Euler.

https://projecteuler.net/problem=042
"""

from lib.misc import is_square

UPPER_CASE_CORRECTION = -64


def problem042(filename="txt/pb042.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().replace('"', "").split(",")

    triangle_words = set()
    for word in words:
        word_val = sum([ord(character) + UPPER_CASE_CORRECTION for character in word])
        if is_triangle_number(word_val):
            triangle_words.add(word)
    return len(triangle_words)


def is_triangle_number(n):
    return is_square(8 * n + 1)
