"""
Problem 144 of Project Euler.

https://projecteuler.net/problem=144
"""

from math import sqrt


def problem144():
    count = 1
    x, y = 1.4, -9.6
    rx, ry = 1.4, -9.6 - 10.1

    while True:
        nx, ny = get_normal(x, y)

        r_dot_n = rx * nx + ry * ny
        rx, ry = rx - 2 * r_dot_n * nx, ry - 2 * r_dot_n * ny

        # y = mx + b
        m = ry / rx
        b = y - (ry / rx) * x

        x, y = next_point(m, b, x, y)
        if -0.01 <= x <= 0.01 and y > 0:
            return count
        count += 1


def get_normal(x, y):
    try:
        n = y / (4 * x)
        nbar = sqrt(1 + n * n)
        nx, ny = 1 / nbar, n / nbar
    except ZeroDivisionError:
        nx, ny = 0, 1
    return nx, ny


def next_point(m, b, x, y):
    det = sqrt(4 * m * m * b * b - 4 * (4 + m * m) * (b * b - 100))
    x1 = (-2 * m * b + det) / (2 * (4 + m * m))
    y1 = m * x1 + b
    x2 = (-2 * m * b - det) / (2 * (4 + m * m))
    y2 = m * x2 + b
    if (round(x1, 9), round(y1, 9)) == (round(x, 9), round(y, 9)):
        return x2, y2
    return x1, y1
