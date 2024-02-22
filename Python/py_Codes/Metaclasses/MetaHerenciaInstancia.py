# -*- coding: utf-8 -*-
"""
* Metaclase hereda de `type`, sobreescribe `__new__`, `__init__` y `__call__` (opcional).
* Metaclases son una forma parecida a herencia en clases.
* Los atributos de Metaclases no se heredan a instancias.
* Los atributos de Metaclases son adquiridos por las clases.
* Las clases toman los atributos Metaclases desde `__class__`, los atributos de clases de `__dict__`.
* Si existe atributos de metaclases y superclases que tengan el mismo nombre, se usarán la superclase.
* Declaración `metaclass=M` se ejecutará en cada construcción de la clase o subclase que lo usa.
* Metaclases son clases (por lo general) y pueden ser funciones.

"""


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        return type.__new__(meta, classname, supers, classdict)
    
    def tostada(type):
        return 'toast'


class Super(metaclass=MetaOne):
    def spam(self):
        return 'SPAM'


class Sub(Super):
    def eggs(self):
        return 'eggs'


if __name__ == '__main__':
    print('________________')

    try:
        x = Sub()             # Instancia definida
        print(x.eggs())       # hereda de `Sub`
        print(x.spam)         # hereda de `Super`
        print(x.tostada())    # no hereda de metaclase
    except Exception as e:
        print(e)
        
    print()

    try:
        x = Sub()
        print(Sub.eggs(x))     # método propio
        print(Sub.spam(x))     # hereda de `Super`
        print(Sub.tostada())   # adquiere de metaclase
        print(Sub.tostada(x))  # no es método de clase normal, es un método de Metaclase
    except Exception as e:
        print(e)

    print()

    try:
        x = Sub()
        print(Sub.tostada)   # método de Metaclase es adquirida por `class`
        print(Sub.spam)      # método de `Super`
        print(x.spam)        # hereda de `Super`
        print(Sub.eggs)      # método de clase `Sub`
        print(x.eggs)        # método de clase `Sub`
    except Exception as e:
        print(e)

