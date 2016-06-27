"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?


Answer:
    840
"""


from math import sqrt
from collections import Counter
from euler.iter import first
from euler.math import divides_by


def pythagorean_triples(limit):
    m = limit // 2
    return ((a, b, sqrt(a**2 + b**2)) for a in range(1, m) for b in range(1, m - a))


def integer_right_triangles(limit):
    return (int(a + b + c) for a, b, c in pythagorean_triples(limit) if divides_by(c, 1))


def max_integer_right_triangle(limit):
    return first(Counter(integer_right_triangles(limit)).most_common(1))


def test_0039_integer_right_triangles():
    assert first(max_integer_right_triangle(1000)) == 840
