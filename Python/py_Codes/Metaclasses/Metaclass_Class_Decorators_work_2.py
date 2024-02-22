# -*- coding: utf-8 -*-
"""
Una Metaclase no puede aplazar un decorador NoMetaclass, porque la clase aún no existe hasta que la metaclase complete el llamado, puede tomar forma de un simple llamado a `type` para crear la clase directamente y pasarlo a decorador.
"""


def Metaclass(clsname, supers, attrdict):
    print("-> metaclass")
    return decorator(type(clsname, supers, attrdict))



def decorator(cls):
    print('-> decorator', cls)
    return cls


class A:
    x = 1


class B(A, metaclass=Metaclass):
    y = 3
    def m(self):
        return self.x + self.y



print(B.x, B.y)

I = B()
print(I.x, I.y, I.m())
