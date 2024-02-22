# -*- coding: utf-8 -*-
"""
Metaclases permiten agregar una capa extra de lógica a clases.

Las instancias obtienen su comportamiento de las clases, no de las metaclases.

Metaclases redefinen métodos `__new__`, `__init__`, y opcionalmente `__call__`.

Heredan de `type`, pueden tener sub-metaclases, `(type, metaclass=MetaClass)`.

Los atributos (métodos) de Metaclases no son accesibles por Instancias. Solo son accesibles por `Class`.
"""


class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('\tMetaTwo - __new__')
        print('...meta: ', meta)
        print('...classname: ', classname)
        print('...supers: ' , supers)
        print('...classdict: ', classdict)
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('\tMetaTwo - __init__')
        print('...Class: ', Class)
        print('...classname: ', classname)
        print('...supers: ' , supers)
        print('...classdict: ', classdict)
#        return type.__new__(meta, classname, supers, classdict)


class Eggs:
    # SuperClass
    pass



if __name__ == '__main__':

    class Spam(Eggs, metaclass=MetaTwo):
        data = 1
        def __init__(self):
            self.data = Spam.data

        def method(self, arg):
            return self.data + arg


    print('_' * 30 + '\n')
    x = Spam()
    print('data: ', x.data, x.method(2))
