# -*- coding: utf-8 -*-
"""
Decorador 'Private' restringe acceso a atributos privados de forma similar a
Java.

En Python, se debe crear una clase para que filtre los atributos, impidiendo
acceso externo, pero manteniendo acceso dentro de la clase por sus métodos.

Usando *delegación* (patrón de diseño), operadores sobrecargados '__getattr__'
y '__setattr__', validación de atributos.

Dependiendo de las entradas dadas al decorador 'Private', se filtrará el acceso
a los atributos, validando el acceso o no.

Usando Python 2.X funcionará correctamente la delegación en operaciones
'built-in' debido al estilo clásico que permite el uso de clases embebidas (no
se las saltan).

Usando Python 3.X no funcionará la delegación en operaciones 'built-in' porque
el nuevo estilo no captura clases embebidas, los métodos '__add__', '__str__'
se saltan '__getattr__'. Implícitamente las clases heredan de superclase
'object'.
"""

import traceback

traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def print_args(name, *args):
    print(name + ' :  ' + ' '.join(map(str, args)))


def Private(*privates):                              # privates in enclosing scope
    print_args("privates attributes", *privates)
    def onDecorator(aClass):                 # aClass in enclosing scope
        print("Class name: ", aClass.__name__)
        class onInstance:                      # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):        # My attrs don't call getattr
                trace('get:', attr)                # Others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    print("\tValidated and delegated to " + aClass.__name__)
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):           # Outside accesses
                trace('set:', attr, value)                   # Others run normally
                print(self.__dict__)
                if attr == 'wrapped':                      # Allow my attrs
                    self.__dict__[attr] = value     # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)  # Wrapped obj attrs
        return onInstance               # Or use __dict__
    return onDecorator



if __name__ == '__main__':
    traceMe = True
    @Private('data', 'size')
#    Doubler = Private(...)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                     # Accesses inside the subject class
            self.data = start                       # Run normally
        def size(self):
            return len(self.data)               # Methods run with no checking
        def double(self):                             # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))


    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])

    print()
    print(X.label)      # Accesses outside subject class
    X.display(); X.double(); X.display()    # Intercepted: validated, delegated
    X.label = "NADA"
    X.display()

    print()

    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()

    print()


    # Fallarán porque están declarados Private, __getattr__ y __setattr__
    try: print("Intentando acceder a 'size()'"); print(X.size())
    except Exception: traceback.print_exc()
    print()

    try: print("Intentando acceder a 'data'"); print(X.data)
    except Exception: traceback.print_exc()
    print()

    try: print("Intentando re-asignar 'data'"); X.data = [1,2,1]
    except Exception: traceback.print_exc()
    print()

    try: print("Intentando reasignar 'size'"); X.size = lambda S:0
    except Exception: traceback.print_exc()
    print()

    try: print("Intentando acceder a 'data'"); print(Y.data)
    except Exception: traceback.print_exc()
    print()

    try: print("Intentando acceder a 'size()'");print(Y.size())
    except Exception: traceback.print_exc()
