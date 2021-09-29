"""
Problem 015 of Project Euler.

https://projecteuler.net/problem=015
"""

from math import comb


def problem015(w=20, h=20):
    """
    You can only move right or dowm.
    Therefore, each route takes w + h steps,
    of which you must choose w of those steps to move right.
    """
    return comb(w + h, w)
