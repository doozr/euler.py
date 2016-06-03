"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
    232792560
"""


def smallest_multiple(limit):
    # For each value that the accumulator does not already divide by,
    # multiply the accumulator by the lowest integer that makes it divide by
    # both the old accumulator and the new value
    return reduce(
        lambda acc, x: acc * next(y for y in range(1, x + 1) if (acc * y) % x == 0),
        range(2, limit + 1),
        1
    )


def test_0005_smallest_multiple():
    assert smallest_multiple(20) == 232792560