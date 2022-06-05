from sys import argv

script, filename = argv

txt = open(filename)

print(f"Fichero: {filename}")
print(txt.read())
txt.close()


