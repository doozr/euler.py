from __future__ import absolute_import
from itertools import count, chain
from math import sqrt
from euler.math import divides_by


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True


def primes():
    return (x for x in count() if is_prime(x))


def sieve_of_eratosthenes(upper_bound):
    marked = [False] * upper_bound
    yield 2
    for value in (x for x in range(3, upper_bound, 2) if not marked[x]):
        yield value
        for i in range(value, upper_bound, value):
            marked[i] = True


def sieve(n):
    marked = [True] * (n//2)
    for i in (x for x in range(3, int(n**0.5 + 1), 2) if marked[x // 2]):
        num_to_update = ((n - i * i - 1) // (2 * i) + 1)
        marked[i * i // 2::i] = [False] * num_to_update
    return chain([2], (2 * i + 1
                       for i in range(1, n // 2)
                       if marked[i]))


def prime_factors(n):
    if n == 2 or n == 3:
        yield n
        return
    i = 2
    while i * i < n:
        while divides_by(n, i):
            n /= i
            yield i
        i += 1
    if n > 1:
        yield n


