import time


def log_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open('log.txt', 'a') as f:
            f.write(str(func.__name__) + '\n')
            f.write(f'Arguments: {args}, {kwargs} \n')
            f.write('Time:' + str(end_time - start_time) + '\n\n')
        return result

    return wrapper


@log_dec
def add(a, b):
    return a + b


if __name__ == '__main__':
    add(b=1, a=2)
    add(4, 7)
