"""
The nth term of the sequence of triangle numbers is given by, tn = n(n+1) / 2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?


Answer:
    162
"""


from os import path
from functools import reduce
from itertools import takewhile, count
from euler.iter import length


TRIANGLE_NUMBERS = set(takewhile(
    lambda x: x <= 200,
    ((n * (n + 1)) / 2
     for n in count(1))))


def load_words():
    def split_csv(l):
        return [x.strip().strip('"') for x in l.split(",")]

    cwd = path.dirname(path.realpath(__file__))
    with open(path.join(cwd, "files", "p042_words.txt")) as fd:
        return reduce(sum, (split_csv(line) for line in fd), [])


def word_scores(words):
    def char_val(c):
        return ord(c) - 64

    def word_score(w):
        return sum(char_val(c) for c in w)

    return ((word, word_score(word)) for word in words)


def triangle_words(words):
    return (word_score
            for word_score in word_scores(words)
            if word_score[1] in TRIANGLE_NUMBERS)


def test_0042_coded_triangle_numbers():
    assert length(triangle_words(load_words())) == 162

