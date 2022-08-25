# Principos SOLID

Los principios SOLID son guías que pueden ser aplicadas en el desarrollo de software para eliminar malos diseños provocando que el programador tenga que refactorizar el código fuente hasta que sea
legible y extensible.

Puede ser utilizado con el desarrollo guiado por pruebas, y forma parte de la estrategia global del desarrollo ágil de software y desarrollo adaptativo de software.

Robert C. Martin, 1995, creó este concepto.


1. **S**ingle Responsability Principle (SRP).

Cada clase debe ocuparse de una sola cosa, debe tener un único motivo para ser modificada.
Por ejemplo, modificar una clase o los métodos de la clase por necesidad debido al cambio en la base de datos o en el negocio, es imperativo hacerlo.

Clases con nombres descriptivos, con pocos métodos.

* Una clase debería tener solo una razón para cambiar
* Cada responsabilidad es el eje del cambio
* Para contener la propagación del cambio, debemos separar las responsabilidades.
* Si una clase asume más de una responsabilidad, será más sensible al cambio.
* Si una clase asume más de una responsabilidad, las responsabilidades se acoplan.


2. **O**pen-Closed Principle (OCP).

Open-Closed, 1988, Bertrand Meyer.

* Una clase, módulo o función debe estar abierto a extensiones pero cerradas a modificaciones.

* Un módulo cerrado quiere decir que es utilizable para otros módulos, pero no modifica su información.

Modificar al alguna de estas partes del código, probablemente tengan dependencias en otros lugares, generará efectos indeseables o errores en cascada. Para evitar esto, el comportamiento de una parte debe ser alterado sin tener que modificar el propio código fuente.

Una forma de lograr esto, es mediante herencia y redefinición de métodos, donde la clase padre podría incluso ser abstracta.

Otra forma es inyectar dependencias que cumplan los requisitos, pero implementan funcionamiento diferente.

Cerrar en exceso conlleva a escribir demasiadas líneas de código al momento de reutilizar código.


> Una clase está cerrada, dado que puede ser compilada, almacenada en una librería y usada por otras clases de cliente. Pero también está abierta, dado que a partir de ella podríamos crear nuevas subclases que incorporaran características nuevas. Y al crear una subclase, no hay ninguna necesidad de modificar las clases cliente de la superclase.
> - Bertrand Meyer - concepto herencia de implentación (concepto de herencia).


A diferencia de Meyer, la definicion nueva (años 90) es la herencia a partir de clases abstractas, se pueden reutilizar especificaciones de interfaz mediante herencia pero no es necesario que exista una implementación. Por lo tanto, la interfaz queda cerrada a posibles modificaciones y las nuevas implementaciones deben implementar, como mínimo, esta interfaz.


3. **L**iskov Substitution Principle (LSP)

Princicio de substitición, 1987, Barbara Liskov.

- Si una función recibe un objeto como parámetro, de tipo X y en su lugar le pasamos oto de tipo Y, que hereda de X, dicha función debe proceder correctamente.

Los objetos de un programa deberían ser reemplazables por instancias de sus subtipos sin alterar el correcto funcionamiento.

Polimorfismo, los compiladores e intérpretes admiten este tipo de parámetros, la cuestión es si la función de verdad está diseñada para hacer lo que debe hacer, aunque reciba como parámetro no exáctamente X, sino Y.

Este principio está estrechamente relacionado con el anterior principio, por su extensiblidad de las clases cuando ésta se realiza mediante herencia o subtipo.

Si una función no cumple *LSP*, esta rompe *OCP*, porque para ser capaz de fusionar con subtipos (clases hijas) necesita saber demasiado de la clase padre y por tanto, modificarla.


4. **I**nterface Segregation Principle (ISP)

Cuando implementamos *SRP* también empleamos *ISP* como efecto colateral.

Muchas interfaces cliente específicas son mejor que una interfaz de propósito general, los clientes de un programa deben conocer solo aquellos métodos que realmente usan y no de aquellos que no.

El *ISP* defiende que no obliguemos a los clientes a depender de clases o interfaces que no necesita usar. Esto ocurre cuando una clase o interfaz tiene más métodos de lo que una clase hija o entidad hija necesita para sí.

Probablemente esta clase sirva a varios objetos hijos con responsabilidades diferentes, con lo que debería estar dividida en varias entidades.


5. **D**ependency Inversión Principle (DIP)

Da origen a la conocida inyección de dependencias, una de las mejores técnicas para lidiar con las colaboraciones entre clases, produciendo código reutilizable, sobrio, preparado para cambiar sin errores de efecto "bola de nieve".

- Un módulo concreto A, no debe depender directamente de otro módulo concreto B, sino de una abstracción de B. Esta abstracción es una interfaz o una clase (podría ser abstracta) que sirve de base para un conjunto de clases hijas.

- Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones (p.ej., interfaces).

- Las abstracciones no deberían depender de los detalles. Los detalles (implementaciones concretas) deben depender de abstracciones.

Debe depender de abstracciones, y no de implementaciones.

En lenguajes interpretados no se necesitan definir interfaces, pero el concepto aplica igualmente.

