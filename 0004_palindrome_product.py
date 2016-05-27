"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
    906609
"""


def is_palindrome(s):
    split = int(len(s) / 2 + 1)
    return s[:split] == s[-split:][::-1]


print max(x
        for x in (y * z
            for y in range(100, 1000)
            for z in range(100, y + 1))
        if is_palindrome(str(x)))
