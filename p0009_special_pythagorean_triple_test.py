"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Answer:
    31875000
"""


def special_triple(num):
    return next((a, b, num - b - a)
                for b in range(1, num)
                for a in range(1, num - b)
                if a**2 + b**2 == (num - b - a)**2)


def special_triple_product(num):
    a, b, c = special_triple(num)
    return a * b * c


def test_0009_special_triple():
    assert special_triple_product(1000) == 31875000
