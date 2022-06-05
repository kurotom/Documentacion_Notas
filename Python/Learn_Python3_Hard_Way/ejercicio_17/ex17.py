from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiar desde {from_file} a {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Tamaño del fichero: {len(indata)} bytes.")

print("Existe el fichero? {exists(to_file)}.")

print("Para salir, Ctrl + c, continuar presione Enter")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print(f"Escrito en {to_file}.")
print()

out_file.close()
in_file.close()

