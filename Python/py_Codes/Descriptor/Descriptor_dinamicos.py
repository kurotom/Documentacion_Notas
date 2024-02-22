"""
'Descriptores dinámicos' permite ejecutar instrucciones y retornar atributos en
lugar de solamente retornar atributos.
"""

import os


class DirectorySize(object):
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()          # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname      # Regular instance attribute



a = Directory(".")
print(a.size)

p = Directory("../")
print(p.size)