```

    Paquete A        Paquete B

    Objeto A         Objeto B
       ||               |
       \/               |
  Interface A   <-------|

```


## Principios SOLID con Python

1. Single Responsability Principle (SRP)

> Una clase debe tener una y solo una razón para cambiar.

Por ejemplo, una clase que calcule la mediana, promedio, etc.

Es de mala práctica que una función realice dichos trabajos, en lugar de ello, es conveniente fragmentar en varias funciones que realicen un trabajo en específico y que sean llamadas por una función principal.

```
def get_mean(list_):
    '''Compute Mean'''
    print(f"the mean is {np.mean(list_)}") 

def get_max(list_):
    '''Compute Max'''
    print(f"the max is {np.max(list_)}") 

def main(list_): 
    # Compute Average
    get_mean(list_)
    # Compute Max
    get_max(list_)

main([1,2,3,4,5])
# the mean is 3.0
# the max is 5
```

Ahora el código se puede cambiar más facilmente, los errores se identican más facilmente, el código es reusable.


2. Open-Closed Pinciple (OCP)

> Entidades de software debe estar abiertas a extensiones, pero cerradas a la modificación.

Ahora, cambiaremos el código anterior a clases, las funciones de calculo ahora serán subclases de clase "Operations", se puede omitir @abstractmethod si no se sabe del tema.
`Operations.__subclasses__()`, obtiene todas las subclases que tiene la clase `Operations`.

```
import numpy as np
from abc import ABC, abstractmethod

class Operations(ABC):
    '''Operations'''
    @abstractmethod
    def operation():
        pass

class Mean(Operations):
    '''Compute Max'''
    def operation(list_):
        print(f"The mean is {np.mean(list_)}") 

class Max(Operations):
    '''Compute Max'''
    def operation(list_):
        print(f"The max is {np.max(list_)}") 

class Main:
    '''Main'''
    @abstractmethod
    def get_operations(list_):
        # __subclasses__ will found all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(list_)


if __name__ == "__main__":
    Main.get_operations([1,2,3,4,5])
# The mean is 3.0
# The max is 5
```


3. Liskov Substitution Principle (LSP)

> Funciones deben ser capaces de recibir objetos heredados de otros objetos

Por ejemplo, si en una subclase, redefine una función que también está presente en la clase base, las dos funciones deberían tener el mismo comportamiento. Sin embargo, esto no significa que deban ser obligatoriamente iguales, sino que el usuario debe esperar el mismo tipo de resultado, dada la misma entrada.

El resultado de este principio es escribir el código de manera consistente y el usuario final necesitaría aprender cómo nuestro código funciona solamente una vez.


4. Interface Segregation Principle (ISP)

> Muchas interfaces son mejor que una interface de propósito general.

Los problemas se generan cuando subclases heredan métodos desde la clase base que no necesita.

Tener métodos fuera de contexto generan errores dificiles de capturar.

```
from abc import ABC, abstractmethod

class Mammals(ABC):
    @abstractmethod
    def swim() -> bool:
        print("Can Swim") 

    @abstractmethod
    def walk() -> bool:
        print("Can Walk") 

class Human(Mammals):
    def swim():
        return print("Humans can swim") 

    def walk():
        return print("Humans can walk") 

class Whale(Mammals):
    def swim():
        return print("Whales can swim")


Human.swim()
Human.walk()

Whale.swim()
Whale.walk()

# Humans can swim
# Humans can walk
# Whales can swim
# Can Walk
```

Las ballenas no caminan, para evitar este error debemos crear clases "Walker", "Swimmer" separadas con sus métodos respectivos.

```
from abc import ABC, abstractmethod

class Walker(ABC):
  @abstractmethod
  def walk() -> bool:
    return print("Can Walk") 

class Swimmer(ABC):
  @abstractmethod
  def swim() -> bool:
    return print("Can Swim") 

class Human(Walker, Swimmer):
  def walk():
    return print("Humans can walk") 
  def swim():
    return print("Humans can swim") 

class Whale(Swimmer):
  def swim():
    return print("Whales can swim") 

if __name__ == "__main__":
  Human.walk()
  Human.swim()

  Whale.swim()
  Whale.walk()

# Humans can walk
# Humans can swim
# Whales can swim
```


5. Dependency Inversion Principle (DIP)

> Un módulo de alto nivel no debe depender de un módulo de bajo nivel, si no que debe depender de una abstracción.

Por ejemplo, creamos un programa que lee un fichero con formato específico, para leer otro formato del fichero debemos crear otro programa. Evitamos esto utilizando una abstracción o interface por cual los módulos de alto y bajo nivel se comuniquen.

```
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter
    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    converter = AlphaConverter()
    app = App(converter)
    app.start()
    #
    con = FXConverter()
    app2 = App(con)
    app2.start()
```

App utiliza una interfaz "CurrencyConverter" que es una clase abstracta cuya anotación `-> float` nos quiere decir que recibe variables `float`

Al utilizar la clase abstracta "CurrencyConverter" podemos tener distintas "API" que cambien los datos y el código seguirá funcionando, por la interfaz creada.




