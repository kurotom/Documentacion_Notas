# -*- coding: utf-8 -*-
"""
Uso y aplicación de decorador para todos los métodos de la clase.
"""

from tracer_any_decorator_to_all_method_Metaclass import decorateAll
from tracer_decorator import tracer, timer


class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())


print('-'*40)
#
#
#      Aplicando `timer`
#
#


class Person(metaclass=decorateAll(timer())):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())


print('%.5f' %Person.__init__.alltime)
print('%.5f' %Person.giveRaise.alltime)
print('%.5f' %Person.lastName.alltime)

print('-'*40)
#
#
#      Aplicando argumento decorator
#
#


class Person(metaclass=decorateAll(timer(label='==>'))):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())



