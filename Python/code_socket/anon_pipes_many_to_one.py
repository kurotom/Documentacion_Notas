"""
Múltiples escrituras a una lectura.

"""


from threading import Thread

import os
import sys

import time

import random


class To_Read(Thread):
    def __init__(self, pipein):
        self.pipein = pipein
        super().__init__()

    def run(self):
        try:
            while True:
                line = os.read(self.pipein, 32).decode()
                msg = '%s | Pipe: %s  | %s ' % (
                            time.ctime(),
                            self.pipein,
                            line
                        )
                print()
                print(msg)
        except (OSError, KeyboardInterrupt):
            os.close(self.pipein)


class To_Write(Thread):
    def __init__(self, pipeout, cls):
        self.pipeout = pipeout
        self.cls = cls
        super().__init__()

    def run(self):
        try:
            while True:
                msg = random.randint(0, 10)
                os.write(self.pipeout, f'{self.cls} - {msg}\n'.encode())
                sys.stdout.flush()
                time.sleep(1)
        except (OSError, KeyboardInterrupt):
            os.close(self.pipeout)


class A:
    """
    Clase solamente lee los mensajes recibidos.
    """
    def __init__(self, pipe_in):
        print(os.getpid())
        self.read = To_Read(pipe_in)

    def start(self):
        self.read.start()

    def __str__(self):
        return 'A'


class B:
    """
    Clase solamente escribe mensajes.
    """
    def __init__(self, pipe_out):
        print(os.getpid())
        self.write = To_Write(pipe_out, self)

    def start(self):
        self.write.start()

    def __str__(self):
        return 'B'


class C(B):
    """
    Hereda de B.
    """
    def __str__(self):
        return 'C'


parentIn, childOut = os.pipe()
childIn, parentOut = os.pipe()
childIn2, parentOut2 = os.pipe()

print(parentIn, childOut)
print(childIn, parentOut)
print(childIn2, parentOut2)

a = A(pipe_in=parentIn)
b = B(pipe_out=childOut)
c = C(pipe_out=childOut)

print('\nStart: %s \n\n' % time.ctime())

a.start()
b.start()
c.start()
