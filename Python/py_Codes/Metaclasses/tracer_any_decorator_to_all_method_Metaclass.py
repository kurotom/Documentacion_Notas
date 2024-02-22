# -*- coding: utf-8 -*-
"""
Se puede aplicar cualquier decorador a todos los métodos de una clase mediante una capa extra exterior que contenga el decorador deseado.
"""


from types import FunctionType
from tracer_decorator import tracer, timer


def decorateAll(decorator):
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate



