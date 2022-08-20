# Programación Orientada de Objetos (POO)

Incluido en los años 1970s.

Se asemeja bastante a como pensamos en la vida real, utilizando las famosas **clases**, permitiendo agrupar un conjunto de variables y funciones.

Las clases tienen diferentes características, estas se llaman **atributos**.

Las clases tienen un conjunto de funcionalidades o cosas que pueden hacer, estas se llaman **métodos**.

Diferentes tipos de estas clases son **objetos**.

Cada objeto generado a partir de una clase se llama **instancia**.


## Atributos y Métodos

* Atributos de **instancia**: pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia.

* Atributos de **clase**: se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.

**Constructor** - `__init__`.
**Destructor** - `__del__`.


```
class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")



mi_perro = Perro("Toby", "Bulldog")
print(type(mi_perro))
# Creando perro Toby, Bulldog
# <class '__main__.Perro'>
```


## Tipos de métodos

* Instancia, son los métodos (def) comunes dentro de `class`.
* Clase, utilizando decorador `@classmethod`.
* Estáticos, metodos estáticos usando `@staticmethod`.


En el siguiente ejemplo, tenemos los tres tipos de métodos en una clase, esto puede variar.

```
class Clase(object):
    def metodo(self):
        return 'Método normal', self

    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls

    @staticmethod
    def metodoestatico():
        return "Método estático"
```



### Método de instancia

Metodos comunes y corrientes, con parametro de entrada es `self` que hace referencia a la instancia del método, puede recibir más argumentos.

* Pueden acceder y modificar los atributos del objeto.
* Pueden acceder a otros métodos.
* Se puede modificar el estado de la clase, mediante el uso de `self.class`.

### Método `classmethod`

`@classmethod`, reciben como argumento `cls`, esta hace referencia a la clase.
Puede acceder a la clase pero no a la instancia.
`@classmethod` es un decorador de método.
El método al cual se le aplica el decorador recibe `cls`.

* NO pueden acceder a los atributos de la instancia.
* Si pueden modificar atributos de la clase.


### Método `staticmethod`

`@staticmethod` es un decorador de método.
`@staticmethod`, no aceptan parámetros.
Es útil para indicar que un método NO modificará el estado de la instancia ni de la clase.
Son funciones normales pero van ligada a la clase concreta, nada más.

* NO pueden modificar el estado ni de la clase o de la instancia.


# Pilares de la programación orientada a objetos

La programación orientada a objetos está basada en 6 principios o pilares básicos:

* Herencia
* Cohesión
* Abstracción
* Polimorfismo
* Acoplamiento
* Encapsulamiento


# Herencia

Es el proceso que permite crear clases hijos desde una clase padre, heredando sus métodos y atributos, pudiendo agregar más métodos y atributos en los hijos.

```
class Animal(object):
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
        

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")



mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()
# Guau!
# Muuu!

mi_vaca.describeme()
mi_abeja.describeme()
# Soy un Animal del tipo Vaca
# Soy un Animal del tipo Abeja

mi_abeja.picar()
# Picar!
```


## super()

Permite acceder a métodos de la clase padre desde una de las clases hijas.

Por ejemplo, para agregar un atributo más a la clase hija, pero utilizando los atributos del padres podemos usar `super()` y entregar los parámetros de los atributos a utilizar y crear uno nuevo.

```
class Perro(Animal):
    def __init__(self, especie, edad, dueño): 
    	# Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño



mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
mi_perro.dueño
```



## Herencia múltiple

En Python, podemos heredar de múltiples clases padres, esto se hace al momento de crear la nueva clase y los argumentos son las clases.

Por ejemplo:
```
class Clase1(object):
    pass
class Clase2(object):
    pass
class Clase3(Clase1, Clase2):
    pass   
```

O que se herede de forma anidada.
```
class Clase1(object):
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
```

---

Pero, ¿cómo podemos saber a cuál método se está llamando si existen varios métodos similares en nombre?.

