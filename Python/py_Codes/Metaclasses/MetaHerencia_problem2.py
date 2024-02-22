# -*- coding: utf-8 -*-
"""
En este caso, la superclase es saltada por "built-ins", no es capta explícitamente y llama, este último se basa en la herencia normal de nombres de atributos.
"""

class SuperMetaClass(type):
    def __call__(meta, classname, supers, classdict):   # por nombre no "built-in" (type)
        print('SuperMetaClass - call -')
        print('classname:  ', classname)
        return type.__call__(meta, classname, supers, classdict)



class SubMetaClass(SuperMetaClass):  # creado por `type` por defecto
    def __init__(Class, classname, supers, classdict):  # sobre-escribe  `type.__init__`
        print('SubMetaClass - init -')
        print('classname:  ', classname)



print(SubMetaClass.__class__)
print([n.__name__ for n in SubMetaClass.__mro__])

print()

# ninguna data es encontrada por nombre
print(SubMetaClass.__call__)

print()

# Explícitamente `__call__`, herencia de clase
SubMetaClass.__call__(SubMetaClass, 'xxx', (), {})

print()

# implícitamente llama por `__call__`, no `type`
SubMetaClass('yyy', (), {})
