"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


Answer:
    4782
"""


from itertools import izip, count
from euler.math import fib


def fib_index(predicate):
    return next(ix for f, ix in izip(fib(), count(1)) if predicate(f))


def lowest_fib_with_length(n):
    return fib_index(lambda f: f >= n)


def test_0025_1000_digit_fibonacci_number():
    assert lowest_fib_with_length(10**999) == 4782
