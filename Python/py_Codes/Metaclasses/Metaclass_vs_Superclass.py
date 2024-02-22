# -*- coding: utf-8 -*-
"""
Instancia no tiene acceso a métodos y atributos de Metaclase.

La clase que usa la Metaclase tiene acceso a sus atributos y métodos.

Una instancia o clase que tenga metaclase puede acceder a los métodos y atributos de esta usando `__class__`.
"""


def metaclass():
    class A(type):
        attr = 1
        def hi(self):
            return 'from metaclass: A'

    class B(object, metaclass=A):
        pass

    x = B()
    print(B.attr)
    print(B.hi())
    try:
        print(x.attr)
    except Exception as e:
        print('>', e, '\n')
    try:
        print(x.hi())
    except Exception as e:
        print('>', e, '\n')
    print(B.__dict__)
    print(B.__class__)
    print()
    print(A.__dict__)
    print(A.__class__)

    print('attr' in B.__dict__, 'attr' in A.__dict__)



def superclass():
    class A(object):
        attr = 1
        def hi(self):
            return 'from metaclass: A'
        def bye():
            return 'bye from metaclass: A'

    class B(A):
        pass

    x = B()
    print(B.attr)
    print(B.hi(B))
    print(B.bye())

    print(x.attr)
    print(x.hi())

    print()
    print(B.__dict__)
    print(B.__class__)
    print()
    print(A.__dict__)
    print(A.__class__)
    
    print('attr' in B.__dict__, 'attr' in A.__dict__)


def metaclass_superclass():
    class M(type):
        attr = 1
        def hi(self):
            return 'from metaclass: M'

    class A(object):
        id = 100
        def a(self):
            return 'from superclass: A'

    class B(A, metaclass=M):
        pass

    x = B()
    print(B.__mro__)
    print(x.id)
    print(x.a())
    try:
        print(x.attr)
    except Exception as e:
        print('>', e, '\n')
    try:
        print(x.hi())
    except Exception as e:
        print('>', e, '\n')

    print(B.attr)
    print(B.hi())

    print()

    print(A.id)
    print(A.a(A))

    print('_' * 30)

    print(M.__dict__)
    print(M.__class__)
    print()
    print(B.__dict__)
    print(B.__class__)
    print()
    print(A.__dict__)
    print(A.__class__)

    print()
    print('attr' in B.__dict__, 'attr' in A.__dict__, 'attr' in M.__dict__)

    print()
    print(B.__class__.hi(B))
    print(x.__class__.hi())
    print(B.__bases__)

if __name__ == '__main__':
    metaclass()
    
    print('#' * 30)

    superclass()

    print('#' * 30)

    metaclass_superclass()
