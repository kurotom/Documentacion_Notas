"""
Server side: abre un puerto, escucha un cliente, envía reply.

Fork un proceso para cada conexión cliente; procesos child comparten el mismo descriptor socket padre.

Fork es menos portable, no disponible en Windows en Python estándar, se debe usar Cygwin.

`os.waitpid(0, os.WNOHANG)` previene los procesos zombies hijos, retornado los procesos hijos muertos, ignora los procesos hijos ya muertos.

"""


import os, time, sys

import socket


myHost = ''
myPort = 50008


# make TCP object
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# reuse port
sockObj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind server to port number
sockObj.bind((myHost, myPort))
# allow 5 pending clients
sockObj.listen(5)


def now():
    """
    Tiempo actual del servidor
    """
    return time.ctime(time.time())



activeChildred = []
def killChildren():
    """
    Colecta y elimina proceso Child muertos, si el proceso está vivo
    llena la tabla de sistema.
    No toma en cuenta los procesos Child exit.
    Lista vacía es False, sino es True
    """
    while activeChildred:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        activeChildred.remove(pid)



def handleClient(connection):
    """
    Proceso hijo, responde y sale.
    Bloqueo arbitrario de 5 segundos, simulando petición costosa o demorosa.
    Lee y escribe a un cliente.
    """
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo => %s at %s' % (data, now())
        connection.send(reply.encode())
    sys.exit(0)



def dispatcher():
    """
    Escucha hasta que el proceso muera, espera la siguente conexión.
    Limpia los procesos children zombies.
    Copia el proceso padre, si el proceso hijo es nuevo lo maneja, si
    el proceso ya existe, lo agrega a la lista `activeChildred`.
    """
    while True:
        connection, address = sockObj.accept()
        print('Server connected by ', address, end=' ')
        print('at', now())
        killChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
        else:
            activeChildred.append(childPid)





dispatcher()
