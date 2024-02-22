# -*- coding: utf-8 -*-
"""
Comparación de generador de función, bucle for, lambda y map.
"""

from datetime import datetime

def timestamp():
    return datetime.now().timestamp()


def for_test(lista):
    a = timestamp()
    r = []
    for i in lista:
        r.append(abs(i))
    print(r)
    b = timestamp()
    t = datetime.fromtimestamp(b-a)
    print(f'\t>>> for_test:    {t.minute}:{t.second}:{t.microsecond}')

def mapa_test(lista):
    a = timestamp()
    print(list(map(abs, lista)))
    b = timestamp()
    t = datetime.fromtimestamp(b-a)
    print(f'\t>>> mapa_test:   {t.minute}:{t.second}:{t.microsecond}')

def gen_test(lista):
    a = timestamp()
    print(list(abs(x) for x in lista))
    b = timestamp()
    t = datetime.fromtimestamp(b-a)
    print(f'\t>>> gen_test:    {t.minute}:{t.second}:{t.microsecond}')

def lambda_test(lista):
    a = timestamp()
    print(list(map(lambda x : abs(x), lista)))
    b = timestamp()
    t = datetime.fromtimestamp(b-a)
    print(f'\t>>> lambda_test: {t.minute}:{t.second}:{t.microsecond}')

l = (-1, -2, 3, 4, -5, 0, 1, 80)
for_test(l)
mapa_test(l)
gen_test(l)
lambda_test(l)


