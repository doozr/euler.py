"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?


Answer:
    7652413
"""

from euler.prime import is_prime
from euler.math import is_pandigital


def pandigital_prime():
    return next(x for x in xrange(7654321, 0, -2) if is_pandigital(x) and is_prime(x))


def test_0041_pandigital_prime():
    assert pandigital_prime() == 7652413

