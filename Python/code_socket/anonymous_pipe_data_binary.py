"""
parent() crea pipe (pipein, pipeout), copia el proceso o espera por la data del hijo creado.

child(pipeout) recibe un pipe end (pipeout) del padre, escribe el mensaje y usa ese pipe para enviarlo al padre.

Los mensajes son data binaria.
"""

import os, time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                                         # make parent wait
        msg = ('Spam %03d' % zzz).encode()     # pipe binary bytes - utf-8
        os.write(pipeout, msg)                           # send to parent
        zzz = (zzz + 1) % 5                                    # goto 0 to 4


def parent():
    pipein, pipeout = os.pipe()                          # make 2-ended pipe
    if os.fork() == 0:                                            # copy this process
        child(pipeout)                                           # in copy, run child
    else:                                                               # in parent, listen to pipe
        while True:
            line = os.read(pipein, 32)                      # blocks until data sent, >= 32 bytes
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))



parent()
