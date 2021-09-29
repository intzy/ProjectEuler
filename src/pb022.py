"""
Problem 022 of Project Euler.

https://projecteuler.net/problem=022
"""

UPPER_CASE_CORRECTION = -64


def problem022(filename="txt/pb022.txt"):
    """
    Recall that ord("A") = 65, so we have to use a correction of -64.
    """
    with open(filename, "r", encoding="utf-8") as f:
        names = f.read().replace('"', "").replace("\n", "").split(",")
    names.sort()
    return sum(
        (i + 1) * sum(ord(letter) + UPPER_CASE_CORRECTION for letter in name)
        for i, name in enumerate(names)
    )
