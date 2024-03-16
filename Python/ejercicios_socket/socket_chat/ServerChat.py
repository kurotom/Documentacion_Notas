"""
"""

import socket
import time
from uuid import uuid4

from threading import Thread

from chatroom import ChatRoom
from models import UserServer

import pickle


class CurrentChatsRooms:
    chats = {}


class Handler(Thread):

    def __init__(
        self,
        connection: socket.socket,
        address: tuple,
        # chatRooms: dict,
    ) -> None:
        self.connection = connection
        self.address = address
        # self.chatrooms_dict = chatRooms
        super().__init__()

    def to_pickle(
        self,
        data: object
    ) -> bytes:
        return pickle.dumps(data)

    def run(self) -> None:

        while True:
            try:
                data = self.connection.recv(1024)
                if len(data) > 0:
                    client_data = pickle.loads(data)

                    clientUsername = client_data['username']
                    clientUID = client_data['uid']
                    chatroomID = client_data['roomuid']
                    messageClient = client_data['message']
                    print(messageClient)

                    currentUser = self.handler_connection(
                            username=clientUsername,
                            client_uid=clientUID,
                            chatroom_id=chatroomID,
                            message_client=messageClient,
                            connection=self.connection,
                            address=self.address,
                        )

                    if messageClient != 'INIT':

                        chat_current = CurrentChatsRooms.chats[chatroomID]

                        if messageClient is None:
                            if chat_current.amount_clients() > 0:
                                chat_current.remove_client(
                                            userServer=currentUser
                                        )
                        else:
                            self.send_to_clients(
                                    userServer=currentUser,
                                    chatroomid=chatroomID,
                                    msgClient=messageClient,
                                )
                else:
                    break
            except ConnectionResetError:
                break
            except EOFError:
                pass

    def handler_connection(
        self,
        username: str,
        client_uid: str,
        chatroom_id: str,
        message_client: str,
        connection: socket.socket,
        address: tuple
    ) -> UserServer:

        current_user = UserServer(
                    username=username,
                    uid=client_uid,
                    chatroom_id=chatroom_id,
                    connection=connection,
                    address=address,
                )

        # print('user ', current_user)

        if chatroom_id not in CurrentChatsRooms.chats:
            CurrentChatsRooms.chats[chatroom_id] = ChatRoom(id=chatroom_id)

        current_chatroom = CurrentChatsRooms.chats[chatroom_id]

        current_chatroom.add_client(client=current_user)

        return current_user

    def send_to_clients(
        self,
        userServer: UserServer,
        chatroomid: str,
        msgClient: str
    ) -> None:
        current_chat_room = CurrentChatsRooms.chats[chatroomid]
        print(current_chat_room.amount_clients())

        for client in current_chat_room.clients:
            # print('--> ', client.username)
            if client.uid != userServer.uid:
                print(msgClient, client.chat_prefix(), client.uid, userServer.uid)
                message = self.prepare_message(
                            prefix=userServer.chat_prefix(),
                            msg_client=msgClient
                        )
                client.connection.send(
                    self.to_pickle(data=message)
                )

    def prepare_message(
        self,
        prefix: str,
        msg_client: str
    ) -> str:
        message = ""
        user_prefix = prefix + ' : '
        msg_chat = msg_client.split("\n")
        for i in range(len(msg_chat)):
            if i == 0:
                first_row = user_prefix + msg_chat[i] + "\n"
                message += first_row
            else:
                message += '\t' + msg_chat[i] + "\n"
        return message.strip() + '\n'


class Server:

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 50008
    ) -> None:
        self.host = host
        self.port = port
        self.sock = None
        self.current_chatrooms = {}

    def prepare(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        self.sock = sock

    def listen(self):
        self.prepare()
        # print(self.sock, type(self.sock))
        self.sock.listen()
        while True:
            conn, address = self.sock.accept()
            print(conn)

            handler = Handler(
                    connection=conn,
                    address=address,
                    # chatRooms=self.current_chatrooms
                )

            handler.start()
