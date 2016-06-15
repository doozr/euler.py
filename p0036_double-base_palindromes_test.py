"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


Answer:
    872187
"""


from euler.util import is_palindrome


def to_bin(x):
    return "{0:b}".format(x)


def double_base_palindromes(limit):
    return (x for x in range(1, limit, 2) if is_palindrome(str(x)) and is_palindrome(to_bin(x)))


def test_0036_double_base_palindromes():
    assert sum(double_base_palindromes(1000000)) == 872187

