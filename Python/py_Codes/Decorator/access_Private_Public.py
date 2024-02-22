# -*- coding: utf-8 -*-
"""
Atributos Privados y Publicos son mutuamente excluyentes, los atributos no
declarados por uno son automáticamente del otro tipo.

* Atributos Publicos pueden ser accedidos y cambiados desde fuera como dentro de
la clase por sus métodos.

* Atributos Privados no pueden ser accedidos y cambiados desde fuera, solamente
dentro de los métodos de la clase.


Usando Python 2.X funcionará correctamente la delegación, los operaciones
'built-in' porque se usa el estilo clásico capturando las clases embebidas.

Usando Python 3.X, la delegación no funcionará porque no se capturan los objetos
embebidos, no pueden capturar las clases proxys ni pasarlos, los
métodos 'bult-in' como '__add__', '__str__' se saltan '__getattr__'.
Implícitamente las clases heredan de superclase 'object'.

Al usar atributos pseudo-privados, se debe acceder mediante la ruta completa
del atributo, por ejemplo: '_onInstance__wrapped'.
"""

import traceback

traceMe = False

def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')

def print_args(name, *args):
    print(name + ' :  ' + ' '.join(map(str, args)))


def accessControl(failIf):
    print("__ : ", failIf)
    def onDecorator(aClass):
        print("___ : ", aClass.__name__)
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    print("\tValidated and delegated to " + aClass.__name__)
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                print(self.__dict__)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator



def Private(*attributes):
    print_args("atributes", *attributes)
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    print_args("atributes", *attributes)
    return accessControl(failIf=(lambda attr: attr not in attributes))



if __name__ == "__main__":
    traceMe = True
    print("Usando 'Private' en 'age'")
    @Private('age')
    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    X = Person('Bob', 40)
    print(X.__dict__)
    print(X.name)

    X.name = 'Sue'
    print(X.name)

    print(X)        # __getattr__ => runs Person.__str__

    try: X.age
    except Exception as e: traceback.print_exc() ; print()

    try: X.age = 'Tom';
    except Exception as e: traceback.print_exc() ; print()

    try:
        X + 10          # __getattr__ => runs Person.__add__
    except Exception as e:
        traceback.print_exc(); print()

    print(X)        # __getattr__ => runs Person.__str__

    print("\nRompiendo la privacidad de 'age'")
    X.__add__(10)
    print(X._onInstance__wrapped.age)




    print("\n#######################\n")
    print("Usando 'Public' en 'name'")

    @Public('name')
    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    X = Person('bob', 40)
    print(X.__dict__)

    print(X.name)
    X.name = 'Sue'
    print(X.name)

    try: print(X)        # __getattr__ => runs Person.__str__
    except Exception as e: traceback.print_exc() ; print()

    try: X.age
    except Exception as e: traceback.print_exc() ; print()

    try: X.age = 'Tom'
    except Exception as e: traceback.print_exc() ; print()

    try:
        X + 10          # __getattr__ => runs Person.__add__
    except Exception as e:
        traceback.print_exc(); print()
