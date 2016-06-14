"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.


Answer:
    16695334890
"""


from itertools import permutations


def list_divides_by(s, x):
    return int("".join(s)) % x == 0


def substring_divisibility():
    def _final_iteration(results):
        return ([str(d)] + p
                for p in results
                for d in xrange(0, 10)
                if str(d) not in p)

    def _subsequent_iterations(results, divisors):
        if not divisors:
            return _final_iteration(results)

        divisor = divisors[-1]
        return _subsequent_iterations(
            ([str(d)] + p
             for p in results
             for d in xrange(0, 10)
             if str(d) not in p and
             list_divides_by([str(d)] + p[:2], divisor)),
            divisors[:-1])

    def _first_iteration(divisors):
        divisor = divisors[-1]
        return (int("".join(rs))
                for rs in _subsequent_iterations((list(p)
                                                   for p in permutations("9876543210", 3)
                                                   if list_divides_by(p, divisor)),
                                                  divisors[:-1]))

    return set(_first_iteration([2, 3, 5, 7, 11, 13, 17]))


def test_0043_substring_divisibility():
    assert sum(substring_divisibility()) == 16695334890


# Original really slow way, takes 10 seconds on a 2.4GHz i5, but it's so simple!
# def substring_divisibility():
#     return sum(int("".join(p))
#                for p in permutations("9876543210")
#                if all(set_divides_by(p[y:y + 3], x)
#                       for x, y in izip(PRIMES, count(1))))

