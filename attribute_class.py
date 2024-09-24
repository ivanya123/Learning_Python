import tkinter

import os_ob as o


class ListInheridted:
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)*4
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += f'{spaces}{attr}\n'
            else:
                result += f'{spaces}{attr} = {getattr(obj, attr)}\n'
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent*4
        if aClass in self.__visited:
            return f'\n{dots}<Class {aClass.__name__} address {id(aClass)}: (see above)>\n'
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent + 1)
            return f'\n{dots}<Class {aClass.__name__}, address {id(aClass)}:\n{here}{above}{dots}>\n'

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 0)
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{here}{above}>\n'

class AttributeClass(ListInheridted, tkinter.Tk):
    new = 1
    def __init__(self):
        self.name = '213'
        self.value = '112'
        self.type = '333'
        self.is_static = False
        self.is_const = False
        self.is_volatile = False
        self.is_inline = False
        self.is_extern = False
        self.is_virtual = False
        self.is_pure_virtual = False
        self.is_friend = False
        self.is_typedef = False
        self.is_template = False
        self.is_operator = False
        self.is_constructor = False
        self.is_destructor = False

    def plus(self):
        return 'sdada'


n = AttributeClass()

print(n)
