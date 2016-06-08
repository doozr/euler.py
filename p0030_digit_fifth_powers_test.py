"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


Answer:
    443839
"""


from itertools import count


def limit(power):
    """
    Determine the upper limit of the calculation

    Find the first value of (x * 9**p) where p is the power we're raising
    each digit to that is lower than (10**(x - 1)). That is to say,
    if the sum of the digits of the highest possible N digit number
    (made up entirely of 9s) is lower than the lowest N digit number
    (made up of a 1 and N-1 0s), it's above our threshold.

    The limit is the sum of the digits for the highest N digit number
    where this is the case.

    Args:
        power (int): Which power are we looking for?

    Returns:
        (int): The upper limit of the search range
    """
    return next(x * (9**power)
                for x in count(1)
                if x * (9**power) < 10**(x - 1))


def digit_power_sum(x, power):
    return sum(int(y) ** power for y in str(x))


def sum_all_that_equal_power_sum(power):
    return sum(x for x in xrange(2, limit(power) + 1)
               if digit_power_sum(x, power) == x)


def test_0030_digit_fifth_powers():
    assert sum_all_that_equal_power_sum(5) == 443839


