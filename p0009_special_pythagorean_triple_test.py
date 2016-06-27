"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Answer:
    31875000
"""


def mn(num):
    return next((m, n)
                for m in range(1, num)
                for n in range(1, m)
                if m * (m + n) == num // 2)


def pythagoras_triangle(num):
    m, n = mn(num)
    return (m**2 - n**2,
            2 * m * n,
            m**2 + n**2)


def special_triple_product(num):
    a, b, c = pythagoras_triangle(num)
    return a * b * c


def test_0009_special_triple():
    assert special_triple_product(1000) == 31875000


