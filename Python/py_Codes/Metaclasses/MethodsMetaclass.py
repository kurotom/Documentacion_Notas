# -*- coding: utf-8 -*-
"""
Los métodos de Metaclases, se aplican a las clases (`cls`) en sí, no se usa `self` (instancia).

Al usar un método metaclase desde una instancia dará error `AttributeError`.
"""


class A(type):
    def x(cls):
        print('ax', cls)
    def y(cls):
        print('ay', cls)


class B(metaclass=A):
    def y(self):
        print('by', self)
    def z(self):
        print('bz', self)


if __name__ == '__main__':

    print(B.x)
    print(B.y)
    print(B.z)
    B.x()

    print('_' * 30)

    I = B()
    I.y()
    I.z()
    I.x()
