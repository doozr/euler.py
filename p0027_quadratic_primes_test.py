"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive
values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.


Answer:
    -59231
"""


from functools import reduce
from itertools import takewhile, count
from euler.prime import sieve
from euler.iter import length


# Precalculate primes - this limits the scale of
# possible calculations but ok for this
PRIMES = set(sieve(1000000))


# Quick for for primality
def is_prime(x):
    return x in PRIMES


def prime_range(limit):
    pos = set(p for p in PRIMES if p < limit)
    neg = set(-x for x in pos)
    pos.update(neg)
    return pos


def num_primes(seq):
    return length(takewhile(is_prime, seq))


def quadratic(a, b):
    return (n**2 + a * n + b for n in count())


def consecutive_primes(limit):
    # a and b are likely to be prime
    primes = prime_range(limit)
    return ((a, b, num_primes(quadratic(a, b)))
            for a in primes
            for b in primes)


def quadratic_primes(limit):
    a, b, p = reduce(
        lambda x, y: y if y[2] > x[2] else x,
        consecutive_primes(limit),
        (0, 0, 0))
    return a * b


def test_0027_quadratic_primes():
    assert quadratic_primes(1000) == -59231

