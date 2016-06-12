"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
    906609
"""


from euler.util import is_palindrome


def palindrome_product(limit):
    return max(x
               for x in (y * z
                         for y in range(100, limit)
                         for z in range(100, y + 1))
               if is_palindrome(str(x)))


def test_0004_palindrome_product():
    assert palindrome_product(1000) == 906609
