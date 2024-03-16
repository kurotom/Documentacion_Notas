"""
FileControler maneja el tema relacionado con la administración de ficheros.
"""


import os
import pickle
from models import UserData, File
from typing import TypeVar, Union


TypeGeneric = TypeVar('TypeGeneric')
TypeFifo = TypeVar('FIFO')
FifoReadOnly = TypeVar('FifoReadOnly')
FifoWriteOnly = TypeVar('FifoWriteOnly')


class FifoControl:

    def create_fifo(
        self,
        fifo_path: str
    ) -> None:
        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)

    def to_data(
        self,
        bytes_data: bytes
    ) -> object:
        try:
            return pickle.loads(bytes_data)
        except Exception:
            return bytes_data

    def to_pickle(
        self,
        data: Union[dict, str, list, int, object]
    ) -> bytes:
        return pickle.dumps(data)

    def gettingData(
        self,
        pipe: FifoReadOnly,
        client_hash: str,
        size_read: int = 1042
    ) -> list:
        """
        """
        list_files = []
        current_file = None

        while True:
            user_data_recv = os.read(pipe, size_read)
            # print(user_data_recv)
            if len(user_data_recv) > 0:
                data_recv = self.to_data(user_data_recv)
                # print()
                if type(data_recv) is dict:
                    filename = data_recv['filename']
                    size = data_recv['size']
                    md5_hash = data_recv['md5']

                    file = File()
                    file.client_hash = client_hash
                    file.filename = filename
                    file.size = size
                    file.md5 = md5_hash
                    current_file = file

                elif type(data_recv) is bytes:
                    current_file.chunks.append(data_recv)

                elif data_recv is None:
                    if current_file is not None:
                        list_files.append(current_file)
                        current_file = None
            else:
                break
        return list_files

    def send_to_pipe(
        self,
        pipeObj: FifoWriteOnly,
        data: Union[bytes, dict, str, list, int, object]
    ) -> None:
        databytes = self.to_pickle(data=data)
        os.write(pipeObj, databytes)

    def close_fifo(
        self,
        fifo: TypeFifo
    ) -> None:
        """
        """
        if fifo is not None:
            os.close(fifo)

    def delete_fifos(
        self,
        fifo_path: str
    ) -> None:
        """
        """
        if os.path.exists(fifo_path):
            os.remove(fifo_path)
