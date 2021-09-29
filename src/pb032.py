"""
Problem 032 of Project Euler.

https://projecteuler.net/problem=032
"""


def problem032():
    pandigital_products = set()
    for i in range(1, 10):
        for j in range(1000, 10000 // i + 1):
            if is_pandigital_product(i, j):
                pandigital_products.add(i * j)
    for i in range(10, 100):
        for j in range(100, 10000 // i + 1):
            if is_pandigital_product(i, j):
                pandigital_products.add(i * j)
    return sum(pandigital_products)


def is_pandigital_product(i, j):
    s = str(i) + str(j) + str(i * j)
    return "".join(sorted(s)) == "123456789"
