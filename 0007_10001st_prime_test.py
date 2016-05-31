"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


Answer:
    104743
"""


from math import sqrt
from itertools import islice, count


def is_prime(x):
    if not x % 2:
        return False
    limit = int(sqrt(x) + 1)
    return all(x % y for y in range(3, limit))


def prime_generator():
    return (x for x in count() if is_prime(x))


def nth_prime(n):
    return next(islice(prime_generator(), n - 1, n))


def test_10001st_prime():
    assert nth_prime(10001) == 104743
