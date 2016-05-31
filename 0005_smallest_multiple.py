"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
    232792560
"""

# For each value that the accumulator does not already divide by,
# multiply the accumulator by the lowest integer that makes it divide by
# both the old accumulator and the new value
assert reduce(
    lambda acc, x: acc * next(y for y in range(1, x + 1) if (acc * y) % x == 0),
    range(2, 21),
    1
) == 232792560
