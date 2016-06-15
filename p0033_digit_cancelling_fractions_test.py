"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


Answer:
    100
"""


from functools import reduce


def nontrivial_fractions():
    return ((x // 10, y % 10)
            for x in range(10, 100)
            for y in range((x % 10) * 10 + 1, (x % 10 + 1) * 10)
            if y > x and
               float(x) / float(y) == float(x // 10) / float(y % 10))


def mul_fracs(fracs):
    return reduce(lambda ab, xy: (ab[0] * xy[0], ab[1] * xy[1]), fracs, (1, 1))


def gcm(a, b):
    return a if b == 0 else gcm(b, a % b)


def digit_cancelling_fractions():
    a, b = mul_fracs(nontrivial_fractions())
    g = gcm(a, b)
    return b / g


def test_0034_digit_cancelling_fractions():
    assert digit_cancelling_fractions() == 100
