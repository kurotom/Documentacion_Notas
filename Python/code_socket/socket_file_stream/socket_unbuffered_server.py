"""
"""

import socket


sock = socket.socket()
sock.bind(('', 50008))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen(5)


print('accepting...')

conn, id = sock.accept()

for i in range(3):
    print('receiving...')
    msg = conn.recv(1024)
    print(msg)
