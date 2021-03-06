"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
    6857
"""


from euler.prime import prime_factors
from euler.iter import last


def highest_prime_factor(n):
    return last(prime_factors(n))


def test_0003_prime_factors():
    assert highest_prime_factor(600851475143) == 6857
