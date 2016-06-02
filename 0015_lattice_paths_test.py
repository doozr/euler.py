"""
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

__    _      _
  |    |_     |    |__    |_     |
  |      |    |_      |     |_   |__


How many such routes are there through a 20x20 grid?


Answer:
    137846528820
"""

# This problem is calculating a binomial coefficient, the formula
# of which is:
#              ( n )       n!
#              (   ) = ---------- for 0 < k < n
#              ( k )    k!(n-k)!
#
# If we consider each move in a grid to be a binary digit, with a
# horizontal move a 0 and a vertical move a 1, then the first path is:
#
# 0000000000000000000011111111111111111111
#
# and the last path is:
#
# 1111111111111111111100000000000000000000
#
# All other paths are some combination of 1s and 0s but, critically,
# there must always be an equal number of 1s and 0s otherwise the
# opposite corner could not be reached.
#
# Given that there are 40 moves required, and 20 moves per side,
# the binomial coefficient is calculated as:
#
#               40!        40!
#           ----------- = ------ = 137846528820
#           20!(40-20)!   20!20!

from math import factorial


def binom(n, k):
    assert 0 < k < n
    return factorial(n) / (factorial(k) * factorial(n - k))


def test_0015_lattice_paths():
    assert binom(40, 20) == 137846528820
