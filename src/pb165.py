"""
Problem 165 of Project Euler.

https://projecteuler.net/problem=165

To get around the problem of numerical stability,
all intersection points are given as fractions.
However, this makes the code more complicated
and adds a ~*2 slowdown.

Given two points (x1, y1), (x2, y2),
its parametric equation is

    r(t) = (x1 + (x2 - x1)t, y1 + (y2 - y1)t),      0 <= t <= 1.

Therefore, given to parametric equations r(t) and s(u),
to find the intersection, it suffices to find the t, u such that r(t) = s(u).
We can solve this by simple linear algebra.
We then know that the intersection is a true intersection point if

    0 < t < 1,  0 < u < 1.
"""

from itertools import combinations
from math import gcd


def problem165(N=5000):
    L = get_line_segments(N)
    true_intersections = set()
    for L1, L2 in combinations(L, 2):
        x = get_intersection(L1, L2)
        if x:
            true_intersections.add(x)
    return len(true_intersections)


def get_line_segments(N):
    s = [290797]
    for _ in range(1, 4 * N + 1):
        s.append(s[-1] * s[-1] % 50515093)
    t = [x % 500 for x in s]
    return [t[n : n + 4] for n in range(1, 4 * N + 1, 4)]


# pylint: disable=R0914
# Too many local variables
def get_intersection(L1, L2):
    x1, y1, x2, y2 = L1
    z1, w1, z2, w2 = L2
    a1 = x2 - x1
    a2 = z1 - z2
    a3 = y2 - y1
    a4 = w1 - w2
    b1 = z1 - x1
    b2 = w1 - y1
    det = a1 * a4 - a2 * a3
    if not det:
        return False
    sign = abs(det) // det
    t = (a4 * b1 - a2 * b2) * sign
    u = (a1 * b2 - a3 * b1) * sign
    det *= sign
    if t <= 0 or t >= det or u <= 0 or u >= det:
        return False
    p = (det * x1 + (x2 - x1) * t, det)
    q = (det * w1 + (w2 - w1) * u, det)
    dp = gcd(p[0], p[1])
    dq = gcd(q[0], q[1])
    p = (p[0] // dp, p[1] // dp)
    q = (q[0] // dq, q[1] // dq)
    return (p, q)
