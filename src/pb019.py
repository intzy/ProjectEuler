"""
Problem 019 of Project Euler.

https://projecteuler.net/problem=019
"""

from datetime import date


def problem019(start_year=1901, end_year=2001, start_day=6):
    return sum(
        1
        for year in range(start_year, end_year)
        for month in range(1, 12 + 1)
        if date(year, month, 1).weekday() == start_day
    )
