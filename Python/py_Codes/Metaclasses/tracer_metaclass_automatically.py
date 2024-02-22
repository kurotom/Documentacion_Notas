# -*- coding: utf-8 -*-
"""
Metaclase que aplica decorador `tracer` automáticamente a métodos.

Combinando `decorators` y `metaclass`.
"""



from types import FunctionType
from tracer_decorator import tracer


class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        # itera por atributos y métodos de la clase
        for attr, attrval in classdict.items():
            # comprueba si atributo es un método
            if type(attrval) is FunctionType:
                    # decora el método
                    classdict[attr] = tracer(attrval)
        # retorna instancia `type`, construye la clase
        return type.__new__(meta, classname, supers, classdict)
