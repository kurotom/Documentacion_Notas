from sys import argv

script, user_name = argv
prompt = '>  '
print(f"Hola {user_name}, Nombre script {script}")
print()

print(f"¿Dónde vives {user_name}?")
lives = input(prompt)

print(f"¿Qué computador tienes?")
computer = input(prompt)

print(f"""
Vives en {lives}.
Tienes un {computer} de computador.
""")

