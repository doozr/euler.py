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
