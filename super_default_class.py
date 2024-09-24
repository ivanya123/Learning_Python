class MyList(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start if index.start else 0
            stop = index.stop if index.stop else len(self) - 1
            if stop < 0:
                stop = len(self) + stop
            if start < 0:
                start = len(self) + start
            print(f'Взять c {start} до {stop} элементы')
        else:
            if index < 0:
                k = len(self) + index
            print(f'Взять {k} элемент')
        return list.__getitem__(self, index)


class NewClass:
    kj = 1
    def __init__(self):
        self.__dict__['a'] = 1
    def __getattr__(self, item):
        print(f'Нет такого атрибута {item}')

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            print(f'Нет такого атрибута {key}')


class N:
    pass


class A(N):
    def __init__(self):
        self._c = None

    @property
    def c(self):
     return self._c

    @c.setter
    def c(self, value):
     self._c = value


class tracer:
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Вызов функции {self.count} раз')
        return self.func(*args, **kwargs)


@tracer
def f(x):
    return x + 1


if __name__ == '__main__':
    a = A()
    a.c = 3
    print(a.c)
    print(type(f))
    f(1)
    f(2)
    f(3)
    f(4)
    f(5)
    print(object.__bases__)
