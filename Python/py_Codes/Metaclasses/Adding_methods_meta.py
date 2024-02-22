# -*- coding: utf-8 -*-
"""
Usando Metaclase para crear nuevas instancias con los métodos deseados.

Teniendo un punto central en donde se construye y retorna la instancia construida, perfecta para cambios futuros, permite reducir el error y tiempo invertido.
"""


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)


class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
        value = 'ni?'


X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


