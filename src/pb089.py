"""
Problem 089 of Project Euler.

https://projecteuler.net/problem=089
"""


def problem089(filename="txt/pb089.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        numerals = f.readlines()
    numerals = [x.replace("\n", "") for x in numerals]

    old_num_characters = sum(len(x) for x in numerals)
    for i, x in enumerate(numerals):
        numerals[i] = roman_to_decimal(x)
    for i, x in enumerate(numerals):
        numerals[i] = decimal_to_roman(x)
    new_num_characters = sum(len(x) for x in numerals)
    return old_num_characters - new_num_characters


def roman_to_decimal(x):
    """
    Given a string representation of a Roman numeral,
    returns the corresponding integer.

    Does not check that the string is in fact a valid Roman numeral.
    """
    x = x.replace("IV", "IIII")
    x = x.replace("IX", "VIIII")
    x = x.replace("XL", "XXXX")
    x = x.replace("XC", "LXXXX")
    x = x.replace("CD", "CCCC")
    x = x.replace("CM", "DCCCC")
    decimal = 0
    decimal += 1000 * x.count("M")
    decimal += 500 * x.count("D")
    decimal += 100 * x.count("C")
    decimal += 50 * x.count("L")
    decimal += 10 * x.count("X")
    decimal += 5 * x.count("V")
    decimal += 1 * x.count("I")
    return decimal


def decimal_to_roman(x):
    """
    Given a decimal, returns the corresponding Roman numeral as a string.
    """
    dec_to_rmn = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    numeral = ""
    for dec, rmn in dec_to_rmn.items():
        while x >= dec:
            numeral += rmn
            x -= dec
    return numeral
