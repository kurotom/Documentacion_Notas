"""
"""

from sockets_server_clients import client
import sys


host = 'localhost'
port = '50008'


message = ['Hello network world.']


args = sys.argv[1:]

if len(args) > 0:
    for arg in args:
        client('%s - %s' % (arg, message))
else:
    client('%s' % message)



