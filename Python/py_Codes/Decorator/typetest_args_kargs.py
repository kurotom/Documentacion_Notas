# -*- coding: utf-8 -*-
"""
Decorador que comprueba el tipo de los datos al momento de llamar a la función
que se le aplique.
"""


def typetest(**argumentos):
    print("--> typetest")
    def onDecorator(func):
        print("--> onDecorator")
        if not __debug__:       # True if "python -O main.py args..."
            print('debug on --> ' + str(func.__name__))
            return func         # No-op: call original directly
        else:                   # Else wrapper while debugging
            code      = func.__code__
            allargs   = code.co_varnames[:code.co_argcount]
            funcname  = func.__name__
            def onCall(*args, **kwargs):
                print("--> onCall")
                positionals = list(allargs)[:len(args)]
                print(args, kwargs, argumentos)
                for (argname, type) in argumentos.items():
                    if argname in kwargs:
                        print("--> Keywords")
                        if not isinstance(kwargs[argname], type):
                            msg = '>>  "{0}"  not is type: "{1}"  <<'
                            errmsg = msg.format(kwargs[argname], type)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        print("--> Positionals")
                        position = positionals.index(argname)
                        if not isinstance(args[position], type):
                            msg = '>>  "{0}"  not is type: "{1}"  <<'
                            errmsg = msg.format(args[position], type)
                            raise TypeError(errmsg)
                    else:
                        print('Argument "{0}" defaulted'.format(argname))
                return func(*args, **kwargs)
            return onCall
    return onDecorator



@typetest(a=int, b=float)
def funcion(a, b, c, d):
    print(a, b, c, d)


funcion(1, 2, 3, 4)
funcion('spam', 2.0, 3, 4)
