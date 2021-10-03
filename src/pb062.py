"""
Problem 062 of Project Euler.

https://projecteuler.net/problem=062
"""

from itertools import count
from math import inf

from lib.euler_lib import int_len


def problem062(c=5):
    """
    Simply check all cubes upwards,
    storing cubes in equivalence classes based on their digits.
    """
    cubes = {}
    min_cube_id = None
    min_cube_len = inf
    for n in count(1):
        cube = n ** 3
        if int_len(cube) > min_cube_len:
            return cubes[min_cube_id].smallest_cube
        cube_id = "".join(sorted(str(cube)))
        if cube_id in cubes:
            cubes[cube_id].count += 1
            if cubes[cube_id].count == c:
                min_cube_len = int_len(cube)
                min_cube_id = cube_id
        else:
            cubes[cube_id] = CubePermutations(cube)
    return None


class CubePermutations:
    def __init__(self, smallest_cube):
        self.count = 1
        self.smallest_cube = smallest_cube
