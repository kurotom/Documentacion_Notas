from sys import argv

script, input_file = argv

def print_Content(file):
    print(file.read())

def rebobinar(file):
    file.seek(0)

def print_a_line(line_count, file):
    print(line_count, file.readline())

current_file = open(input_file)

print("Imprimiendo el fichero completo.\n")

print_Content(current_file)

print("Rebobinar el fichero, así como una cinta.\n")

rebobinar(current_file)

print("Imprimir tres líneas.\n")

linea = 1
print_a_line(linea, current_file)

linea = linea + 1
print_a_line(linea, current_file)

linea += 1
print_a_line(linea, current_file)

current_file.close()
