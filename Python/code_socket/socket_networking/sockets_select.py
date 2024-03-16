"""
Implementación de servidor ECHO usando `select`.

Multiplexa las tareas de respuesta a los clientes usando un event-loop único para el servidor.

Útil para peticiones cortas.

No requieren de `thread` o `fork()`, pero se pueden usar para operaciones de peticiones de larga duración.
"""


import sys, time
from select import select
import socket


def now():
    """
    Tiempo actual del servidor.
    """
    return time.ctime(time.time())



myHost = ''
myPort = 50008

if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]


# Número de puertos para clientes
numPortSocks = 2


# Crea sockets principales para aceptar clientes nuevos
mainsocks, readsocks, writesocks = [], [], []

# Bucle para cear sockets
for i in range(numPortSocks):
    portsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portsock.bind((myHost, myPort))
    portsock.listen(5)

    mainsocks.append(portsock)
    readsocks.append(portsock)

    myPort += 1


# Event Loop - multiplexa hasta matar al server
print('###  select-server loop - Ready.  ###')

while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockObj in readables:
        if sockObj in mainsocks:
            print('> New client')
            newsock, address = sockObj.accept()
            print('>> Connect: ', address, id(newsock))
            readsocks.append(newsock)
        else:
            print('> Serving client.')
            data = sockObj.recv(1024)
            print('>> Got: ', data, ' on ', id(sockObj))
            if not data:
                print('>>> Client finished.')
                sockObj.close()
                readsocks.remove(sockObj)
            else:
                print('>>> Send reply to Client.')
                # escribir datos puede ser bloqueante.
                # se puede usar `select` para enviar el mensaje.
                reply = 'Echo => %s at %s' % (data, now())
                sockObj.send(reply.encode())


