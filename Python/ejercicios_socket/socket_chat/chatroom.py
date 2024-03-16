"""
"""

from models import UserServer


class ChatRoom:

    def __init__(
        self,
        id: str
    ) -> None:
        self.id = None
        self.clients = []

    def amount_clients(self) -> int:
        return len(self.clients)

    def find_client(
        self,
        client: UserServer
    ) -> UserServer:
        for item in client:
            if item.uid == client.uid:
                return item

    def exists(
        self,
        client: UserServer
    ) -> int:
        return len([i for i in self.clients if i.uid == client.uid])

    def add_client(
        self,
        client: UserServer
    ) -> bool:
        if self.exists(client=client) == 0:
            self.clients.append(client)
            return True
        else:
            return False

    def remove_client(
        self,
        userServer: UserServer
    ) -> None:
        try:
            for i in range(len(self.clients)):
                if self.clients[i].uid == userServer.uid:
                    self.clients.pop(i)
        except IndexError:
            print('AMOUNT --> ', self.amount_clients())
            pass
