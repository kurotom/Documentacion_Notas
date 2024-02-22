# -*- coding: utf-8 -*-
"""
Como los métodos de clase, los métodos de metaclases están diseñadas para manejar información `nivel-clase`.
"""


class A(type):
    def a(cls):             # método metaclase: get class
        print(cls)
        cls.x = cls.y + cls.z


class B(metaclass=A):
    y, z = 11, 22

    @classmethod            # método de clase: get class
    def b(cls):
        print(cls)
        return cls.x



if __name__ == '__main__':

    B.a()                   # call método metaclase, solo clase
    print(B.x)              # crea data en clase B, accesible por instancias

    print()

    I = B()
    print(I.x, I.y, I.z)

    print()
    print(I.b())            # método de clase, envía class, visible por instancia
    print(I.a())            # método de metaclase, accesible solo class

