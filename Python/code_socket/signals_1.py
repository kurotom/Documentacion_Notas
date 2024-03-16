"""
Módulo `signal` provee mecanismos para usar manejadores de señales en Python.

Las señales se refieren a mecanismos que permiten a un proceso recibir notificaciones asincrónicas sobre eventos o cambios en su entorno.
"""

import sys, signal, time


def now():
    # current time string
    return time.ctime(time.time())


def onSignal(signum, stackframe):
    # python signal handler
    # most handlers stay in effect
    print('Got signal ', signum, ' at ', now())
    # signal.signal(signal.SIGCHLD, onSignal)



signum = int(sys.argv[1])

# install signal handler
signal.signal(signum, onSignal)


# wait for signals or pass
while True:
    signal.pause()
