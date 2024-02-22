# -*- coding: utf-8 -*-
"""
Un Decorador de clase en esencia puede realizar el rol del método `__init__` de Metaclase, porque retorna una instancia de Metaclase, o una de superclase `type`.

Al usar un decorador que retorne una instancia de metaclase, agrega un paso extra al momento de creación de la clase.
"""


class Metaclass(type):
    def __init__(meta, clsname, supers, attrdict):
        print('>> INIT', clsname)

    def __new__(meta, clsname, supers, attrdict):
        print('In M.__new__:')
        print([clsname, supers, list(attrdict.keys())])
        return type.__new__(meta, clsname, supers, attrdict)


def decorator(cls):
    return Metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))



class A:
    x = 1


@decorator
class B(A):
    """
    Usa decorador que retorna una instancia Metaclass.
    Agrega un paso extra al tiempo de construcción.
    """
    y = 2
    def m(self):
        return self.x + self.y


class C(A, metaclass=Metaclass):
    """
    Mismo efecto, pero solamente usa una clase.
    """
    z = 3


print(B.x, B.y)

I = B()
print(I.x, I.y, I.m())


print(C.x, C.z)
