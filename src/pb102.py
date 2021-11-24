"""
Problem 102 of Project Euler.

https://projecteuler.net/problem=102

A triganle xyz contains the origin if and only if x * xy, y * yz, and z * zx
all have the same sign, where * denotes cross product.
"""

from lib.misc import file_to_matrix


def problem102():
    m = file_to_matrix("txt/pb102.txt", ",")
    return sum(
        1
        for xyz in m
        if origin_in_triangle((xyz[0], xyz[1]), (xyz[2], xyz[3]), (xyz[4], xyz[5]))
    )


def origin_in_triangle(x, y, z):
    x1, x2 = x
    y1, y2 = y
    z1, z2 = z
    x_cross_xy = x1 * (y2 - x2) - x2 * (y1 - x1)
    y_cross_yz = y1 * (z2 - y2) - y2 * (z1 - y1)
    z_cross_zx = z1 * (x2 - z2) - z2 * (x1 - z1)
    return (
        x_cross_xy * y_cross_yz >= 0
        and y_cross_yz * z_cross_zx >= 0
        and z_cross_zx * x_cross_xy >= 0
    )
