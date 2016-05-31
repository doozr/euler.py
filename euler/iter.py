from collections import deque
from itertools import izip, izip_longest


def window(seq, n):
    it = iter(seq)
    win = deque((next(it) for _ in xrange(n)), maxlen=n)
    yield win
    for e in it:
        win.append(e)
        yield win


def zipwith(fn, *args):
    return (fn(*xs) for xs in izip(*args))


def transpose(xss):
    return izip(*xss)


def transpose_irregular(xss):
    return ((x for x in xs if x is not None) for xs in izip_longest(*xss, fillvalue=None))


def reverse(xs):
    return list(xs)[::-1]


