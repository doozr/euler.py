from math import sqrt
from itertools import count, takewhile


def is_prime(x):
    if not x % 2:
        return False
    limit = int(sqrt(x) + 1)
    return all(x % y for y in range(3, limit))


def primes():
    return (x for x in count(1) if is_prime(x))


def prime_factors(x):
    limit = int(sqrt(x) + 1)
    return (y for y in takewhile(lambda z: z < limit, primes()) if not x % y)


print max(prime_factors(600851475143))
