"""
Herramientas para conectar streams estándars de programas no-GUI a
sockets de programas GUI, usados para comunicación entre estos dos
tipos de programas.
"""


import sys
import socket
import time


port = 50008
host = 'localhost'


def initListenerSocket(port=port):
    """
    inicializa socket conectado a servidor modo listener.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn


def redirectOut(port=port, host=host):
    """
    conecta stream stdout del caller a un socket para GUI para
    empezara escuchar, o falla antes de aceptar.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('w')
    sys.stdout = file
    return sock


def redirectIn(port=port, host=host):
    """
    conecta stdin stream a un socket dado por GUI.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    sys.stdin = file
    return sock


def redirectBothAsClient(port=port, host=host):
    """
    conecta stream stdin y stdout del caller al mismo socket en
    ese modo.
    cliente al servior, envía msg y recibe reply.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    outputFile = sock.makefile('w')
    inFile = sock.makefile('r')
    sys.stdout = outputFile
    sys.stdin = inFile
    return sock


def redirectBothAsServer(port=port, host=host):
    """
    conecta stream stdin y stdout del caller a un mismo socket en 
    ese modo.
    servidor a cliente: recibe msg y envía reply.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    outputFile = conn.makefile('w')
    inFile = conn.makefile('r')
    sys.stdout = outputFile
    sys.stdin = inFile
    return conn



