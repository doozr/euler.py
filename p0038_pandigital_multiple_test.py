"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
with (1,2, ... , n) where n > 1?


Answer:
    932718654
"""


from itertools import count
from euler.iter import scan


DIGITS = set("123456789")


def is_pandigital(x):
    return len(x) == len(DIGITS) and set(x) == DIGITS


def has_duplicate_digits(x):
    return len(x) > len(set(x))


def pandigital_multiple(x):
    for ds in scan(lambda a, y: a + str(y * x), count(1), ""):
        if has_duplicate_digits(ds):
                return None
        if is_pandigital(ds):
                return int(ds)


def max_pandigital_multiple():
    return max(pandigital_multiple(x) for x in xrange(1, 10000))


def test_0038_pandigital_multiple():
    assert max_pandigital_multiple() == 932718654
