#! -*- coding: utf-8 -*-
"""
Descriptores tienen precedencia, se ejecutan para evitar reasignación en `__class__` y `__dict__`.

Es automático en descriptores Python por defecto, o al crear descriptores.
"""


class D:
    def __get__(self, instance, owner):
        print('__get__')
    def __set__(self, instance, value):
        print('__set__')



class C:
    d = D()


if __name__ == '__main__':

    I = C()
    I.d
    I.d = 1
    I.d
    I.__dict__['d'] = 'spam'
    print(I.__dict__)
    I.d
    print(I.__dict__['d'])



