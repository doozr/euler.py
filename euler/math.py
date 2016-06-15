from __future__ import absolute_import
from math import log
from functools import reduce
from operator import mul


def divisors(n):
    def _divisors():
        i = 1
        while i * i < n:
            if n % i == 0:
                yield i
                if i != 1:
                    yield n / i
            i += 1
        if i * i == n:
            yield i
    return set(_divisors())


def product(seq):
    return reduce(mul, seq, 1)


def fib():
    x = 0
    y = 1
    yield y
    while True:
        x, y = y, x + y
        yield y


def factorial(x):
    return 1 if x == 0 else product(range(2, x + 1))


def num_digits(n, base=10):
    return int(log(n, base)) + 1


def is_pandigital(x, n = None):
    sx = set(str(x))
    c = set(str(cc) for cc in range(1, n or len(sx) + 1))
    return sx == c

