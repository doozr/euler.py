from math import floor, log10
from euler.prime import sieve
from euler.iter import length, scan


def num_digits(x):
    return 1 if x == 0 else int(floor(log10(x)) + 1)


def has_even_digit(x):
    return any((x / 10**n) % 2 == 0
               for n in range(0, num_digits(x)))


def rotate(x):
    if x < 10:
        return x
    first = x % 10
    rest = x // 10
    exp = num_digits(rest)
    return rest + first * 10 ** exp


def rotations(x):
    return set(scan(
        lambda a, _: rotate(a),
        range(0, num_digits(x)), x))


def circular_primes(limit):
    primes = set(sieve(limit))
    return (p for p in primes
            if (p == 2 or not has_even_digit(p)) and
            rotations(p).issubset(primes))


def test_0035_circular_primes():
    assert length(circular_primes(1000000)) == 55
