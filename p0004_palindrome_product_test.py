"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
    906609
"""

from euler.util import is_palindrome
from itertools import takewhile


def palindrome_products(start, end):
    lower_bound = start

    def countdown():
        return takewhile(lambda n: n > lower_bound, range(end, 0, -1))

    candidates = ((x * y, min(x, y))
                  for x in countdown()
                  for y in countdown()
                  if is_palindrome(x * y))

    for palindrome, new_lower_bound in candidates:
        yield palindrome
        lower_bound = new_lower_bound


def max_palindrome_product(start, end):
    return max(palindrome_products(start, end))


def test_0004_palindrome_product():
    assert max_palindrome_product(100, 999) == 906609
