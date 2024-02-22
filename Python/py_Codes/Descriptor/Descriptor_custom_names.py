"""
Personalizar los nombres atributos que se asignen los Descriptores, que se
usarán dentro del mismo 'Descriptor', en atributos pseudo-privados
concatenando '_' al nombre de la variable.

Dependiendo de los atributos de la clase que hacen uso de un Descriptor, el uso
del atributo con el nombre personalizado.
"""

import logging

logging.basicConfig(level=logging.INFO)


class LoggedAccess(object):
        def __set_name__(self, owner, name):
                self.nombre_attr = name
                self.otro_attr = '_' + name
        def __get__(self, obj, objtype=None):
                value = getattr(obj, self.otro_attr)
                logging.info('Accessing %r giving %r', self.nombre_attr, value)
                return value
        def __set__(self, obj, value):
                logging.info('Updating %r to %r', self.nombre_attr, value)
                setattr(obj, self.otro_attr, value)


class Person:
        name = LoggedAccess()              # First descriptor instance
        age = LoggedAccess()               # Second descriptor instance
        def __init__(self, name, age):
                self.name = name           # Calls the first descriptor
                self.age = age             # Calls the second descriptor
        def birthday(self):
                self.age += 1



print(vars(vars(Person)['name']))
print(vars(vars(Person)['age']))


pete = Person('Peter P', 10)
kate = Person('Catherine C', 20)

print(vars(pete))
print(vars(kate))
