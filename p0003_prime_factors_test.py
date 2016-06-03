"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
    6857
"""


from math import sqrt
from euler.prime import sieve


def reverse_primes(start):
    return reversed(list(sieve(start)))


def highest_prime_factor(x):
    limit = int(sqrt(x) + 1)
    return next(y for y in reverse_primes(limit) if not x % y)


def test_0003_prime_factors():
    assert highest_prime_factor(600851475143) == 6857