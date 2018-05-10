from collections import deque
from itertools import zip_longest
from functools import reduce


def get_at(n, seq):
    """
    Get the value at offset n of a non-indexed sequence

    :param n: The index of the value to get
    :param seq: The sequence to get the value from
    :return: The value at the given sequence
    """
    return last(take(n, seq))


def take(n, seq):
    """
    Get the first n values in a sequence

        take([1, 2, 3, 4], 2)
        >> 1, 2

    :param n: The number of values to pull
    :param seq: The sequence to pull values from
    :return: A generator yielding the first n values of seq
    """
    if n < 0:
        raise ValueError("Only take positive integers")
    i = iter(seq)
    return (next(i) for _ in range(n))


def take_while_incl(fn, seq):
    """
    Get values from a sequence up to and including the value that fails the predicate

        take_while(lambda x: x < 3, [1, 2, 3, 4])
        >> 1, 2

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

        every([1, 2, 3, 4, 5, 6], 3)
        >> 3, 6

        every([1, 2, 3, 4, 5, 6], 2, 0)
        >> 1, 4

    :param seq: The sequence to pull values from
    :param step: The interval between values
    :param skip: Optional number of values to skip before starting
    :return: A generator yielding values from seq
    """
    i = iter(seq)
    if skip is not None:
        list(take(skip, i))
        yield next(i)
    while True:
        list(take(step - 1, i))
        yield next(i)


def window(seq, n):
    """
    Get a sliding window of values over a sequence of width n

    Each window will have exactly n values unless the total length
    of the sequence is lower than n, in which case the entire sequence
    will be returned as a single window.

        window([1, 2, 3, 4, 5], 3)
        >> [1, 2, 3], [2, 3, 4], [3, 4, 5]

    :param seq: The sequence to iterate over
    :param n: The width of each window
    :return: A generator yielding lists of values
    """
    if n <= 0:
        raise ValueError("Window size must be positive integer")
    it = iter(seq)
    w = deque(take(n, it), maxlen=n)
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

        window_greedy([1, 2, 3, 4, 5], 3)
        >> [1], [1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5], [5]

    :param seq: The sequence to iterate over
    :param n: The maximum width of each window
    :return: A generator yielding lists of values
    """
    if n <= 0:
        raise ValueError("Window size must be positive integer")
    it = iter(seq)
    w = deque(take(1, it), maxlen=n)
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
    """
    Map over concurrent values of multiple sequences

    For each iteration the next value of each list is passed to the function.

        zip_with(lambda x, y: (x, y), [1, 2, 3], [4, 5, 6])
        >> (1, 4), (2, 5), (3, 6)

    :param fn: The map function that accepts one value from each input
    :param args: An arbitrary number of sequences
    :return: A generator that yields the mapped values
    """
    return (fn(*xs) for xs in zip(*args))


def transpose(xss):
    """
    Transpose a 2 dimensional array made up of lists of lists

        transpose([[1, 2], [3, 4]])
        >> [[1, 3], [2, 4]]

    :param xss: A 2 dimensional array
    :return: The transposed array
    """
    return zip(*xss)


def transpose_irregular(xss):
    """
    Transpose a 2 dimensional array with an irregular number of
    fields in each row.

    Fills any gaps with None.

        transpose_irregular([[1, 2], [3, 4, 5], [6, 7]])
        >> [[1, 3, 6], [2, 4, 7], [None, 5, None]]

    :param xss: An irregular 2 dimensional array
    :return: The transposed array
    """
    return zip_longest(*xss, fillvalue=None)


def reverse(xs):
    """
    Reverse a sequence and return it as a list

    :param xs: A sequence
    :returns: A list representing the reversed sequence
    """
    return list(xs)[::-1]


def scan(fn, xs, a):
    """
    Reduce a sequence xs using function fn with starting value a
    yielding every intermediate value.

        list(scan(lambda a, x: a + x, [1, 2, 3], 0))
        >> [1, 3, 6]

    :param fn: The function to call on each element
    :param xs: The sequence to process
    :param a: The starting accumulator value
    :returns: A sequence of values produced by fn
    """
    for x in xs:
        a = fn(a, x)
        yield a


def scan_right(fn, xs, a):
    """
    Reduce the reverse of sequence xs using function fn with starting value a
    yielding every intermediate value.

        list(scan_right(lambda a, x: a + x, [1, 2, 3], 0))
        >> [3, 5, 6]

    :param fn: The function to call on each element
    :param xs: The sequence to process
    :param a: The starting accumulator value
    :returns: A sequence of values produced by fn
    """
    return reverse(scan(fn, reverse(xs), a))


def length(seq):
    """
    Get the total length of a sequence.

    This is very inefficient as it walks the whole sequence.
    Consider if you really need this very carefully.

    :param seq: A sequence
    :return: The total length of the sequence
    """
    return reduce(lambda a, _: a + 1, seq, 0)


def first(seq):
    """
    Get the first value in a sequence.

    :param seq: A sequence
    :return: The first value of the sequence
    """
    return next(iter(seq))


def last(seq):
    """
    Get the last value in a sequence.

    This is very inefficient as it walks the whole sequence.
    Consider if you really need this very carefully.

    :param seq: A sequence
    :return: The last value of the sequence
    """
    return reduce(lambda a, x: x, iter(seq))


