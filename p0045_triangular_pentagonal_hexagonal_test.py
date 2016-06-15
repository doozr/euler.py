"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	   1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2,  1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	   1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


Answer:
    1533776805
"""


from itertools import count


def triangle_numbers(start=1):
    return (n * (n + 1) / 2 for n in count(start))


def pentagonal_numbers(start=1):
    return (n * (3 * n - 1) / 2 for n in count(start))


def hexagonal_numbers(start=1):
    return (n * (2 * n - 1) for n in count(start))


def is_lowest(n, *ms):
    return all(n <= m for m in ms)


def next_triangle_pentagonal_hexagonal(ft=1, fp=1, fh=1):
    ts = triangle_numbers(ft)
    ps = pentagonal_numbers(fp)
    hs = hexagonal_numbers(fh)

    t = next(ts)
    p = next(ps)
    h = next(ps)

    while not (t == p == h):
        if is_lowest(t, p, h):
            t = next(ts)
        elif is_lowest(p, t, h):
            p = next(ps)
        else:
            h = next(hs)

    return t


def test_0045_triangle_pentagonal_hexagonal():
    assert next_triangle_pentagonal_hexagonal(286, 166, 144) == 1533776805

