# -*- coding: utf-8 -*-
"""
Decoradores de clase:

    validador: valida los datos dados al constructor de la clase.
    extraMod: agrega método a la clase de forma automáticamente.
"""

def validador(**argumentos):
    def onDecorador(cls):
        def onCall(*args):
            keys = list(argumentos.keys())
            t = len(keys)
            for i in range(t):
                if isinstance(args[i], argumentos[keys[i]]):
                    return cls(*args)
                else:
                    msg = f"Argument '{keys[i]}' with value '{args[i]}' is not '{argumentos[keys[i]]}'"
                    raise TypeError(msg)
        return onCall
    return onDecorador


def extra(self, args):
    print(f"método extra  {args}")

def extraMod(cls):
    cls.extra = extra
    return cls


@validador(name=str, age=int, sex=str)
@extraMod
class C:
    def __init__(self, name, age, sex):
            self.name = name
            self.age = age
            self.sex = sex
    def __str__(self):
        return f'Data: {self.name}, {self.age}, {self.sex}'

c = C("Sam", 12, "F")
print(c)
print(c.__dict__)
c.extra("#valor#")

print()

c = C(12, "Bob", "M")

