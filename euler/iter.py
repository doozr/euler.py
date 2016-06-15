from collections import deque
from itertools import zip_longest
from functools import reduce


def take(seq, n):
    """
    Get the first n values in a sequence

    Args:
        seq: The sequence to pull values from
        n: The number of values to pull

    Returns:
        A generator yielding the first n values of seq
    """
    if n < 0:
        raise ValueError("Only take positive integers")
    i = iter(seq)
    return (next(i) for _ in range(n))


def take_while_incl(fn, seq):
    """
    Get values from a sequence up to and including the value that fails the predicate

    Args:
        fn: The predicate to check each value against
        seq: The sequence to pull values from

    Returns:
        A generator yielding values from seq
    """
    for x in seq:
        yield x
        if not fn(x):
            break


def every(seq, step, skip=None):
    """
    Get every nth value with interval step, optionally skipping some values

    Specify a skip of 0 to retrieve the first value of seq, otherwise (step - 1)
    will be skipped as part of the normal step interval

        every([1, 2, 3, 4], 2)
        >> (2, 4)

        every([1, 2, 3, 4], 2, 0)
        >> (1, 3)

    Args:
        seq: The sequence to pull values from
        step: The interval between values
        skip (optional): The number of values to skip before starting

    Returns:
        A generator yielding values from seq
    """
    i = iter(seq)
    if skip is not None:
        list(take(i, skip))
        yield next(i)
    while True:
        list(take(i, step - 1))
        yield next(i)


def window(seq, n):
    if n <= 0:
        raise ValueError("Window size must be positive integer")
    it = iter(seq)
    w = deque(take(it, n), maxlen=n)
    yield list(w)
    for x in it:
        w.append(x)
        yield list(w)


def window_greedy(seq, n):
    if n <= 0:
        raise ValueError("Window size must be positive integer")
    it = iter(seq)
    w = deque(take(it, 1), maxlen=n)
    yield list(w)
    for x in it:
        w.append(x)
        yield list(w)
    while True:
        w.popleft()
        if not len(w):
            break
        yield list(w)


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
