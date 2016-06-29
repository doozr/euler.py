"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the divisors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?


Answer:
    76576500
"""


from itertools import count
from euler.math import divides_by, num_divisors


def first_with_n_divisors(t):
    x = y = 1
    for n in count(2):
        if divides_by(n, 2):
            y = num_divisors(n + 1)
        else:
            x = num_divisors(n // 2 + 1)
        if x * y >= t:
            return sum(range(1, n+1))


def test_0012_highly_divisible_triangle_number():
    assert first_with_n_divisors(500) == 76576500
