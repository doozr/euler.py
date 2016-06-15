"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


Answer:
    669171001
"""


from operator import add
from itertools import chain, repeat
from euler.iter import scan


def spiral_diagonal_sum(limit):
    """
    The diagonals of the spiral can be calculated without having to calculate
    the whole spiral. Starting from 1 there is a step size of 2 to 3, 5, 7 and 9.
    Then there is a step size of 4 to 13, 17, 21 and 25. A step size of 6 would
    be next to take 25 to 31, 37, 43 and 49. Incrementing the step size by 2 for
    every fourth value is how to handle this.

    Args:
        limit (int): The maximum length of a side (must be odd)

    Returns:
        (list): A list of values in the diagonals
    """
    assert limit % 2
    increments = chain.from_iterable(repeat(x, 4) for x in range(2, limit, 2))
    return 1 + sum(scan(add, increments, 1))


def test_0028_number_spiral_diagonals():
    assert spiral_diagonal_sum(1001) == 669171001
