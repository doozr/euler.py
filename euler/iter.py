from collections import deque
from itertools import zip_longest
from functools import reduce


def take(seq, n):
    return (next(seq) for _ in range(n))


def take_until(fn, seq):
    for x in seq:
        yield x
        if fn(x):
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
    return (fn(*xs) for xs in zip(*args))


def transpose(xss):
    return zip(*xss)


def transpose_irregular(xss):
    return ((x for x in xs if x is not None) for xs in zip_longest(*xss, fillvalue=None))


def reverse(xs):
    return list(xs)[::-1]


def scan(fn, xs, a):
    for x in xs:
        a = fn(a, x)
        yield a


def scan_right(fn, xs, a):
    return reverse(scan(fn, reverse(xs), a))


def length(seq):
    return reduce(lambda a, _: a + 1, seq, 0)


def first(seq):
    return next(iter(seq))
