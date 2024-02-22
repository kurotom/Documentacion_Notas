"""
Descriptor computado permite usar, asignar, modificar, eliminar atributos y
entrega una capa de código en la que se pueden registrar, validar la operación
de los atributos.
"""

class DescSquare(object):
    def __init__(self, start):# Each desc has own state
        self.value = start
    def __get__(self, instance, owner):
        return self.value ** 2
    def __set__(self, instance, value):
        self.value = value


class Client1:
    X = DescSquare(3)   # Assign descriptor instance to class attr


class Client2:
    X = DescSquare(32)  # Another instance in another client class

# Could also code two instances in same class

c1 = Client1()
c2 = Client2()
print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)
