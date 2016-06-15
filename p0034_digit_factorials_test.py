from itertools import count, chain, combinations_with_replacement
from euler.math import factorial


FACTORIALS = [factorial(_n) for _n in range(0, 10)]


def max_num_digits():
    return next(x for x in count(1) if x * factorial(9) < 10 ** x)


def inputs(max_digits):
    return chain.from_iterable(
        ("".join(map(str, x)) for x in combinations_with_replacement(range(0, 10), n))
        for n in range(2, max_digits + 1)
    )


def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))


def digit_factorials():
    for n in inputs(max_num_digits()):
        s = sum(FACTORIALS[int(x)] for x in n)
        if same_digits(n, s):
            yield s


def test_0035_digit_factorials():
    assert sum(digit_factorials()) == 40730

