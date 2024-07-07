def retry(n):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            while count < n:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    count += 1
                    print(f"Attempt {count}/{n} failed with error: {e}")
                    if count == n:
                        raise
        return wrapper
    return real_decorator

@retry(3)
def add(a, b):
    return a + b

if __name__ == '__main__':
    add(1, '2')