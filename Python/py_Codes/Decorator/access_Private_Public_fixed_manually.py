# -*- coding: utf-8 -*-
"""
Una forma de arreglar la "vulnerabilidad" del acceso no permitido a atributos
privados, es sobre-cargar los métodos "buil-in" dentro de la clase proxy.

Esta forma tiene desventaja como aumentar la cantidad de código, toma tiempo,
y es propenso a errores.
"""
import traceback


traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    print("__ : ", failIf)
    def onDecorator(aClass):
        print("___ : ", aClass.__name__)
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)


            # Intercept and delegate built-in operations specifically
            def __str__(self):
                return str(self.__wrapped)
            def __add__(self, other):
                return self.__wrapped + other   # Or getattr(x, '__add__')(y)
            def __getitem__(self, index):
                return self.__wrapped[index]    # If needed
            def __call__(self, *args, **kargs):
                return self.__wrapped(*args, **kargs)
            # Append all built-in operations required



            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
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
    print(x._onInstance__wrapped.age)
