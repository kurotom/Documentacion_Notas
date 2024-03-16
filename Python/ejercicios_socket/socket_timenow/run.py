"""
Ejecuta Servidor o Cliente según argumento dado al ser ejecutado.
"""


from Server import Server
from Client import Client


import sys


opt = int(sys.argv[1])
if opt == 1:
    s = Server()
    s.start()
else:
    c = Client()
    c.get_time()
