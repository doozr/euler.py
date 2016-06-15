"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right
to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


Answer:
    748317
"""


from euler.math import num_digits
from euler.prime import sieve


PRIMES = set(sieve(1000000))


def is_truncatable(x):
    return all((x // 10**p) in PRIMES and
               (x % 10**p) in PRIMES
               for p in range(1, num_digits(x)))


def truncatable_primes():
    return sum(x for x in PRIMES if x > 7 and is_truncatable(x))


def test_0037_truncatable_primes():
    assert truncatable_primes() == 748317
