"""
genera proceso/programa child, conecta stdin/stdout a procesos child de stdout/stdin, lee y escribe mapas para streams de salida y entrada del programa generado, muy parecido a unir secuencias con un módulo de `subprocess`.
"""

import os, sys

def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()
    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()
    pid = os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        os.execvp(prog, args)
        assert False, 'execvp failed!'


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'anonymous_pipe_bidirectional_test_child.py', 'spam')# fork child program
    print('Hello 1 from parent', mypid)
#    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)# to child's stdin
    print('Hello 2 from parent', mypid)
#    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])
