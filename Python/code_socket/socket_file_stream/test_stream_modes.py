"""
Efecto de conectar stream estándar a ficheros en modo texto y binario
usando `socket.makefile`.
`print()` requiere modo texto, pero este modo impide modo unbuffered usando `-u` o `sys.stdout.flush()`.

Para probar las dos últimas líneas se debe comentar/descomentar una y
ejecutar el código.
"""


import sys


def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp


# Works: `input()` retorna texto
reader( open('test_stream_modes.py'))

# Works: `input()` retorna bytes
reader( open('test_stream_modes.py', 'rb'))



def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp


# Works: `print()` pasa texto a `.write()`
writer( open('temp', 'w'))
print(open('temp').read())


# Fallará en `print()`: requiere bytes modo binario
writer( open('temp', 'wb'))

# Fallará en `open()`: texto debe ser unbuffered
writer( open('temp', 'w', 0))

