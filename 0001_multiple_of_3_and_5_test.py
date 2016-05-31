"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer:
    233168
"""


def multiples_of_three_and_five(limit):
    return sum(x for x in range(1,limit) if not x % 3 or not x % 5)


def test_0001_multiples_of_three_and_five():
    assert multiples_of_three_and_five(1000) == 233168
