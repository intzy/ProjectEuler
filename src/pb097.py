"""
Problem 097 of Project Euler.

https://projecteuler.net/problem=097
"""


def problem097(power=7_830_457, multiple=28433, digits=10):
    return (multiple * pow(2, power, 10 ** digits) + 1) % (10 ** digits)
