# -*- coding: utf-8 -*-
"""
"""
import traceback

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')


class BuiltinsMixins:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):
        return self.reroute('__add__', other)
    def __str__(self):
        return self.reroute('__str__')
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)


def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixins):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)

                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)

                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))



if __name__ == "__main__":
    traceMe = True
    @Private('age')
    class Person():
        def __init__(self):
            self.age = 42
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    x = Person()
    print(x.__dict__)

    try:
        x.age
    except Exception as e:
        traceback.print_exc()
        print("")

    print(x)        # __getattr__ => runs Person.__str__
    print("")

    try:
        x + 10          # __getattr__ => runs Person.__add__
    except Exception as e:
        traceback.print_exc()
        print("")

    print(x)        # __getattr__ => runs Person.__str__


    print("\nRompiendo la privacidad")
    x.__add__(10)
    print(x._onInstance__wrapped.age)
