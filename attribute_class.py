from typing import Any


class Attribute():
    def __init__(self):
        self.name = "Polina"
        self.age = 20

    def __str__(self):
        text = ''
        for key, value in self.__dict__.items():
            text += f"{key}: {value}; "
        return text.strip()


def set_attr(obj: Attribute, values: dict[str, Any]):
    for key, value in values.items():
        obj.__dict__[key] = value

    return obj


if __name__ == '__main__':
    polina = Attribute()
    print(polina)
    dict_ivan = {
        'name': 'Ivan',
        'age': 28
    }
    ivan = set_attr(polina, dict_ivan)
    print(ivan)
    ivan.name = 'Stepan'
    ivan.__dict__['name'] = 'Stepan'
    print(ivan)
    func = lambda x:x
    print(func.__dict__)
    kljfgla = Attribute()