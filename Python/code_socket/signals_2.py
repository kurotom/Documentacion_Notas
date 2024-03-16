"""
Crear una alarma programada para desencadenar y capturar timeouts en el futuro.
"""

import sys, signal, time

def now():
    return time.asctime()


def onSignal(signum, stackframe):
    # python signal handler
    print('Got alarm ', signum, ' at ', now())
    # most handlers stay in effect


while True:
    print('Setting at ', now())

    # install signal handler
    signal.signal(signal.SIGALRM, onSignal)
   
    # do signal in 5 seconds
    signal.alarm(5)

    # wait for signals 
    signal.pause()
   
