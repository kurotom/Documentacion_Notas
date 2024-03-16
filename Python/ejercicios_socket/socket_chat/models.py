"""
"""

import socket
from typing import TypeVar

UserServer = TypeVar("UserServer")


class UserServer:

    def __init__(
        self,
        username: str,
        uid: str,
        chatroom_id: str,
        connection: socket.socket,
        address: tuple
    ):
        self.username = username
        self.uid = uid
        self.chatroom_id = chatroom_id
        self.connection = connection
        self.address = address

    def compare(
        self,
        userServerInstance: UserServer
    ) -> bool:
        return self.uid == userServerInstance.uid

    def chat_prefix(self) -> str:
        return '%s-%s' % (self.username, self.uid[:8])

    def __str__(self) -> str:
        return '<[%s, %s, %s, %s]>' % (
                    self.uid,
                    self.chatroom_id,
                    self.connection,
                    self.address
                )
