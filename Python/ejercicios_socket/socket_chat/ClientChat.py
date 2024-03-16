"""
"""

import socket
import pickle
from threading import Thread
import os
import textwrap
from hashlib import md5
from time import sleep

from typing import TypeVar


TextTk = TypeVar("TextTk")
ControllerChat = TypeVar("ControllerChat")


class ReaderMessages(Thread):

    def __init__(
        self,
        socket_client: socket.socket,
        text_tk_element: TextTk
    ) -> None:
        self.socket_client = socket_client
        self.text_tk_element = text_tk_element
        super().__init__()

    def decode_data(
        self,
        bytes_data: bytes
    ) -> str:
        return pickle.loads(bytes_data)

    def run(self) -> None:
        while True:
            try:
                data = self.socket_client.recv(1024)
                if len(data) > 0:
                    current_message = self.decode_data(bytes_data=data)
                    # print('Run receive ', current_message)
                    self.text_tk_element.insert_message(message=current_message)
            except OSError:
                break


class Client:
    def __init__(
        self,
        username: str,
        room_id: int = 0,
        host: str = 'localhost',
        port: int = 50008
    ) -> None:
        self.room_id = room_id
        self.username = username
        self.hash_user = md5(username.encode()).hexdigest()
        self.host = host
        self.port = port
        self.sock = None

    def get_hash(self) -> str:
        return self.hash_user

    def prepare(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        return sock

    def connect(self) -> bool:
        # print(self.host, self.port)
        for i in range(1, 4):
            try:
                self.sock.connect((self.host, self.port))
                self.send(message='INIT')
                # self.is_connected.append(True)
                # print('-->')
                break
            except (ConnectionRefusedError, TimeoutError):
                print('Trying connect to server - %d' % i)
                sleep(1)
                pass
        if i > 3:
            msg = 'Server not connected, limit of connection attempts reached.'
            raise ConnectionError(msg)

    def send(
        self,
        message: str
    ) -> None:
        data = {
            'username': self.username,
            'roomuid': self.room_id,
            'uid': self.hash_user,
            'message': message  # + '---END'
        }
        data_pickled = pickle.dumps(data)
        try:
            self.sock.send(data_pickled)
        except OSError:
            pass

    def recieve_messages(
        self,
        text_tk: TextTk
    ) -> None:
        readermessages = ReaderMessages(
                socket_client=self.sock,
                text_tk_element=text_tk
            )
        readermessages.start()

    def stop_socket(self) -> None:
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        finally:
            self.sock.close()

    def __str__(self) -> str:
        return "<%s, %s>" % (self.host, self.port)
