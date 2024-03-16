"""
Tranferencia simple de archivos usando FIFOS.
Intentando crear una ambiente simulado del modelo Cliente/Servidor.
"""


import os
import sys

from Server_FIFO import Server
from Client_FIFO import Client

import time


if __name__ == '__main__':

    pipe_file = '/tmp/fifo_public_py'

    if not os.path.exists(os.path.abspath(pipe_file)):
        os.mkfifo(os.path.abspath(pipe_file))

    arg = int(sys.argv[1])
    if arg == 1:
        s = Server(public_fifo=pipe_file)
        s.listen
    else:
        file = os.path.abspath(sys.argv[2])
        c = Client(user_name='un usuario')
        c.public_fifo = pipe_file

        c.send_file(path_file=file)

        time.sleep(1)

        c.list_files

        time.sleep(1)

        c.get_file(filename='song_file.m4a', autosave=True)
        c.get_files(['file.txt', 'file (3ª copia).txt'], autosave=True)

        c.search(namefile='file.txt', save_file=True)

        c.delete_file(namefile='song_file.m4a')
