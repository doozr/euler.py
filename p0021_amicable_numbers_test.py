"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


Answer:
    31626
"""


def divisors(n):
    i = 1
    while i * i < n:
        if n % i == 0:
            yield i
            if i != 1:
                yield n / i
        i += 1


def d(n):
    return sum(divisors(n))


# Could be improved by using a "seen" list and yielding both halves
# of the pair at the same time but it's only marginally faster and this
# is way cooler. One liners for the win!
#
# Check d(d(n)) == n first so it's faster. Checking d(n) != n first for
# every number slows it down by 25%. For limit = 10000 there are only
# 4 numbers (6, 28, 496 and 8128) where n == d(n) == d(d(n)) so we can
# minimise how often the check runs by having it second. There are 10
# amicable numbers (5 pairs) < 10000 so we end up doing the check 10
# times instead of 10000 times. Much better.
def amicable_numbers(limit):
    return (n
            for n in xrange(1, limit + 1)
            if d(d(n)) == n and d(n) != n)


def sum_amicable_numbers(limit):
    return sum(amicable_numbers(limit))


def test_0021_amicable_numbers():
    assert sum_amicable_numbers(10000) == 31626

