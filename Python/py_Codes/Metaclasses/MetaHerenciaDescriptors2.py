# -*- coding: utf-8 -*-
"""
En este caso el descriptor `D` tiene solamente `__get__` por lo que los otros métodos mágicos como `__set__`, `__delete__` son puestos automáticamente por Python.
"""


class D:
    def __get__(self, instance, owner):
        print('__get__')



class C:
    d = D()


if __name__ == '__main__':

    I = C()
    I.d
    I.__dict__['d'] = 'spam'
    I.d
    print(I.__dict__)
    print(I.__dict__['d'])

