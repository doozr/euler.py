"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


Answer:
    104743
"""


from euler.prime import sieve
from euler.iter import take, last


def nth_prime(n):
    # 200000 should be enough ...
    # The actual 10001st prime is 104743 so 104744 would be enough
    # but given the calculation is lazy it doesn't make a lot of
    # difference. Just storage size of the cache
    return last(take(n, sieve(104744)))


def test_10001st_prime():
    assert nth_prime(10001) == 104743
