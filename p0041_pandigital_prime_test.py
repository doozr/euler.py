import time
from itertools import permutations
from euler.prime import sieve


PRIMES = set(x for x in sieve(7654321) if x > 10 ** 6)

start = time.time()
print next(x for x in (int("".join(y)) for y in permutations('7654321')) if x in PRIMES)
end = time.time()
print "Time taken: %f seconds" % (end - start)
