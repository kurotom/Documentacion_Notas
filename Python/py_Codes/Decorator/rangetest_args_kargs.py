# -*- coding: utf-8 -*-
"""
**kwarg = diccionario, accede a los argumentos por medio de llaves.
*parg = tupla, accede a los argumentos por su posición.

rangetest([indice, mínimo, máximo], [...], ...)
"""


def rangetest(**argumentos):      # Validate positional arg ranges
    print('->  rangetest')
    def onDecorator(func):
        print('->  onDecorator')
        if not __debug__:       # True if "python -O main.py args..."
            print('debug on --> ' + str(func.__name__))
            return func         # No-op: call original directly
        else:                   # Else wrapper while debugging
            code      = func.__code__
            allargs   = code.co_varnames[:code.co_argcount]
            funcname  = func.__name__

            def onCall(*pargs, **kargs):
                print('->  onCall')
                expected    = list(allargs)
                positionals = expected[:len(pargs)]
                print(argumentos, pargs)
                for (argname, (low, high)) in argumentos.items():
                    if argname in kargs:
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1} no in {2}..{3}"'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1} no in {2}..{3}"'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        print('Argument "{0}" defaulted'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator



@rangetest(age=(0, 120))
def ageInfo(name, age):
    print('->  ageInfo')
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2023))
def birthday(M, D, Y):
    print('->  birthday')
    print('birthday =  {0}/{1}/{2}'.format(M, D, Y))

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)


if __name__ == '__main__':
    omitargs()
    omitargs(d=8, c=7, b=6)
    # ageInfo('Bob', 45)
    # birthday(8, 28, 2004)
    # birthday(5, D=1, Y=1963)
    #
    # class Person:
    #     def __init__(self, name, job, pay):
    #         self.job = job
    #         self.pay = pay
    #
    #     @rangetest(percent=(0.0, 1.0))
    #     def giveRaise(self, percent):
    #         self.pay = int(self.pay * (1 + percent))
    #
    #
    # sue = Person("Sue Jones", 'dev', 100)
    # sue.giveRaise(.10)
    # print(sue.pay)
    # try: sue.giveRaise(1.10)     #  Raise TypeError
    # except Exception as e: print(e)
    # print(sue.pay)
    #
    #
    # omitargs(1, 2, 3, 4)
    # omitargs(1, 2, 3)
    # omitargs(1, 2, 3, d=4)
    # omitargs(1, d=4)
    # omitargs(d=4, a=1)
    # omitargs(1, b=2, d=4)
    # omitargs(d=8, c=7, a=1)
    #
    # try: omitargs(1, 2, 3, 11)     # bad D
    # except Exception as e: print(e)
    # try: omitargs(1, 2, 11)        # bad C
    # except Exception as e: print(e)
    # try: omitargs(1, 2, 3, d=11)   # bad D
    # except Exception as e: print(e)
    # try: omitargs(11, d=4)         # bad A
    # except Exception as e: print(e)
    # try: omitargs(d=4, a=11)       # bad A
    # except Exception as e: print(e)
    # try: omitargs(1, b=11, d=4)    # bad B
    # except Exception as e: print(e)
    # try: omitargs(d=8, c=7, a=11)  # bad A
    # except Exception as e: print(e)
