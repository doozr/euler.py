"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
    906609
"""


from euler.util import is_palindrome


def palindrome_product(start, end):
    lower_bound = start
    pp = 0
    x = end
    while x > lower_bound:
        y = end
        while y > lower_bound:
            r = x * y
            if is_palindrome(r):
                lower_bound = min(x, y)
                pp = max(pp, r)
            y -= 1
        x -= 1
    return pp


def test_0004_palindrome_product():
    assert palindrome_product(100, 999) == 906609

