from math import sqrt
from itertools import count


def is_prime(x):
    if not x % 2:
        return False
    limit = int(sqrt(x) + 1)
    return all(x % y for y in range(3, limit))


def primes():
    return (x for x in count() if is_prime(x))


def sieve(size):
    marked = [0] * size
    value = 3
    yield 2
    for value in (x for x in xrange(value, size, 2) if marked[x] == 0):
        yield value
        for i in xrange(value, size, value):
            marked[i] = 1
