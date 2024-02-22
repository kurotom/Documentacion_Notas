# -*- coding: utf-8 -*-
"""
Clase que usa decorator tracer en métodos
"""


from tracer_decorator import tracer


class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    
    @tracer
    def lastName(self):
        return self.name.split()[-1]



bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())
