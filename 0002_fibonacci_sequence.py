from itertools import islice, takewhile

def fib():
    x = 0
    y = 1
    while True:
        x, y = y, x + y
        yield y

print sum(x for x in takewhile(lambda y: y < 4000000, fib()) if not x % 2)
