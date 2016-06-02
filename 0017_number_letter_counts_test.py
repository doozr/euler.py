"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


Answer:
    21124
"""


def nslen(s):
    return len(s.replace(" ", ""))

def number_letter_counts():
    one_to_nine = nslen("one two three four five six seven eight nine")
    ten_to_nineteen = nslen("ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen")
    twenty_to_ninety = nslen("twenty thirty forty fifty sixty seventy eighty ninety")
    hundred = len("hundred")
    thousand = len("thousand")
    _and = len("and")
    one = len("one")

    return one + thousand + \
           900 * hundred + \
           100 * one_to_nine + \
           100 * twenty_to_ninety + \
           891 * _and + \
           80 * one_to_nine + \
           10 * (one_to_nine + ten_to_nineteen)


def test_0017_number_letter_counts():
    assert number_letter_counts() == 21124