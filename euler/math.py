from operator import mul


def divisors(n):
    def _divisors():
        i = 1
        while i * i < n:
            if n % i == 0:
                yield i
                if i != 1:
                    yield n / i
            i += 1
        if i * i == n:
            yield i
    return list(_divisors())


def muls(seq):
    return reduce(mul, seq, 1)


def fib():
    x = 0
    y = 1
    yield y
    while True:
        x, y = y, x + y
        yield y


def factorial(x):
    return 1 if x == 0 else reduce(mul, xrange(2, x + 1), 1)
