def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        tuple_kwargs = tuple((key, value) for key, value in kwargs.items())
        if (args, tuple_kwargs) not in cache:
            cache[args, tuple_kwargs] = func(*args, **kwargs)
        return cache[args, tuple_kwargs]

    return wrapper


@cache_decorator
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(100))


