import itertools
import math


def primes():
    p = 1
    while True:
        p += 1
        if (math.factorial(p-1) + 1) % p == 0:
            yield p
print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]