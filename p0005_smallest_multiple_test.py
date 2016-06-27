"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
    232792560
"""


from functools import reduce
from euler.math import divides_by


def smallest_multiple(limit):
    # For each value that the accumulator does not already divide by,
    # multiply the accumulator by the lowest integer that makes it divide by
    # both the old accumulator and the new value

    def multiply_by_lowest_int(total, n):
        lowest_multiplier = next(m for m in range(1, n + 1)
                                 if divides_by(total * m, n))
        return total * lowest_multiplier

    return reduce(multiply_by_lowest_int,
                  range(2, limit + 1), 1)


def test_0005_smallest_multiple():
    assert smallest_multiple(20) == 232792560
