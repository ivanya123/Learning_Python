def count_decorator(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {count=}')
        return result

    return wrapper


@count_decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    add(1, 2)
    add(1, 2)
    add(1, 2)
    add(1, 2)
    add(1, 2)