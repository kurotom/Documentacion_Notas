# -*- coding: utf-8 -*-
"""
Usando un Descriptor como solución, permite generar los métodos automáticamente
desde una lista, siendo creados al momento de llamado, mediante un descriptor
de nivel clase.

Es más complejo que escribir manualmente los operadores "built-in" y crear una
clase 'Mixin', pero es la forma más eficiente debido a que se crea
automáticamente los métodos al momento del llamado.
"""

import traceback

class BuiltinsMixin:
    class ProxyDesc(object):
        def __init__(self, attrname):
            self.attrname = attrname
        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)     # Assume a _wrapped

    builtins = ['add', 'str', 'getitem', 'call']                                  # Plus any others
    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))




traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    print("__ : ", failIf)
    def onDecorator(aClass):
        print("___ : ", aClass.__name__)
        class onInstance(BuiltinsMixin):
            def __init__(self, *args, **kargs):
                self._wrapped = aClass(*args, **kargs)      # use self._wrapped instead of self.__wrapped

            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self._wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self._wrapped, attr, value)
        return onInstance
    return onDecorator



def Private(*attributes):
    print("_ : ", " ".join(map(str, attributes)))
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    print("_ : ", " ".join(map(str, attributes)))
    return accessControl(failIf=(lambda attr: attr not in attributes))



if __name__ == "__main__":
    traceMe = True

    @Private('age')
    class Person():
        def __init__(self):
            self.age = 42
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    x = Person()

    try:
        x.age
    except Exception as e:
        traceback.print_exc()
        print("")

    print(x)        # __getattr__ => runs Person.__str__
    print("")

    try:
        x + 10          # __getattr__ => runs Person.__add__
    except Exception as e:
        traceback.print_exc()
        print("")

    print(x)        # __getattr__ => runs Person.__str__


    print("\nRompiendo la privacidad")
    x.__add__(10)
    print(x._wrapped.age)
