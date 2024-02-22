# -*- coding: utf-8 -*-
"""
Usando clase 'Mixin' permite establecer el código una vez en una superclase y
sea usado en todas las subclases que las requieran, disminuye la cantidad de
código escritor, pero aún toma tiempo y es propensa a errores, pero es más
práctica que escribir manualmente cada método "built-in" en la clase proxy.

La clase 'Mixin' asume el nombre del la instancia usada dentro del constructor
de clase proxy, deben ser iguales.
"""
import traceback

traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


class BuiltinsMixin:
    def __add__(self, other):
        return self._wrapped + other        # Assume a _wrapped
    def __str__(self):                      # Bypass __getattr__
        return str(self._wrapped)
    def __getitem__(self, index):
        return self._wrapped[index]
    def __call__(self, *args, **kargs):
        return self._wrapped(*args, **kargs)
    # plus any others needed



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
