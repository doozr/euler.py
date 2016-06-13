"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000


Answer:
    210
"""


from itertools import chain, count, izip
from euler.math import product


def champernownes_digits():
    return chain.from_iterable(map(int, str(x)) for x in count())


def champernownes_product(offsets):
    return product(n for n, c in izip(champernownes_digits(),
                                      xrange(0, max(offsets) + 1))
                   if c in offsets)


def test_0040_champernownes_constant():
    assert champernownes_product([10**x for x in xrange(0, 7)]) == 210

