"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is
minimised; what is the value of D?


Answer:
    5482660
"""


from itertools import count, takewhile


def pentagon_number(n):
    return n * (n * 3 - 1) / 2


PENTAGON_LIST = list(takewhile(lambda n: n <= 10000000, (pentagon_number(n) for n in count(1))))
PENTAGON_NUMBERS = set(PENTAGON_LIST)


def minimised_diff():
    return next(x - y
                for x, y in ((PENTAGON_LIST[a], PENTAGON_LIST[b])
                             for a in range(0, len(PENTAGON_LIST))
                             for b in range(a, -1, -1))
                if x + y in PENTAGON_NUMBERS and
                x - y in PENTAGON_NUMBERS)


def test_0044_pentagon_numbers():
    assert minimised_diff() == 5482660

