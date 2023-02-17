import itertools
import math


def primes():
    p = 1
    while True:
        p += 1
        if (math.factorial(p - 1) + 1) % p == 0:
            yield p


def main(n):
    print(list(itertools.takewhile(lambda x: x <= n, primes())))


if __name__ == "__main__":
    main(int(input().strip()))

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# https://stepik.org/lesson/24464/step/5?unit=6769
