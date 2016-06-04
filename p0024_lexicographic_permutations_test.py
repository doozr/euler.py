"""
A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Answer:
    2783915460
"""


from itertools import permutations, islice


def nth_permutation(s, n):
    # If the list passed to permutations() is sorted, the output will be too
    return "".join(next(islice(permutations(sorted(s)), n - 1, n)))


def test_0024_lexicographic_permutations():
    assert nth_permutation("0123456789", 1000000) == "2783915460"
