"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
    906609
"""


from euler.util import is_palindrome
from itertools import takewhile


def max_palindrome_product(start, end):
    def _palindrome_products():
        lower_bound = start
        still_valid = lambda n: n > lower_bound
        for palindrome, new_lower_bound in ((x * y, min(x, y))
                                            for x in takewhile(still_valid, range(end, 0, -1))
                                            for y in takewhile(still_valid, range(end, 0, -1))
                                            if is_palindrome(x * y)):
            yield palindrome
            lower_bound = new_lower_bound

    return max(_palindrome_products())


def test_0004_palindrome_product():
    assert max_palindrome_product(100, 999) == 906609

