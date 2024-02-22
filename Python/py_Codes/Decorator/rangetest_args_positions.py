# -*- coding: utf-8 -*-
"""
Usar decoradores para validar automáticamente los atributos dados.

Funciona mediante posicionamiento de los argumentos.

rangetest([indice, mínimo, máximo], [...], ...)
"""


def rangetest(*argumentos):      # Validate positional arg ranges
    print('->  rangetest')
    def onDecorator(func):
        print('->  onDecorator')
        if not __debug__:       # True if "python -O main.py args..."
            print('debug on --> ' + str(func.__name__))
            return func         # No-op: call original directly
        else:                   # Else wrapper while debugging
            def onCall(*args):
                print('->  onCall')
                for (ix, low, high) in argumentos:
                    print({ix: [args[ix], low]}, {ix: [args[ix], high]})
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator


# 1 = age
@rangetest((1, 0, 120))
def ageInfo(name, age):
    print('->  ageInfo')
    print('%s is %s years old' % (name, age))

# 0 = M, 1 = D, 2 = Y
@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2023])
def birthday(M, D, Y):
    print('->  birthday')
    print('birthday =  {0}/{1}/{2}'.format(M, D, Y))


if __name__ == '__main__':
    ageInfo('Bob', 45)
    birthday(8, 28, 2004)

    class Person:
        def __init__(self, name, job, pay):
            self.job = job
            self.pay = pay

        @rangetest([1, 0.0, 1.0])
        def giveRaise(self, percent):
            self.pay = int(self.pay * (1 + percent))


    sue = Person("Sue Jones", 'dev', 100)
    sue.giveRaise(.10)
    print(sue.pay)
    try: sue.giveRaise(1.10)     #  Raise TypeError
    except Exception as e: print(e)
    print(sue.pay)
