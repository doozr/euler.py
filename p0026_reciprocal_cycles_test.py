"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


Answer:
    983
"""


# The answer is based on the fact that the cycle length of any given n's reciprocal is
# in the multiplicative order 10^k = 1(mod n). That is, the cycle length is the smallest
# value of k such that n divides cleanly into (10^k - 1) and that no value n that is
# co-prime with 10 (for this we just check only primes) ever has a cycle length
# greater than n - 1


from euler.prime import sieve


def reverse_primes(x):
    return reversed(list(sieve(x)))


def period_lengths(seq):
    return (next((n, k) for k in range(1, n) if not (10**k - 1) % n) for n in seq)


def n_with_max_reciprocal_cycle(x):
    return next(n for n, k in period_lengths(reverse_primes(x)) if k == n - 1)


def test_0026_reciprocal_cycle():
    assert n_with_max_reciprocal_cycle(1000) == 983