- **MRO**, Method Order Resolution, **__mro__**.

Muestra la forma en que el lenguaje resuelve un método o atributo, define el orden en el cual las clases base son buscadas cuando se ejecuta un método.

Esto depende del orden en que las clases son pasadas.

```
print(Clase3.__mro__)
# (<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)
```

---


## @property

Se usa para modificar un método para que se comporte como un atributo.
Al aplicar este decorador a un método, después se llama como método, dará error, puesto que se debe llamar como un atributo normal, sin `()`.

```
class Clase(object):
     def __init__(self, a):
             self.atributo = a
     
     @property
     def funcion(self):
             return self.atributo
 
 
clase = Clase('hola')
clase.atributo
#'hola'

clase.funcion
#'hola'
```



Esto hace lo mismo pero sin `@property`.

```
class Clase(object):
	def __init__(self, a):
		self.atributo = a


clase = Clase('hola')
clase.atributo
#'hola'
```



# Cohesión

Es el grado de relación entre los elementos de un módulo.
Pensar bien la tarea que va a realizar, intentando que sea única y bien definida.

* Cohesión débil: la relación entre los elementos es baja, no pertenecen a una única funcionalidad.

```
# Mal. Cohesión débil
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)

suma()
```

Es débil, porque que pasa si el usuario ya tiene los números y no quiere pedirlo por pantalla, la funcion "suma" no le servirá.


* Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del módulo.

```
# Bien. Cohesión fuerte
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total
```

Acá, se creó la función suma, con un solo objetivo, que es sumar y retornar el total. No importando la cantidad de números entregados, este hará la suma.


Normalmente el acoplamiento débil se relaciona con cohesión fuerte o alta.

---

Es importante buscar que las funciones realicen una única tarea (o conjunto) pero relacionadas entre sí. 

---


Esto permite:

* Reducir la complejidad del módulo, porque tendrá menor cantidad de operaciones.
* Se podrá utilizar los módulos más facilmente.
* El sistema será más fácilmente mantenible.



# Abstracción

Se refiere a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en cómo puede ser usada, lo que se conoce como **interfaz**.

Está muy relacionado con el enfoque **caja negra**.

Esta ofrece unas funciones de alto nivel, por lo general sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay adentro.

Por ejemplo, una televisión, la podemos usar, configurar, conectar, sin tener conocimientos en electrónica, electricidad, o estándares. Esta viene con una interfaz con la que interactuamos, es amistosa y podemos usarla fácilmente.

Una `clase abstracta` es la que contiene métodos abstractos, y se define como `métodos abstracto`.

Es posible crear métodos abstractos en Python utilizando el decorador `@absttractmethod`.



# Polimorfismo

Poly - muchas
Morfo - formas

Los objetos deben tomar diferentes formas:

* Polimorfismo dinámico (o polimorfismo paramétrico)
Es aquel en el que el código no incluye ningún tipo de especificación sobre el tipo de datos sobre el que se trabaja. Así, puede ser utilizado a todo tipo de datos compatible.

* Polimorfismo estático (o polimorfismo ad hoc)
Es aquél en el que los tipos a los que se aplica el polimorfismo deben ser explícitos y declarados uno por uno antes de poder ser utilizados.


Un objeto de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) segun cómo sean accedidos.

En pocas palabras, un único objeto puede tener múltiples estados y comportamientos, básicamente es la capacidad de los objetos de una clase, en responder de diferentes maneras a un solo mensaje, está estrechamente relacionada a la herencia, y que mayormente sucede gracias a este.

En Python tiene tipado dinámico, el polimorfismo va muy relacionado con el `duck typing`.

```
class Animal(object):
	def hablar(self):
		pass

class Perro(Animal):
	def hablar(self):
		print('Guau')


class Gato(Animal):
	def hablar(self):
		print('Miau')



for animal in Perro(), Gato():
	animal.hablar()


# Guau
# Miau
```


