# -*- coding: utf-8 -*-
"""
"""


def herencia_super():
    class D(type):
        def __str__(self):
            return ('--> D class')

    class C(D):
        pass

    print((C.__str__(C), str(C))) # Explícito => super, built-in => metaclass
    print(C.__str__)
    for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])


def herencia_super_str():
    class D(type):
        def __str__(self):
            return ('--> D class')

    class C(D):
        def __str__(self):
            return ('==> C class')

    print((C.__str__(C), str(C))) # Explícito => class, built-in => metaclass
    print(C.__str__)
    for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])


def metaclass_class_str():
    class D(type):
        def __str__(self):
            return ('--> D class')

    class C(metaclass=D):
        def __str__(self):
            return ('==> C class')

    print((C.__str__(C), str(C))) # Built-in => user-defined metaclass
    print(C.__str__)
    for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])


def metaclass_str():
    class D(type):
        def __str__(self):
            return ('--> D class')

    class C(metaclass=D):
        pass

    print((C.__str__(C), str(C))) # Built-in => user-defined metaclass
    print(C.__str__)
    for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])



def str_object():
    class D(type):
        def __str__(self):
            return ('--> D class')

    class C(metaclass=D):
        pass

    print((C.__str__(C), str(C))) # explícito => object, built-in => metaclass
    print(C.__str__)

    for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])


if __name__ == '__main__':
    herencia_super()

    print()

    herencia_super_str()

    print()

    metaclass_class_str()

    print()

    metaclass_str()

    print()

    str_object()
