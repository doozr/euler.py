from collections import deque
from itertools import zip_longest
from functools import reduce


def take(seq, n):
    """
    Get the first n values in a sequence

    :param seq: The sequence to pull values from
    :param n: The number of values to pull
    :return: A generator yielding the first n values of seq
    """
    if n < 0:
        raise ValueError("Only take positive integers")
    i = iter(seq)
    return (next(i) for _ in range(n))


def take_while_incl(fn, seq):
    """
    Get values from a sequence up to and including the value that fails the predicate

    :param fn: The predicate to check each value against
    :param seq: The sequence to pull values from
    :return: A generator yielding values from seq
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

    :param seq: The sequence to pull values from
    :param step: The interval between values
    :param skip (optional): The number of values to skip before starting
    :return: A generator yielding values from seq
    """
    i = iter(seq)
    if skip is not None:
        list(take(i, skip))
        yield next(i)
    while True:
        list(take(i, step - 1))
        yield next(i)


def window(seq, n):
    """
    Get a sliding window of values over a sequence of width n

    Each window will have exactly n values unless the total length
    of the sequence is lower than n, in which case the entire sequence
    will be returned as a single window.

    e.g a sliding window of width 3 over [1, 2, 3, 4, 5] returns:

        [1, 2, 3], [2, 3, 4], [3, 4, 5]

    :param seq: The sequence to iterate over
    :param n: The width of each window
    :return: A generator yielding lists of values
    """
    if n <= 0:
        raise ValueError("Window size must be positive integer")
    it = iter(seq)
    w = deque(take(it, n), maxlen=n)
    yield list(w)
    for x in it:
        w.append(x)
        yield list(w)


def window_greedy(seq, n):
    """
    Get a sliding window of values over a sequence of widths 1 to n

    Each window will have up to n values starting with the first single
    value and ending with the last single value. If the length of the
    sequence is lower than n the entire sequence will be returned as
    a single window and the width will never be n.

    e.g a sliding window of width 3 over [1, 2, 3, 4, 5] returns:

        [1], [1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5], [5]

    :param seq: The sequence to iterate over
    :param n: The maximum width of each window
    :return: A generator yielding lists of values
    """
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
