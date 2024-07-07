from typing import List, Optional, Sequence, Union


def type_decorator(*typing: type):

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typing):
                    raise TypeError(f"Argument must be of type {typing}")
            for key, value in kwargs.items():
                if not isinstance(value, typing):
                    raise TypeError(f"Argument {key} must be of type {typing}")
            return func(*args, **kwargs)

        return wrapper

    return real_decorator



@type_decorator(str, int)
def add(a,b):
    return a+b



if __name__ == "__main__":
    add(1,2)
    add("1","2")
    add("1","2")
    add([1,2,3], [4,5,6])

