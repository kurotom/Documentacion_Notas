# -*- coding: utf-8 -*-
"""
Decorador para aplicar a todos los métodos.

Retorna la clase orginal aumentada, no un *wrapper* como con Metaclases.
"""


from types import FunctionType
from tracer_decorator import tracer, timer


def decorateAll(decorator):
    def DecoDecorate(aClass):
        print(">> DecoDecorate")
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass, attr, decorator(attrval))
        return aClass
    return DecoDecorate



