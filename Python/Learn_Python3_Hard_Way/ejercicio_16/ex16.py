from sys import argv

script, filename = argv

print("Vamos a eliminar {filename}")
print("Para cancelar, CTRL + c")

input("?")

print("Abriendo fichero...")

target = open(filename, 'w')

print("Truncando el fichero, adios")
target.truncate()

print("Ingrese datos")

line1 = input("linea 1: ")
line2 = input("linea 2: ")
line3 = input("linea 3: ")

print("Ahora voy a escribir esas líneas")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finalmente, cierro el fichero")
target.close()

