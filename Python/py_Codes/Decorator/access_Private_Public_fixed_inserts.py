# -*- coding: utf-8 -*-
"""
Una alternativa a agregar manualmente, Mixin, descriptor, es insertar a la
clase los métodos '__getattribute__' y `__setattr__`, los cuales interceptarán
todos las referencias y asignación de atributos realizdas en las instancias.

Estos métodos debe pasar las peticiones válidas a su superclase para evitar
loops.
"""
import traceback


traceMe = False


def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get: ', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)
        def setattributes(self, attr, value):
            trace('set: ', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__setattr__(self, attr, value)

        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes
        print(aClass.__dict__)
        return aClass
    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))



if __name__ == "__main__":
    traceMe = True

    @Private('age')
    class Person:
        def __init__(self):
            self.age = 42
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    x = Person()
    print("algo")


    # try:
    #     x.age
    # except Exception as e:
    #     traceback.print_exc()
    #     print("")
    #
    # print(x)        # __getattr__ => runs Person.__str__
    # print("")
    #
    # try:
    #     x + 10          # __getattr__ => runs Person.__add__
    # except Exception as e:
    #     traceback.print_exc()
    #     print("")
    #
    # print(x)        # __getattr__ => runs Person.__str__
    #
    #
    # print("\nRompiendo la privacidad")
    # x.__add__(10)
