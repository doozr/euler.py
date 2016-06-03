"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Answer:
    837799
"""


memo = {1: 1}


def next_collatz(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


def count_collatz(n):
    if n not in memo:
        memo[n] = count_collatz(next_collatz(n)) + 1
    return memo[n]


def longest_collatz_sequence(limit):
    def is_max((ax, al), (nx, nl)):
        return (nx, nl) if nl > al else (ax, al)

    n, l = reduce(is_max,
                  ((x, count_collatz(x)) for x in range(1, limit)),
                  (0, 0))
    return n


def test_0014_longest_collatz_sequence():
    assert longest_collatz_sequence(1000000) == 837799
