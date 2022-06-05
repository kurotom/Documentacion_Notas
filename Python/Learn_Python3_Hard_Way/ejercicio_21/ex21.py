def add(a,b):
    print(f"Sumar {a} + {b}")
    return a + b
def restar(a,b):
    print(f"Restar {a} - {b}")
    return a - b
def multiplicar(a,b):
    print(f"Multiplicar {a} * {b}")
    return a * b
def dividir(a,b):
    print(f"Dividir {a} / {b}")
    return a / b

print("Algunas operaciones aritméticas")

age = add(30, 5)
heigth = restar(78, 10)
weigth = multiplicar(10, 8)
iq = dividir(100, 3)

print(f"Edad: {age}, Altura: {heigth}, Peso: {weigth}, IQ: {iq}.")

print("Un Puzzle")

que = add(age, restar(heigth, multiplicar(weigth, dividir(iq, 2))))

print("Esto es: ", que, "¿Puedes hacerlo a mano?.")


