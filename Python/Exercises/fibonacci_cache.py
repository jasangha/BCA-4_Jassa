from functools import lru_cache
fib_cache = {}


def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        return 1
    else:
        value = (fib(n-1)+fib(n-2))

    fib_cache[n] = value
    return value


for n in range(1, 101):
    print(n, ":", fib(n))

#################################################################


@lru_cache(maxsize=1000)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))


for n in range(1, 101):
    print(n, ":", fib(n))
