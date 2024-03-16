"""
"""


import time
import socket


sock = socket.socket()
sock.connect(('localhost', 50008))

file = sock.makefile('w', buffering=1)


print('sending data1')
file.write('spam\n')
time.sleep(5)
file.flush()


print('sending data2')
print('eggs', file=file)
time.sleep(5)
file.flush()


print('sending data3')
sock.send(b'ham\n')
time.sleep(5)
