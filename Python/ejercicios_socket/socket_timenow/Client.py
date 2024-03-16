"""
Clase Cliente envía al servidor una petición de tiempo actual.
"""

import socket
import time


class Client:

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50008
    ) -> None:
        self.host = host
        self.port = port
        self.sock = None

    def get_time(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = sock
        sock.connect((self.host, self.port))
        sock.send('get_time'.encode())
        reply = sock.recv(1024)
        print(reply.decode())

    def close(self) -> None:
        if self.sock is not None:
            self.sock.close()
