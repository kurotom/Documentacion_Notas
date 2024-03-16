"""
`os.fork` no funcionan en sistemas Windows.

Se crea un pipe (in, out), parent recibe pipein y child recibe pipeout.

Se crea un hilo por cada hijo creado y lo inicia con `.start()`.

parent espera los datos del hijo y lee los primeros 32 bytes de texto.
"""

import os, time, threading


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))



pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
