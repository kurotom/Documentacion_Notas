# -*- coding: utf-8 -*-
"""
Una metaclase no necesariamente debe retornar una instancia `type`, cualquier objeto compatible puede hacerlo.
"""


def func1(name, supers, attrs):
    print('> func1', name)
    return 'spam'


class C(metaclass=func1):
    attr = 'huh?'


print(C, C.upper())




def func2(cls):
    print('> func2', cls)
    return 'spam'


@func2
class C:
    attr = 'huh?'


print(C, C.upper())