Es importante utilizar 'duck typing' para entender el polimorfismo en Python que es tipado dinámico.




# Acoplamiento

Mide la dependencia entre dos módulos distintos de software, como pueden por ejemplo las clases.

* Acoplamiento débil: indica que no existe dependencia de un módulo con otros. Este debe ser el objetivo de nuestro software.

* Acoplamiento fuerte: indica que un módulo tiene dependencias internas con otros.


El acoplamiento está muy relacionado con la cohesión, el acoplamiento débil suele ir ligado a la cohesión fuerte.
En el código se busca tener acoplamiento débil y cohesión fuerte, que tenga menos dependencias de módulos externos y que las tareas estén relacionadas entre sí.

Esto es porque:

* Debido a las dependencias con otros módulo, un cambio en un modulo ajeno al nuestro podría tener un “efecto mariposa” en nuestro código, aún sin haber modificado directamente nuestro módulo.

* Si un módulo tiene dependencias con otros, reduce la reusabilidad, ya que para reusarlo deberíamos copiar también las dependencias.


Ver el siguiente ejemplo:
```
class Clase1:
    x = True
    pass

class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor



mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
mi_clase.valor
```

Es sencillo, pero basta para explicar el problema de una acoplamiento fuerte.
Ahora se modificará la "Clase1", el atributo "x" pasará a "False". Esto repercute directamente en "Clase2" operando de forma negativa.

```
class Clase1:
    x = False
    pass

class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor



mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
mi_clase.valor
# Da error
```

El error generado es por el acoplamento fuerte con "Clase1", se modificó un atributo y "Clase2" falló.



# Encapsulamiento

Es el ocultamiento de los estados internos de un clase al exterior, es decir, no se pueden acceder desde el exterior a los atributos o métodos internos de una clase, si no, que el propio objeto puede acceder a ellos.

Para evitar que sean modificados de forma incorrecta.

En Python, el doble guión bajo antes del nombre de la variable (`__`) le indica que la "oculte" y no pueda ser accedida como un atributo normal. Queda ligada solamente a dicha clase.

```
class Clase(object):
	def __init__(self, valor):
		self.__atributo = valor
		


clase = Clase('hola')
clase.__atributo
# No se puede acceder desde el exterior
```


Esto es útil para evitar el acceso NO controlado a estas variables. Al definir `@property` el acceso a ese atributo se realiza por medio de una función, siendo así una forma controlada de acceder a este.

```
class Clase(object):
	def __init__(self, valor):
		self.__atributo = valor

	@property
	def control(self):
		return self.__atributo
		


clase = Clase('hola')
clase.control
# hola
```



`.setter`, es un decorador que permite definir un "método" que modifica el contenido del atributo.
```
class Clase(object):
	def __init__(self, valor):
		self.__atributo = valor

	@property
	def control(self):
		return self.__atributo

	@control.setter
	def control(self, nuevo):
		if nuevo != '':
			print('modificando el atributo valor')
			self.__atributo = nuevo
		else:
			print('"nuevo" está vacío')




clase = Clase('hola')
clase.control
# hola


clase.control = 'nuevo_valor'
clase.control
# nuevo_valor


clase.control = ''
clase.control
# '"nuevo" está vacío'
```


`setter`, es útil, por ejemplo, para realizar comprobaciones antes de establecer el nuevo valor del atributo oculto, una forma de control que asegura el correcto funcionamiento del objeto, esto no se puede hacer en un atributo normal.


Otro ejemplo, de encapsulamiento, usando '__' para que se interpreten como "privados":
```
class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()



mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
```


---

Usando `dir` para ver el listado de métodos y atributos de nuestra clase.
Podremos ver un listado de métodos normales y atributos de clase pero no podemos encontrar los métodos ni atributos privados.

```
print(dir(Clase)
```
---


Aunque, es posible, pero **no recomendable**, llamar a los métodos y atributos privados de la siguiente forma.
```
Clase._Clase__atributo_clase
# 'Hola'
```

