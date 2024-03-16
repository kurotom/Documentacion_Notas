"""
no hay output por 10 segundos a menos que se use `python -u` o 
`sys.stdout.flush()`, pero salida de writer aparece cada 2
segundos cuando es usada esa opción.
"""


import os
import sys



def buffered_output():
    """
    la salida tarda 10 segundos en mostrarse en la terminal.
    """
    for line in os.popen('python pipe_unbuffered_writer.py'):
        print(line, end='')


def unbuffered_output():
    """
    la salida se muestra cada 2 segundos en la terminal
    (por el time.sleep de writer)
    se muestra a tan pronto se envía la data.
    """
    for line in os.popen('python -u pipe_unbuffered_writer.py'):
        print(line, end='')



if __name__ == '__main__':
    opt = int(sys.argv[1])
    if opt == 1:
        buffered_output()
    elif opt == 2:
        unbuffered_output()

