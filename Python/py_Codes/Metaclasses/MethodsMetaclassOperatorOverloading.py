# -*- coding: utf-8 -*-
"""
Metaclases puede tener métodos sobre-cargados.

`__getitem__` diseñado para clase
`__getattr__` diseñado para instancia de clase, no instancias normales.
"""


class A(type):
    
    def __getitem__(cls, i):           # metodo metaclase, procesa class
        print('A - __getitem__')
        return cls.data[i]             # "built-ins" se saltan las clases, usa metaclase
                                       # nombre explícito busca `class` + `meta`

    def __getattr__(cls, name):        # adquirido por clase B getitem
        print('A - __getattr__')
        return getattr(cls.data, name) # no resulta igual para "built-ins"


class B(metaclass=A):                  # data descriptor en meta es usado primero
    data = 'spam'



if __name__ == '__main__':
    print(B[0])                        # nombre instancia metaclase, solo clases
    print(B.__getitem__)

    print(B.upper())
    print(B.upper)
    print(B.__getattr__)



    I = B()
    print(I.data, B.data)              # nombes hereados normalmente, visible para instancia y clase.
    try:
        print(I[0])                    # no disponible para instancia
    except Exception as e:
        print(e)

    try:
        print(I.upper)                 # no disponible para instancia
    except Exception as e:
        print(e)

    try:
        print(I.__getattr__)           # no disponible para instancia
    except Exception as e:
        print(e)


    B.data = [1,2,3]
    B.append(4)
    print(B.data)
    print(B.__getitem__(0))
    print(B[0])
