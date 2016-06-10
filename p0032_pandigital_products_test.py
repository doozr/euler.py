"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product
is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


Answer:
    45228
"""


DIGITS = set("123456789")


def is_pandigital(x, y):
    s = "%s%s%s" % (x, y, x * y)
    return len(s) == 9 and set(s) == DIGITS


def pandigital_products():
    return set(x * y for x in xrange(1, 100) for y in range(100, 10000 / x + 1) if is_pandigital(x, y))


def test_0032_pandigital_products():
    assert sum(pandigital_products()) == 45228
