"""
named pipe
"""

import os
import sys

import time


fifo_file = '/tmp/my_fifopy'


class Server:
    """
    Se puede leer named pipes de dos formas.
        * os.open(), os.read()
        * open() , readline() - fichero regular, terminar con '\n'
    """
    def __init__(self):
        self.pipein = os.open(fifo_file, flags=os.O_RDONLY)
        # self.pipein = open(fifo_file, 'r')

    def main(self):
        while True:
            line = os.read(self.pipein, 32)
            print('%s' % line.decode())
            # line = self.pipein.readline()[:-1]
            # print('%s' % line)


class Client:
    """
    Para escribir en un FIFO
        * abrir el fifo, `os.open()`
        * escribir `os.write()`
    """
    def __init__(self):
        self.pipeout = os.open(fifo_file, flags=os.O_WRONLY)

    def main(self):
        try:
            while True:
                msg = '%s \n' % (self)
                os.write(self.pipeout, msg.encode())
                time.sleep(1)
        except BrokenPipeError:
            pass

    def __str__(self):
        return 'Client %s' % hash(self)


if __name__ == '__main__':
    if not os.path.exists(os.path.abspath(fifo_file)):
        os.mkfifo(fifo_file)

    arg = int(sys.argv[1])
    if arg == 1:
        s = Server()
        s.main()
    else:
        c = Client()
        c.main()
