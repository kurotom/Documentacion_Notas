"""
Descriptores permiten tener más control en cuanto al acceso, uso, modificación,
eliminación de los atributos de una clase.

Usando módulos como 'logging' se pueden crear ficheros '.log' y registrar las
operaciones realizadas. Además de crear validaciones para comprobar si cumple
los requisitos antes de asignar el valor al atributo.

Esto es especialmente útil en sistemas ORM.
"""

import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess(object):
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()         # Descriptor instance
    def __init__(self, name, age):
        self.name = name            # Regular instance attribute
        self.age = age              # Calls __set__()

    def birthday(self):
        self.age += 1               # Calls both __get__() and __set__()


mary = Person('Mary M', 30)
dave = Person('David D', 40)
print(vars(dave))
print(vars(mary))
print(mary.age)
print(mary.birthday())
print(dave.name)
print(dave.age)
