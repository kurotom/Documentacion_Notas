# -*- coding: utf-8 -*-
"""
Uso de Metaclase `MetaTrace` para aplicar decorador automáticamente a métodos.

El resultado es la combinación de `decorators` y `metaclass`.
"""


from tracer_metaclass_automatically import MetaTrace

class Person(metaclass=MetaTrace):
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
