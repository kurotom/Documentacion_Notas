# -*- coding: utf-8 -*-
"""
Combinación de Class Decorator
"""


from tracer_any_decorator_to_all_method_Class_Decorator import decorateAll
from tracer_decorator import tracer, timer



def multiple_decorators():
    @decorateAll(tracer(timer(label='@@')))   # combinación de decoradores
    class Person:                         # aplica decorador a métodos
        def __init__(self, name, pay):    # Person = decorateAll(..)(Person)
            self.name = name              # Person = DecoDecorate(Person)
            self.pay = pay
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
        def lastName(self):
            return self.name.split()[-1]
    return Person


def trace_time_method():
    @decorateAll(tracer)                 # traza onCall wrapper, method times
    @decorateAll(timer(label='>>'))
    class Person:                         # aplica decorador a métodos
        def __init__(self, name, pay):    # Person = decorateAll(..)(Person)
            self.name = name              # Person = DecoDecorate(Person)
            self.pay = pay
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
        def lastName(self):
            return self.name.split()[-1]
    return Person


def time_trace_methods():
    @decorateAll(timer(label='=='))       # timepo wrapper onCall, traces methods
    @decorateAll(tracer)
    class Person:                         # aplica decorador a métodos
        def __init__(self, name, pay):    # Person = decorateAll(..)(Person)
            self.name = name              # Person = DecoDecorate(Person)
            self.pay = pay
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
        def lastName(self):
            return self.name.split()[-1]
    print('%.5f' % Person.__init__.alltime)
    return Person


Person = multiple_decorators()
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())

print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)


print('-'*40)

Person = trace_time_method()
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())


print('-'*40)

Person = time_trace_methods()
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)

sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())

print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)



