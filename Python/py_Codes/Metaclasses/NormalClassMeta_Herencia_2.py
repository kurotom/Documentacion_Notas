# -*- coding: utf-8 -*-
"""
Clase Común y Corriente que hereda de otra clase, con métodos `__init__` y `__new__` sobrecargado y llamados mediante método `__call__` de la super clase.
"""

class METAMETA(object):
    print('METAMETA')
    def __call__(self, classname, supers, classdict):
        print('METAMETA - call')
        Class = self.__NEW__(classname, supers, classdict)
        self.__INIT__(Class, classname, supers, classdict)
        return Class

class MetaObj(METAMETA):
    def __call__(self, classname, supers, classdict):
        print('MetaObj.call')
        return super().__call__(classname, supers, classdict)

    def __NEW__(self, classname, supers, classdict):
        print('MetaObj.new')
        return type(classname, supers, classdict)

    def __INIT__(self, Class, classname, supers, classdict):
        print('MetaObj.init')
        print('..init class object: ', list(Class.__dict__.keys()))


class Eggs:
    pass


if __name__ == '__main__':
    class Spam(Eggs, metaclass=MetaObj()):
        data = 1
        def method(self, arg):
            return self.data + arg


    print('_' * 30)
    x = Spam()
    print('data: ', x.data, x.method(2))
