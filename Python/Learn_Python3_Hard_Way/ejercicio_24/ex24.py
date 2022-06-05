print("")
print("")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
"""

print("----")
print(poem)
print("----")


five = 10 - 2 + 3 - 6
print(f"Debería dar cinco: {five}.\n")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("Empezando con .{} puntos.\n".format(start_point))
print(f"{beans} beans, {jars} jars, {crates} crates.\n")

start_point = start_point / 10

print("Otra forma de hacerlo:")

formula = secret_formula(start_point)
print("{} beans, {} jars, {} crates.\n".format(*formula))



