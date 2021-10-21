"""
Problem 265 of Project Euler.

https://projecteuler.net/problem=265

Note that all valid binary strings must begin with "00000".
Also note that valid binary strings, have five consecutive "0"'s,
five consecutive "1"'s, three consecutive "0"'s, and three consecutive "1"'s,
all exactly once, with no four consecutive sequences.
"""

from itertools import product


def problem265():
    return sum(int(string, 2) for string in string_builder() if check(string))


def check(bin_str):
    bin_str += 5 * "0"
    return all("".join(seq) in bin_str for seq in product(["0", "1"], repeat=5))


def string_builder():
    blocks = ["11111", "000", "111"]
    blocks += "0" * 8
    blocks += "1" * 8
    return string_builder_helper("00000", blocks)


def string_builder_helper(bin_str, blocks):
    if not blocks:
        return [bin_str]

    add_blocks = []
    if "11111" in blocks and bin_str[-1] == "0":
        add_blocks.append("11111")
    if "111" in blocks and bin_str[-1] == "0":
        add_blocks.append("111")
    if "000" in blocks and bin_str[-1] == "1":
        add_blocks.append("000")
    if "1" in blocks and not (bin_str[-1] == "1" and bin_str[-2] == "1"):
        add_blocks.append("1")
    if "0" in blocks and not (bin_str[-1] == "0" and bin_str[-2] == "0"):
        add_blocks.append("0")

    strings = []
    for x in add_blocks:
        i = blocks.index(x)
        strings += string_builder_helper(bin_str + x, blocks[:i] + blocks[i + 1 :])

    return strings
