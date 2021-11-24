"""
Diophantine equation solvers.
"""

from math import gcd, isqrt

from lib.misc import is_square


def bezouts(a, b, d):
    """
    Gives a solution (x, y) to ax + by = d, if one exits.
    Otherwise, returns None.
    """
    if d % gcd(a, b) != 0:
        return None
    q = [None, None]
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    while r[-1] != 0:
        q.append(r[-2] // r[-1])
        r.append(r[-2] - q[-1] * r[-1])
        s.append(s[-2] - q[-1] * s[-1])
        t.append(t[-2] - q[-1] * t[-1])
    m = d // r[-2]
    x = m * s[-2]
    y = m * t[-2]
    return (x, y)


def pells_eqn_fundamental_soln(D):
    """
    Find fundamental solution (x, y) to x^2 - Dy^2 = 1.
    """
    s = isqrt(D)
    t = 1
    p = [1, s]
    q = [0, 1]
    x = s
    y = 1
    while x * x - D * y * y != 1:
        t = (D - s * s) // t
        a = (isqrt(D) + s) // t
        s = t * a - s
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
        x = p[-1]
        y = q[-1]
    return (x, y)


def cf_period(n):
    """
    y / (sqrt(n) - x) = y (sqrt(n) + x) / (n - x^2)
                      = (sqrt(n) + x) / ynew
                      = a + (sqrt(n) - xnew) / ynew
    It we encounter the same (x, y) as before, then we hit a new cycle.
    """
    remainders = []
    x = isqrt(n)
    y = 1
    while (x, y) not in remainders:
        remainders.append((x, y))
        y = (n - pow(x, 2)) // y
        a = (isqrt(n) + x) // y
        x = y * a - x
    return len(remainders) - remainders.index((x, y))


def negative_pells_eqn_fundamental_soln(D):
    s = isqrt(D)
    t = 1
    p = [1, s]
    q = [0, 1]
    x = s
    y = 1
    while x * x - D * y * y != -1:
        t = (D - s * s) // t
        a = (isqrt(D) + s) // t
        s = t * a - s
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
        x = p[-1]
        y = q[-1]
    return (x, y)


def pells_eqn_solns(D):
    """
    Iterates through all solutions (x, y) for the Diophontaine equation

        x^2 - Dy^2 = 1.
    """
    if is_square(D):
        return
    x0, y0 = pells_eqn_fundamental_soln(D)
    xk, yk = x0, y0
    while True:
        yield (xk, yk)
        xk, yk = x0 * xk + D * y0 * yk, x0 * yk + y0 * xk


def negative_pells_eqn_solns(D):
    """
    Iterates through all solutions (x, y) for the Diophontine equation

        x^2 - Dy^2 = -1.
    """
    if is_square(D):
        return
    if not cf_period(D) % 2:
        return
    x0, y0 = negative_pells_eqn_fundamental_soln(D)
    u, v = (x0 * x0 + D * y0 * y0), 2 * x0 * y0
    xk, yk = x0, y0
    while True:
        yield (xk, yk)
        xk, yk = xk * u + D * yk * v, xk * v + yk * u
