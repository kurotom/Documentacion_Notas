"""
"""

from typing import TypeVar
from time import sleep

from ClientChat import Client

SocketClient = TypeVar("SocketClient")
TextTk = TypeVar("TextTk")
ControllerInstance = TypeVar("ControllerInstance")


class Controller:
    def __init__(
        self
    ):
        self.client = None
        self.client_socket = None
        self.messages_list = []
        self.username = None
        self.chatroom = None

    def get_hash_client(self) -> str:
        return self.client.hash_user

    def set_user_data(
        self,
        username: str,
        chatroom: str,
    ):
        self.username = username
        self.chatroom = chatroom

    def create_connection(
        self,
        host: str,
        port: int
    ):
        client = Client(
                        username=self.username,
                        room_id=self.chatroom,
                        host=host,
                        port=port,
                    )
        self.client_socket = client.prepare()
        self.client = client
        # print(client)
        return self

    def to_connect(self) -> None:
        # print(self.client_socket)
        self.client.connect()

    def recv_messages(
        self,
        text_element: TextTk
    ) -> None:
        # print('Controller - recv', self.client)
        self.client.recieve_messages(
            text_tk=text_element
        )

    def send_message(
        self,
        message: str
    ) -> None:
        self.client.send(message=message)

    def socket_stop(self) -> None:
        self.client.stop_socket()

    def __str__(self) -> str:
        return "[%s, %s]" % (self.username, self.chatroom)
