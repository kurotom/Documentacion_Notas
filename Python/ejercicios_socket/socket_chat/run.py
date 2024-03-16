"""

"""

import sys
from ServerChat import Server
from ClientChat import Client



arg = int(sys.argv[1])

if arg == 1:
    s = Server()
    s.listen()
else:
    c = Client(username='kurotom')
    c.connect()
    c.send_message(message='Hola')
