# Duck Typing

Concepto relacionado con la programación que aplica a ciertos lenguajes orientados a objetos.

> If it walks like a duck and it quacks like a duck, then it must be a duck.


Los patos son objetos, y hablar/andar son métodos.

Duck typing se funda en el razonamiento inductivo (la verdad de las premisas apoyan la conclusión, pero no la garantizan).

A Python no le importa el tipo de objetos, lo único que importa son los métodos.

```
# Esta función utiliza el método hablar del objeto que se le pase
# sin importar su tipo.
def llama_hablar(x):
    x.hablar()



class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")

class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")
        

llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!


# Otra forma de verlo, es usando una lista de clases, iterando
# para usar su metodo.

lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!
```


* Python es un lenguaje que soporta el duck typing, lo que hace que el tipo de los objetos no sea tan relevante, siendo más importante lo que pueden hacer (sus métodos).
* Otros lenguajes como Java no soporta el duck typing, pero se puede conseguir un comportamiento similar cuando los objetos comparten un interfaz (si existe herencia entre ellos). Este concepto relacionado es el polimorfismo.
* El duck typing está en todos lados, desde la función len() hasta el uso del operador *.





