# -*- coding: utf-8 -*-
"""
Uso de Class Decorator, retorna la clase original aumentada.
"""


from tracer_any_decorator_to_all_method_Class_Decorator import decorateAll
from tracer_decorator import tracer, timer


#@decorateAll(tracer)
#@decorateAll(timer())
@decorateAll(timer(label='@@'))       # usa decorador
class Person:                         # aplica decorador a métodos
    def __init__(self, name, pay):    # Person = decorateAll(..)(Person)
        self.name = name              # Person = DecoDecorate(Person)
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
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)
