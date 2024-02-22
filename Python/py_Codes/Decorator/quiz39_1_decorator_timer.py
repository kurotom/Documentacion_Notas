# -*- coding: utf-8 -*-
"""
"""

from time import sleep, process_time, perf_counter


def timer(label='', trace=True):
    print("- timer")
    def onDecorator(func):
        print("-- onDecorator")
        def onCall(*args):
            print("--- onCall")
            start = perf_counter()
            result = func(*args)
            elapsed = perf_counter() - start
            if trace:
                format = '%s %s: %.5f seconds'
                values = (label, func.__name__, elapsed)
                print(format % values)
            return result
        return onCall
    return onDecorator



# Aplicado a función
@timer(">>>")
def algo():
    sleep(1)
    print("Mensaje")


# Aplicado a método de clase
class Algo:
    @timer("-->")
    def method(self):
        sleep(1)
        print("metodo de clase")

    @timer("==>")
    def methodClass(cls):
        sleep(1)
        print("classmethod ", cls)

    @staticmethod
    @timer("##>")
    def methodStatic():
        sleep(1)
        print("staticmethod")
    nada = classmethod(methodClass)


# Run function
algo()

# Run class, method, classmethod, staticmethod
a = Algo()
a.method()
a.methodClass()
a.methodStatic()
