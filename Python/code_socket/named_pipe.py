"""
named pipes son creado usando `os.mkfifo`, no disponible en Windows,
no es necesario `.fork()` porque los ficheros *fifos* son externos
a procesos y compartimiento de ficheros descriptores en procesos
parent/child.
"""


import os, time, sys


fifoname = '/tmp/PYpipefifo'


def child():
    pipeout = os.open(fifoname, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('%s -- Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5



def parent():
    pipein = open(fifoname, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))




if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)

    if len(sys.argv) == 1:
        print('PARENT')
        parent()
    else:
        print('CHILD')
        child()

