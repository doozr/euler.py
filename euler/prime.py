from itertools import count


def is_prime(x):
    return x in sieve(x + 1)


def primes():
    return (x for x in count() if is_prime(x))


def sieve(upper_bound):
    marked = [0] * upper_bound
    yield 2
    for value in (x for x in xrange(3, upper_bound, 2) if marked[x] == 0):
        yield value
        for i in xrange(value, upper_bound, value):
            marked[i] = 1


def prime_factors(n):
    if n == 2 or n == 3:
        yield n
        return
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
            yield i
        i += 1
    if n > 1:
        yield n


