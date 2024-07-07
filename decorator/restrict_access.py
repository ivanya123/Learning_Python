class Users:
    pass


u_1 = Users()
u_2 = Users()
u_1.key = 'Access'


def restrict_access(func):
    def wrapper(*args, user: Users, **kwargs):
        if 'key' in user.__dict__:
            if user.key == 'Access':
                return func(*args, user, **kwargs)
        else:
            print('Отказано в доступе')

    return wrapper


@restrict_access
def add(a, b, user: Users):
    return a, b


if __name__ == '__main__':
    print(add(2, 3, user=u_1))
    print(add(2, 3, user=u_2))


