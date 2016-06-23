from time import time


def is_palindrome(x):
    s = str(x)
    split = int(len(s) / 2 + 1)
    return s[:split] == s[-split:][::-1]


def ms(t=None):
    if not t:
        t = time()
    return int(t * 1000)


def ms_timer(fn):
    s = ms()
    fn()
    e = ms()
    return e - s
