"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


Answer:
    1366
"""


def power_digit_sum(x, y):
    return sum(int(z) for z in str(x**y))


def test_0016_power_digit_sum():
    assert power_digit_sum(2, 1000) == 1366