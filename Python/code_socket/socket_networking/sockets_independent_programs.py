"""
Se reusará funciones `client` y `server`, para ejecutarlos en programas independientes.

La comunicación entre Sockets y Thread, se debe a la memoria compartida de los Threads, pudiendo emplear named pipes, objetos, queues.

Sockets son como Fifos, son accesibles por todo el sistema, no requieren de memoria compartida.

Socket son portables.
"""

from sockets_threads import client, server
import sys, os

from threading import Thread


mode = int(sys.argv[1])

if mode == 1:
    server()
elif mode == 2:
    client('Client: process = %s' % os.getpid())
else:
    for i in range(mode):
        Thread(target=client, args=('Client: thread = %s' % i, )).start()


