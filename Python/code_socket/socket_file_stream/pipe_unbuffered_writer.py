"""
linea output buffered (unbuffered) si stdout es una terminal,
buffered por defecto para otros dispositivos.

`-u` o `sys.stdout.flush()` para evitar demoras de salida en
pipe/socket.
"""


import time
import sys

for i in range(5):
    print(time.asctime())
    sys.stdout.write('spam\n')
    time.sleep(2)
