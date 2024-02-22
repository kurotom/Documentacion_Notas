# -*- coding: utf-8 -*-
"""
Las Metaclases ,por lo general, son sentencias `class`, pero se pueden usar cualquier objeto *callable* (que tengan `__call__`) como metaclase.

Las funciones pueden hacer de metaclases, *funciones metaclases*.
"""


def MetaFunc(classname, supers, classdict):
    print('\tMetaFunc')
    print('...classname: ', classname)
    print('...supers: ', supers)
    print('...classdict: ', classdict)
    return type(classname, supers, classdict)


class Eggs:
    pass


if __name__ == '__main__':
    class Spam(Eggs, metaclass=MetaFunc):
        data = 1
        def method(self, args):
            return self.data + args


    print('_' * 30)
    x = Spam()
    print('data: ', x.data, x.method(2))
