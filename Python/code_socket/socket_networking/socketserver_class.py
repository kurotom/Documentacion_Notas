"""
`socketserver` permite crear clases para levantar un servidor, incorpora hilos para manejar clientes múltiples y no bloquar al servidor.


Heredar de `socketserver.BaseRequestHandler` (TCP server) debe implementar el método `handle()`.

Esta implementación es asíncrono.
"""


import time
import socketserver
import socket


myHost = ''
myPort = 50008


def now():
    """
    Tiempo actual del servidor.
    """
    return time.ctime(time.time())


class MyClientHandler(socketserver.BaseRequestHandler):
    """
    Hereda de `BaseRequestHandler`, se debe implementar `handle()`.
    `setup()` y otros métodos es opcional.
    """

    def setup(self):
        self.request.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def handle(self):
        """
        Implementar `handle()`, maneja todas las nuevas peticiones.
        """
        print('--->>>>')
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            reply = 'Echo => %s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()




myaddr = (myHost, myPort)
# Implementa `ThreadingTCPServer` para crear hilo por cada nueva conexión.
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)

print(server.socket)

# Configuración de parámetros de servidor.
server.socket.listen(5)

# Maneja peticiones hasta que terminan.
server.serve_forever()
