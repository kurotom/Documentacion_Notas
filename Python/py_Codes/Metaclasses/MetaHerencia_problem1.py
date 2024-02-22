# -*- coding: utf-8 -*-
"""
Sobrecargar `__call__` de `SuperMetaClass(type)` teniendo métodos `__new__` retornando objeto `type` y `__call__`. Las superclases y subclases pueden tener `__init__`.

Heredan de `type`.

Problema: `Spam` adquiere `call` de SuperMetaClass, pero la creación de instancia `Spam` falla antes que sea creada una instancia.
"""


class SuperMetaClass(type):
    def __call__(meta, classname, supers, classdict):
        print('\nSuperMetaClass - call -')
        print('...classname: ', classname)
        print('...supers: ', supers)
        print('...classdict: ', classdict)
        return type.__call__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('\nSuperMetaClass - init -')
        print('...classname: ', classname)
        print('...supers: ', supers)
        print('...classdict: ', classdict)


class SubMetaClass(type, metaclass=SuperMetaClass):
    def __new__(meta, classname, supers, classdict):
        print('\nSubMetaClass - new -')
        print('...classname: ', classname)
        print('...supers: ', supers)
        print('...classdict: ', classdict)
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('\nSubMetaClass - init -')
        print('...Class: ', classname)
        print('...supers: ', supers)
        print('...classdict: ', classdict)


class Eggs:
    pass


if __name__ == '__main__':

    class Spam(Eggs, metaclass=SubMetaClass): # invoca SubMetaClass via SuperMetaClass.__call__
        data = 1
        def __init__(self):
            self.data = Spam.data

        def method(self, arg):
            return self.data + arg


    print('_' * 30 + '\n')
    x = Spam()
    print('data: ', x.data, x.method(2))

