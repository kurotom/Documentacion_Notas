"""
parent() crea pipe (pipein, pipeout), copia el proceso o espera por la data del hijo creado.

child(pipeout) recibe un pipe end (pipeout) del padre, escribe el mensaje y usa ese pipe para enviarlo al padre.

Los mensajes en `str` se debe envolver usando `os.fdopen`.
"""


import os, time

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                                                # make parent wait
        msg = ('Spam %03d\n' % zzz).encode()         # pipes are binary in 3.X
        os.write(pipeout, msg)                                   # send to parent
        zzz = (zzz + 1) % 5                                            # roll to 0 at 5


def parent():
    pipein, pipeout = os.pipe()                                  # make 2-ended pipe
    if os.fork() == 0:                                                    # in child, write to pipe
        os.close(pipein)                                                # close input side here
        child(pipeout)
    else:                                                                       # in parent, listen to pipe
        os.close(pipeout)                                              # close output side here
        pipein = os.fdopen(pipein)                              # make text mode input file object
        while True:
            line = pipein.readline()[:-1]                           # blocks until data sent
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()), type(line))


parent()
