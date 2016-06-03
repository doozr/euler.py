def divisors(n):
    i = 1
    while i * i < n:
        if n % i == 0:
            yield i
            if i != 1:
                yield n / i
        i += 1



