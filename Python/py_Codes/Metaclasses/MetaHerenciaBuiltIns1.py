# -*- coding: utf-8 -*-
"""
"""


class C:
    attr = 1
    def __str__(self):
        return ('class')


if __name__ == '__main__':

    I = C()
    print(I.__str__(), str(I))
    
    I.__str__ = lambda: 'instance'
    print(I.__str__(), str(I))

    print(I.attr)
    I.attr = 2
    print(I.attr)
