# -*- coding: utf-8 -*-
"""
Inheritance
"""

class Adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, item):
        return self.data(self.data, item)

    def add(self, y):
        print('Not Implemented')


class ListAdder(Adder):
    def add(self, y):
        return self.data + y


class DictAdder(Adder):
    def add(self, y):
        self.data.update(y)
        return self.data



listadder = ListAdder([1,2])
print(listadder.add([3,4]))


dictadder = DictAdder({1:2})
print(dictadder.add({5:6}))

