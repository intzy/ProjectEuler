"""
Problem 493 of Project Euler.

https://projecteuler.net/problem=493
"""

from math import comb


def problem493(colours=7, balls_per_colour=10, chosen=20):
    """
    The probability that you won't pick a ball from a given colour is

        p = comb((colours - 1) * balls_per_colour, chosen) / comb(total_balls, chosen).
    """
    total_balls = colours * balls_per_colour
    p = comb(total_balls - balls_per_colour, chosen) / comb(total_balls, chosen)
    return round(colours * (1 - p), 9)
