"""
Clase Client encargada de enviar los datos del fichero dado
al servidor.

Modo de comunicación:
1. Se comunica con el servidor usando un FIFO público, enviando el uuid
del cliente.
2. Abre un FIFO privado entre cliente y servidor.
3. Envía y recibe los datos usando los FIFOs privados.
4. Cierra la comunicación.
"""


import os
from operations import Operations
from fifocontroller import FifoControl
from filemanagerfifo import FileManager

from models import UserData, File

import time


class Client:
    """
    Clase Client representa al usuario y envía el archivo al servidor.
    """
    def __init__(
        self,
        user_name: str,
    ) -> None:
        self.filemanager = FileManager()
        self.fifocontrol = FifoControl()
        self.public_fifo = None
        self.size_read = 1042

        self.user = UserData(username=user_name)
        self.hashClient = self.user.genhash()
        # self.hashClient = '8756855518477'

        self.fifo_read_private = f"/tmp/{self.hashClient}_ro_fifo"
        self.fifo_write_private = f"/tmp/{self.hashClient}_wo_fifo"
        self.fifocontrol.create_fifo(self.fifo_read_private)
        self.fifocontrol.create_fifo(self.fifo_write_private)

    @property
    def list_files(self) -> dict:
        """
        """
        print('Listing Files')
        self.request_operation(Operations.list)

        pipe_read = os.open(self.fifo_read_private, os.O_RDONLY)
        data = os.read(pipe_read, self.size_read)

        unpickled_data = self.fifocontrol.to_data(data)

        if unpickled_data != []:
            for item in unpickled_data:
                print(item)
        else:
            print(unpickled_data)

        return unpickled_data

    def search(
        self,
        namefile: str,
        save_file: bool = False
    ) -> None:
        """
        Busca fichero en Server.
        """
        self.request_operation(Operations.search)

        pipe_out = os.open(self.fifo_write_private, os.O_WRONLY)

        self.fifocontrol.send_to_pipe(
            pipeObj=pipe_out,
            data=namefile
        )

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_out)

        pipe_in = os.open(self.fifo_read_private, os.O_RDONLY)

        file_matches = self.fifocontrol.gettingData(
            pipe=pipe_in,
            client_hash=self.hashClient
        )

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_in)

        if file_matches != []:
            for file_item in file_matches:
                if save_file:
                    isWritten = self.filemanager.save_file(
                            file=file_item,
                            path='.'
                        )
                    if isWritten:
                        print('The file was written successfully.')
                        print("%s" % file_item.filepath)
        else:
            print('File not found.')

    def delete_file(
        self,
        namefile: str
    ) -> None:
        """
        """
        self.request_operation(Operations.delete)

        pipe_out = os.open(self.fifo_write_private, os.O_WRONLY)

        self.fifocontrol.send_to_pipe(
            pipeObj=pipe_out,
            data=namefile
        )

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_out)

        pipe_in = os.open(self.fifo_read_private, os.O_RDONLY)

        response_from_server = os.read(pipe_in, self.size_read)

        isDeleted = self.fifocontrol.to_data(bytes_data=response_from_server)

        if isDeleted:
            print('File "%s" has been deleted successfully.' % namefile)
        else:
            print(isDeleted)

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_in)

    def get_file(
        self,
        filename: str,
        path_to_save: str = '.',
        autosave: bool = True
    ) -> File:
        """
        Read, obtiene el fichero desde el Server.
        """
        print('Get File')
        self.request_operation(Operations.get_file)

        pipe_out = os.open(self.fifo_write_private, os.O_WRONLY)

        self.fifocontrol.send_to_pipe(
                pipeObj=pipe_out,
                data=filename
            )

        time.sleep(0.1)

        self.fifocontrol.close_fifo(pipe_out)

        pipe_in = os.open(self.fifo_read_private, os.O_RDONLY)

        listFileObjs = self.fifocontrol.gettingData(
            pipe=pipe_in,
            client_hash=self.hashClient
        )

        for file_item in listFileObjs:
            # print(file_item)
            is_written = self.filemanager.save_file(
                                    file=file_item,
                                    path=path_to_save
                                )
            if is_written:
                print('File "%s" has been written. Path "%s"' % (
                                file_item.filename,
                                file_item.filepath
                    ))

        self.fifocontrol.close_fifo(pipe_in)
        return listFileObjs

    def get_files(
        self,
        filenames: list,
        autosave: bool = True
    ) -> list:
        """
        """
        for item in filenames:
            self.get_file(filename=item, autosave=autosave)

    def send_file(self, path_file: str) -> None:
        """
        Create, envía los datos del fichero al FIFO privado.
        """
        print('Sending Data to Server')
        self.request_operation(Operations.write)

        if os.path.exists(path_file):
            pipe_transfer = os.open(self.fifo_write_private, os.O_WRONLY)
            if os.path.isfile(path_file):

                fileObj = self.filemanager.prepare_file(
                                file_path=path_file,
                                client_hash=self.hashClient
                            )

                # envía metadata primero
                self.fifocontrol.send_to_pipe(
                        pipeObj=pipe_transfer,
                        data=fileObj.get_metadata()
                    )

                time.sleep(0.1)

                # envía chunks del fichero
                for x in range(len(fileObj.chunks)):
                    # print('Transfering chunk %s' % x)
                    self.fifocontrol.send_to_pipe(
                            pipeObj=pipe_transfer,
                            data=fileObj.chunks[x]
                        )

                time.sleep(0.1)

                # finaliza el intercambio con un None
                self.fifocontrol.send_to_pipe(
                        pipeObj=pipe_transfer,
                        data=None
                    )

                time.sleep(0.1)

            elif os.path.isdir(path_file):
                list_fileObj = self.filemanager.prepare_directory(
                                            directory_path=path_file,
                                            client_hash=self.hashClient
                                        )

                for item in list_fileObj:
                    # envía metadata primero
                    # print(item)
                    self.fifocontrol.send_to_pipe(
                            pipeObj=pipe_transfer,
                            data=item.get_metadata(),
                        )

                    time.sleep(0.1)

                    # envía chunks del fichero
                    for i in range(len(item.chunks)):
                        # print('Transfering chunk %d' % i)
                        self.fifocontrol.send_to_pipe(
                                pipeObj=pipe_transfer,
                                data=item.chunks[i]
                            )

                    time.sleep(0.1)

                    # finaliza el intercambio con un None
                    self.fifocontrol.send_to_pipe(
                            pipeObj=pipe_transfer,
                            data=None
                        )

                    time.sleep(0.1)

            self.fifocontrol.close_fifo(pipe_transfer)

    def request_operation(self, operation: int):
        """
        Indica al servidor la operación que quiere realizar.
        """

        fifopublic = os.open(self.public_fifo, os.O_WRONLY)

        data_neg = {
            'user': self.user,
            'clientHash': self.hashClient,
            'operation': operation
        }

        self.fifocontrol.send_to_pipe(
            pipeObj=fifopublic,
            data=data_neg
        )

    def clear(self, pipe=None) -> None:
        """
        """
        if pipe is not None:
            os.close(pipe)
        if os.path.exists(self.fifo_read_private):
            os.remove(self.fifo_read_private)
        if os.path.exists(self.fifo_write_private):
            os.remove(self.fifo_write_private)
