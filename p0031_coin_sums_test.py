# coding=utf-8
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?


Answer:
    73682
"""


def ways_to_make_change(total, denominations):
    def _ways_to_make_change(n, d, r):
        if r:
            return sum(_ways_to_make_change(x, r[0], r[1:])
                       for x in xrange(n, -1, -d))
        else:
            return 1
    ds = list(reversed(sorted(denominations)))
    return _ways_to_make_change(total, ds[0], ds[1:])


def test_0031_coin_sums():
    assert ways_to_make_change(200, [1, 2, 5, 10, 20, 50, 100, 200]) == 73682

