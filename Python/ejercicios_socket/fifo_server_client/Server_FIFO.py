"""
Clase Server encargado de recibir las presentaciones de clase Client.

Clase Handler, se encarga de manejar las operaciones del cliente,
se comunican por medio de FIFOs privados para lectura y escritura.
"""


import os
import time
import pickle
from hashlib import md5
import threading

from operations import Operations
from filemanagerfifo import FileManager
from fifocontroller import FifoControl

from models import UserData, File


class Handler(threading.Thread):
    """
    Clase Handler, maneja los clientes nuevos o existentes,
    coleccionando los chunks de data enviados.
    """
    def __init__(
        self,
        client_operation: dict
    ) -> None:
        """
        """
        self.fifocontrol = FifoControl()
        self.filemanager = FileManager()

        self.size_read = 1042

        self.current_user = client_operation['user']
        self.clientHash = str(client_operation['clientHash'])
        self.operation = client_operation['operation']

        self.pipein_path = f"/tmp/{self.clientHash}_wo_fifo"
        self.pipeout_path = f"/tmp/{self.clientHash}_ro_fifo"

        print(client_operation)

        super().__init__()

    def run(self) -> None:
        """
        """
        self.fifocontrol.create_fifo(self.pipein_path)
        self.fifocontrol.create_fifo(self.pipeout_path)

        print('>>>  Private PIPE')
        if self.operation == Operations.write:
            self.op_write()
        if self.operation == Operations.get_file:
            print('Getting files.')
            self.op_get_file()
        if self.operation == Operations.list:
            print('Listing files.')
            self.op_list_files()
        if self.operation == Operations.delete:
            self.op_delete_file()
        if self.operation == Operations.search:
            self.op_search_file()

    def op_delete_file(self) -> None:
        """
        """
        print('op_delete_file - Deleting File')

        pipe_in = os.open(self.pipein_path, os.O_RDONLY)

        data = os.read(pipe_in, self.size_read)
        file_to_delete = self.fifocontrol.to_data(bytes_data=data)
        file_data = self.filemanager.find_file(
            directory=self.clientHash,
            filename=file_to_delete
        )

        pipe_out = os.open(self.pipeout_path, os.O_WRONLY)

        is_deleted = self.filemanager.delete_file(file=file_data)

        self.fifocontrol.send_to_pipe(
            pipeObj=pipe_out,
            data=is_deleted
        )

        time.sleep(0.1)
        self.fifocontrol.close_fifo(pipe_out)

    def op_search_file(self) -> None:
        """
        """
        print('op_search_file - Searching File')
        pipe_in = os.open(self.pipein_path, os.O_RDONLY)

        data = os.read(pipe_in, self.size_read)
        file_to_search = self.fifocontrol.to_data(bytes_data=data)

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_in)

        file_match = self.filemanager.find_file(
                directory=self.clientHash,
                filename=file_to_search
            )

        pipe_out = os.open(self.pipeout_path, os.O_WRONLY)

        if file_match is None:
            self.fifocontrol.send_to_pipe(
                pipeObj=pipe_out,
                data=None
            )
            time.sleep(0.1)
        else:
            self.fifocontrol.send_to_pipe(
                pipeObj=pipe_out,
                data=file_match.get_metadata()
            )
            time.sleep(0.1)
            for x in range(len(file_match.chunks)):
                self.fifocontrol.send_to_pipe(
                    pipeObj=pipe_out,
                    data=file_match.chunks[x]
                )
            time.sleep(0.1)
            self.fifocontrol.send_to_pipe(
                pipeObj=pipe_out,
                data=None
            )
            time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_out)

    def op_write(self) -> None:
        """
        """
        print('op_write - Writting files')
        pipein = os.open(self.pipein_path, os.O_RDONLY)
        files_client = self.fifocontrol.gettingData(
                            pipe=pipein,
                            client_hash=self.clientHash,
                            # pipein_path=self.pipein_path
                        )
        for item in files_client:
            user_dir = self.filemanager.make_directory(
                                    directory=self.clientHash
                                )

            path_file = os.path.join(user_dir, item.filename)

            item.filepath = path_file

            fileWasWritten = self.filemanager.save_file(file=item)
            if fileWasWritten:
                print('Fichero se ha escrito con éxito.')
            else:
                print('Hubo un error, el fichero no fue escrito.')

        self.fifocontrol.close_fifo(pipein)

    def op_list_files(self) -> None:
        """
        """
        print('op_list_files - Listing files')
        directory = self.clientHash
        path_directory = os.path.abspath(os.path.join('.', directory))

        files_matches = self.filemanager.list_directory(path=path_directory)

        pipeout = os.open(self.pipeout_path, os.O_WRONLY)

        self.fifocontrol.send_to_pipe(
                    pipeObj=pipeout,
                    data=files_matches
                )

        time.sleep(0.1)

        self.fifocontrol.close_fifo(fifo=pipeout)

    def op_get_file(self) -> None:
        print('op_get_file - Getting files')
        pipein = os.open(self.pipein_path, os.O_RDONLY)
        data = os.read(pipein, self.size_read)

        req_filename = self.fifocontrol.to_data(bytes_data=data)

        self.fifocontrol.close_fifo(fifo=pipein)

        fileObj = self.filemanager.find_file(
            directory=self.clientHash,
            filename=req_filename
        )

        pipe_out = os.open(self.pipeout_path, os.O_WRONLY)

        # print(fileObj)
        if fileObj is not None:

            self.fifocontrol.send_to_pipe(
                    pipeObj=pipe_out,
                    data=fileObj.get_metadata()
                )

            time.sleep(0.1)

            for x in range(len(fileObj.chunks)):
                self.fifocontrol.send_to_pipe(
                        pipeObj=pipe_out,
                        data=fileObj.chunks[x]
                    )

            time.sleep(0.1)

            self.fifocontrol.send_to_pipe(
                    pipeObj=pipe_out,
                    data=None
                )

            time.sleep(0.1)
        self.fifocontrol.close_fifo(pipe_out)


class Server:
    """
    Clase Servidor, espera clientes nuevos y los deriva al manejador Handler.
    """
    def __init__(
        self,
        public_fifo
    ) -> None:
        """
        """
        self.pipein = os.open(public_fifo, os.O_RDONLY)
        self.size = 1024
        self.users = {}

    @property
    def listen(self) -> None:
        """
        """
        while True:
            data = os.read(self.pipein, self.size)
            if len(data) > 0:
                print('>>>  Public PIPE')
                data_client = pickle.loads(data)
                handler = Handler(
                                client_operation=data_client
                            )
                handler.start()
