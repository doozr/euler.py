"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
    6857
"""

from math import sqrt
from itertools import count, takewhile


def is_prime(x):
    if not x % 2:
        return False
    limit = int(sqrt(x) + 1)
    return all(x % y for y in range(3, limit))


def reverse_primes(start):
    return (x for x in range(start, 1, -1) if is_prime(x))

def highest_prime_factor(x):
    limit = int(sqrt(x) + 1)
    return next(y for y in reverse_primes(limit) if not x % y)


print highest_prime_factor(600851475143)
