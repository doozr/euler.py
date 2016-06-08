from collections import deque
from itertools import izip, izip_longest


def take(seq, n):
    return (next(seq) for _ in xrange(n))


def take_until(pred, seq):
    for x in seq:
        yield x
        if pred(x):
            break

def window(seq, n):
    it = iter(seq)
    w = deque(take(it, n), maxlen=n)
    yield w
    for x in it:
        w.append(x)
        yield w


def window_greedy(seq, n):
    it = iter(seq)
    w = deque(take(it, 1), maxlen=n)
    yield w
    for x in it:
        w.append(x)
        yield w
    while True:
        w.popleft()
        if not len(w):
            break
        yield w


def zip_with(fn, *args):
    return (fn(*xs) for xs in izip(*args))


def transpose(xss):
    return izip(*xss)


def transpose_irregular(xss):
    return ((x for x in xs if x is not None) for xs in izip_longest(*xss, fillvalue=None))


def reverse(xs):
    return list(xs)[::-1]


def scan(fn, xs, a):
    for x in xs:
        a = fn(a, x)
        yield a


def scan_right(fn, xs, a):
    return reverse(scan(fn, reverse(xs), a))
