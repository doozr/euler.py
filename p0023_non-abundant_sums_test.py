"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


Answer:
    4179871
"""


from euler.math import divisors


ABUNDANT_NUMBERS = frozenset(n for n in range(1, 28124) if sum(divisors(n)) > n)


def is_abundant_sum(x):
    return any(x - a in ABUNDANT_NUMBERS for a in ABUNDANT_NUMBERS)


def sum_nonabundant_numbers():
    return sum(x for x in range(1, 28124) if not is_abundant_sum(x))


def test_0023_nonabundant_sums():
    assert sum_nonabundant_numbers() == 4179871
