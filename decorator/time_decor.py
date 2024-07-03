import time
from decorator.cache_decor import cache_decorator


def time_decor(func):
    func._recursion_depth = 0

    def wrapper(*args, **kwargs):
        func._recursion_depth += 1
        if func._recursion_depth == 1:
            start = time.time()
        result = func(*args, **kwargs)
        if func._recursion_depth == 1:
            end = time.time()
            print(f"{func.__name__} took {end - start} seconds")
        func._recursion_depth -= 1
        return result

    return wrapper


@time_decor
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@time_decor
@cache_decorator
def fibonacci_cache(n):
    if n <= 1:
        return n
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci_cache(33))
