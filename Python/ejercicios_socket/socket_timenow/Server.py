"""
Clase Server, entrega tiempo actual al cliente conectado.
"""


import socket
import time
from threading import Thread


class Server(Thread):

    def __init__(
        self,
        port: int = 50008
    ) -> None:
        self.port = port
        super().__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.port))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            # print(type(conn))
            # print(type(addr))
            data = conn.recv(1024)
            if data.decode() == 'get_time':
                msg = '\nTime Now: %s\n' % time.ctime()
                conn.send(msg.encode())
