"""
socket permiten comunicacion cruzada

Iniciar los threads para comunicarse sobre sockets, programas independientes también, porque son de todo el sistema como los fifos.
Clientes y procesos pueden estar en threads para hablar con el servidor mediante sockets.

Sockets usan string `bytes`, objetos `pickle` o texto encoded Unicode.

Advertencia: es posible que sea necesario sincronizar las impresiones en subprocesos si su salida se superpone.
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from threading import Thread


port = 50008
host = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'Server got: [%s]' % data
        conn.send(reply.encode())



def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print('client got: [%s]' % reply)



if __name__ == '__main__':
    sthread = Thread(target=server)
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        Thread(target=client, args=('client%s' % i, )).start()
