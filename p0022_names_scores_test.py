"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
 alue by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?


Answer:
    871198282
"""


from os import path
from itertools import izip, count


def load_names():
    def split_csv(l):
        return [x.strip().strip('"') for x in l.split(",")]

    cwd = path.dirname(path.realpath(__file__))
    with open(path.join(cwd, "files", "p022_names.txt")) as fd:
        return reduce(sum, (split_csv(line) for line in fd), [])


def names_scores(names):
    def char_val(c):
        return ord(c) - 64

    return sum(
        index * sum(char_val(char) for char in name)
        for name, index
        in izip(sorted(names), count(1)))


def test_0022_names_scores():
    assert names_scores(load_names()) == 871198282
