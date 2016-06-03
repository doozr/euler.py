"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Answer:
    171
"""


# It has been pointed out that this can be calculated using 1200/7, where 1200 is number of months in 100 years
# and 7 is the number of potential starting days of the week. However, this is not a general solution and
# essentially an estimate, so I disregarded it. The fact it happens to work for the 20th century is irrelevant.


from datetime import datetime


def count_months_starting_with_day(start_year, end_year, day):
    return sum(1
               for year in range(start_year, end_year+1)
               for month in range(1, 13)
               if datetime(year, month, 1).weekday() == day)


def test_0019_counting_sundays():
    assert count_months_starting_with_day(1901, 2000, 6) == 171

