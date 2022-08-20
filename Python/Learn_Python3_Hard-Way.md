# 0 - Instalar Python

En Linux.

Ir a la página oficial de Python, descargar el paquete Python o instalar desde el administrador de paquetes incorporado de la distribución Linux.

En Fedora:

```bash
$ sudo dnf install python3 atom vim
```


Editores de texto se pueden usar: vi, vim, nano, PyCharm, Atom, entre otros.


Para entrar y salir, se utiliza la instrucción "exit()" o Ctrl + D, del interprete de Python desde la consola.

```bash

$ python --version
Python 3.10.4

$ python
>>> print("hola")
hola
>>> exit()
$
```


# 1 - Primer programa

Escribir el código utilizando la función incorporada "print", este imprime por consola el contenido que se le entrega entre paréntesis, puede ser literal o números.

```python
print("algo")
print(1)
print('12 algo')
```

Ejecutamos el script usando la consola.

```bash
$ chmod u+x ex1.py
$ python ex1.py
```

Cualquier error generado, se debe revisar la escritura del código y asegurarse que los entradas literales estén dentro de comillas dobles o simples, los números y strings estén dentro de los paréntesis.



# 2 - Comentarios y Caracteres

Comentarios son importantes en los programas, nos indican que se hace, también deshabilitan partes del programa que se necesita remover temporalmente.

Símbolo # se llama "octothorpe" o "almuadilla" (hash)

```python
#  Un
#     Comentario
#  Hastag "#" dentro de un comentario es ignorado
print("comentarios")

# deshabilitado
# print("nada")

print("run")
```


# 3 - Números y Matemática

Cada lenguaje de programación tiene números y matemática, se pueden realizar operaciones aritméticas con Python:

* +:  suma
* -:  resta
* /:  división
* //:  retorna entero de division
* *:  multiplicación
* ^:  potencia
* %:  modulo, remanente de división
* <:  menor que
* >:  mayor que
* <=:  menor o igual que
* >=:  mayor o igual que
* ==:  igual a



Existen valores Booleanos que son True y False, estos son comparadores lógicos que se obtienen al comparar o realizar una tarea lógica, por ejemplo: 12 == 12, retorna True, 50 >= 100, retorna False.


# 4 - Variables y Nombres

Variables, es una forma de almacenar información e identificarlo con un nombre.
Existen algunos nombres que están reservadas para el lenguaje Python y no se pueden usar.

A las variables se le puede asignar cualquier dato, desde un string, numeros, u objetos.

```bash
$ python
>>> help()
help> keywords
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
help> quit
>>>
```

Para usar una variable se debe escribir tal cual se declara.


Declarar variables en Python.

```python
variable1 = "hola"
variable2 = "mundo"
variable3 = "!"
print(variable1, variable2, variable3)
hola mundo !
```


Declarar una variable vacia, dará error, para evitar ello se puede usar algun valor y reasignar cuando sea necesario el nuevo contenido para esa variable.

```python
vacio = ""
print(vacio)

vacio = "nada por allá"
print(vacio)
nada por allá
```


# 5 - Más variables e Imprimir

Para imprimir un valor se usa "print" y los valores a imprimir se declaran dentro de un paréntesis y entre comillas si es una frase-declaración literal o números.

```python
print("hola")
hola
print(1)
1
print("")

print("123das")
123das

print(1,2,3,4)
1 2 3 4
```


Ahora, para imprimir una variable dentro de una frase o string, se debe usar una función especial, usando el siguiente formato.


```python
variable = "por acá"
imprimir = f"algo {variable}!"
print(imprimir)
algo por acá
```

Esto permite crear un string incorporando valores de variables en pocas líneas y con formato.



En números de punto flotante, o "float", se puede redondear usando "round()" entregando el número float y la cantidad de decimales para ese número.
Pasado 5 en el decimal, se le suma 1, de lo contrario se mantiene el número anterior.

```python
numero = 1.55555
print(round(numero, 1))
1.6
```



# 6 - String y Text

**string** es un pedazo de texto para mostrar algo o imprimir fuera del programa.
Python lo reconoce cuando se usa comillas dobles o comillas simples. Un string puede ser un número dentro de un texto o un texto en sí.

Recordar:

```python
a = 10
b = "10"
a == b
False
```

En este caso, a es del tipo "str" (string) y b es del tipo "int" (entero) y estos no son iguales aunque se vean iguales.


# 7 - Más String

Métodos de string o "str()"

Para utilizar un método se debe usar formato punto, es decir:
	"algo".método
	
	variable = "string"
	variable.método()


## Lista de métodos str.

.capitalize()  -  retorna una versión capitalizada de un string.
.title() -  retorna una versión del string con la primera letra de cada palabra en mayúscula.
.casefold()  -  devuelve una versión de la cadena adecuada para comparaciones sin mayúsculas y minúsculas.
.center(width, fillchar=' ')  --  retorna un string centrado con el largo width.
.lower()  -  retorna una copia del string en minúsculas.
.upper()  -  retorna una copia del string en mayusculas.

.count(patron)  -  retorna un número de veces que aparece el patron dentro del string.
.find(patron)  -  retorna el indice (número) del patron en el string.
.rfind(patron)  -  retorna el valor indice más alto (número) del patron en el string.

.encode(encoding='utf-8', errors='strict')  -  codifica el string usando codec entregado.

.startswith(prefijo)  -  retora True si string empieza con prefijo, de lo contrario False.
.endswith(prefijo)  -  retorna True si string termina con prefijo, de lo contrario Fasle.
.expandtabs(tabsize=8)  -  retorna una copia donde todos los carácter "tab" se expanden la cantidad de espacios ingresados, por defecto es 8.

.removeprefix(prefijo)  -  retorna string con el prefijo entregado si está presente.
.removesuffix(sufijo)  -  retorna string con el sufijo entregado si está presente.
.swapcase()  -  convierte carácteres mayusculas en minusculas y viceversa.


.format(string)  -  retorna la version formateada de un str con los valores de variables, los valores sustituidos se identifican con {}.
.format_map(mapping)  -  retorna una version de str usando sustitución desde mapping, los valores sustituidos se identifican con {}.
.index(string)  -  retorna el menor valor de índice (número) de string dentro de un str, error si no existe.
.rindex(string)  -  retorna el valor mayor de índice (numero) de un string dentro de un str, error si no existe.
.partition(separador)  -  parte el string en tres partes usando un separador.
.rpartition(separador)  -  parte el string en tres partes usando un separador.

.islower()  -  retorna True si es minuscula, False de no.
.isupper()  -  retorna True si el string está en mayúsculas, o False si no.
.isnumeric() - retorna True si el string es numérico, False de no.
.isdigit()  -  retorna True si es int() o False de no.
.isalnum()  -  retorna True si string es alfanumerico, False de no.
.isalpha()  -  retorna True si string es alfabético, False de no.
.isspace()  -  retorna True si es un espacio, False de no.
.istitle()  -  retorna True si es un string en formato título o False de no ser así.
.isascii()  -  retorna True si string es carácter ascii, False de no.
.isdecimal()  -  retorna True si string es numero decimal o False de no.
.isidentifier()  -  retorna True si string es un identificador string válido Python, False de no.
.isprintable()  -  retorna True si string es imprimible, False de no.

.translate(table)  -  reemplaza cada carácter en string usando la tabla entregada.
.maketrans()  -  retorna tabla usable de translación para .translate().

.split(separador, maxsplit=-1)  -  retorna una lista de palabras separadas por el "separador", se puede limitar las separaciones con "maxsplit".
.rsplit(separador, maxsplit=-1)  -  retorna una lista de palabras separadas por el "separador", se puede limitar las separaciones con "maxsplit".
.splitlines(keepends=False)  -  retorna una lista de líneas string, quebradas línea por línea, se incluye los salto de líneas si "keepends" es True.

.strip()  -  elimina los espacios al inicio y final del string.
.lstrip()  -  elimina espacios a la izquierda del string.
.rstrip()  -  elimina espacios a la derecha del string.

.replace(original, nuevo, count=-1)  -  reemplaza todos los carácteres original con nuevo, para limitar ingresar la cantidad "count".
.join(iterable)  -  concatena una cantidad de string entregado en formato lista.
.zfill(cantidad)  -  llena de 0 a la izquierda del string dependiendo de la cantidad entregada.
.ljust(width, fillchar=' ')  -  ajusta hacia la izquierda el string de laro width.
.rjust(width, fillchar=' ')  -  ajusta hacia la izquierda el string de laro width.



# 8 - Imprimir, Imprimir

"print" un poco más complejo.

Método ".format()" toma una posición declarada con "{}" y reemplaza con un valor de variable.

# 9 - Imprimir, Imprimir, Imprimir

Salto de línea dentro de un string, "\n".
String multiple línea con comillas dobles triples, """  """.


# 10 - What was that?

Carácter backslash (\) codifica carácteres dificiles en un string.

```python
string = """
Hola soy \"Dora\"\n
Me puedes hacer un sandwich?
(Le tiran un pan)
"""
print(string)
Hola soy "Dora"

Me puedes hacer un sandwich?
(Le tiran un pan)
```


## Secuencias Escape

| Escape | What it does. |
|-|-|
| \\ | Backslash (\) |
| \' | Single-quote (') |
| \" | Double-quote (") |
| \a | ASCII bell (BEL) |
| \b | ASCII backspace (BS) |
| \f | ASCII formfeed (FF) |
| \n | ASCII linefeed (LF) |
| \N | {name}Character named name in the Unicode database (Unicode only) |
| \r | Carriage return (CR) |
| \t | Horizontal tab (TAB) |
| \uxxxx | Character with 16-bit hex value xxxx |
| \Uxxxxxxxx | Character with 32-bit hex value xxxxxxxx |
| \v | ASCII vertical tab (VT) |
| \000 | Character with octal value 000 |
| \xhh | Character with hex value hh |



# 11 - Haz una pregunta

Ahora obtendremos información desde el programa ingresando datos, una forma de interactuar con el programa de forma básica, pero no menos importante.


```python
print("¿Cuál es tu edad?", end=' ')
age = input()
print("¿Cuál es tu altura?", end=' ')
height = input()
print("¿Cuál es tu peso?", end=' ')
weight = input()
print(f"Entonces, tienes {age} años, mides {height} y pesas {weight} kgs.")
```

- end=' ', le indica a "print" que no termine en un salto de línea.

* print:
	Función "print()" produce uno o más salidas legibles omitiendo las comillas dobles o simples e imprime carácteres especiales de escape.



# 12 - Mensaje a gente

Cuando se usa "input()", el string que se escribe entre los paréntesis será el mensaje mostrado en la consola, esperará datos ingresados por teclado.
Puede ser asignado a una variable y usar el valor ingresado después.


```python
age = input("¿Cuál es tu edad? ")
height = input("¿Cuál es tu altura? ")
weight = input("¿Cuál es tu peso? ")
print(f"Entonces, tienes {age} años, mides {height} y pesas {weight} kgs.")
```

***

**$ python -m pydoc [line_command]**:  permite obtener documentación sobre alguna instrucción Python (palabra reservada).

Por ejemplo:

```bash
$ python -m pydoc input
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

```

***


[Documentación **pydoc**](https://docs.python.org/3.10/library/pydoc.html)



# 13 - Parámetros, Desempacar, Variables

Al pasar parametros a un script se llaman argumentos, estos argumentos pueden ser obtenidos mediante el módulo "sys" y el método "argv".

Módulo son ficheros con códigos python que realizan alguna función determinada, estos pueden tener "Clases" y cada una tiene su propio "método" que no son más que funciones de una clase que relizan una operación determinada. (es más complejo que eso pero para fines simplificados está bien).

Para desempacar (unpack) una lista de argumentos, se tiene que asignar la cantidad exacta de variables para la cantidad de argumentos, sino, dará error.


```python
from sys import argv
namescript, arg2, arg3, arg4, arg5 = argv

print("Nombre script:", namescript)
print("Variable 1:", arg2)
print("Variable 2:", arg3)
print("Variable 3:", arg4)
print("Variable 5:", arg5)
```

"namescript, arg2, arg3, arg4, arg5 = argv":  Desempaqueta una lista de argumentos obtenidos, "argv".

Las posiciones de argumentos, 0 para el nombre del script, del 1 al X, son los parámetros de argumentos.

El error al desepacar se debe a que las variables no son suficientes a los argumentos o viceversa, por lo que se debe entregar la misma cantidad de argumentos con las mismas cantidades de variables.



# 14 - Imprimiendo y Pasando

Utilizando "input()" y "sys.argv" en un script con argumentos.

```python
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
```


# 15 - Leyendo ficheros

Al abrir ficheros se necesita abrir y cerrar, usando las instruccioes "open" y método "close()".

open():  crea un objeto llamado "file object", este objeto tiene métodos para poder procesar el contenido.

Es decir, abrir el fichero, realizar operaciones con el contenido del fichero y una vez realizado esas operaciones se debe cerrar.

Una forma de hacer es abrir, operar, y cerrarlo:
```python
file = open(filename)
file.read()
file.close()
```

La forma más "correcta", porque no se olvida cerrar un fichero una vez realizadas todas las operaciones, esta forma abre el fichero y lo cierra automáticamente al terminar las operaciones, el contenido se puede guardar en una lista o un string, pero el fichero se cierra.
```python
contenido = ""
with open(filename, 'r') as file:
	contenido = file.read()

print(contenido)
```


* .read:  método para leer el todo el contenido del fichero.


```python
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Fichero: {filename}")
print(txt.read())
txt.close()
```


## Métodos de la Clase File


# 16 - Leyendo y Escribiendo ficheros

Algúnos métodos que son más utilizado.

* close:  cierra el fichero.
* read:  lee todo el contenido del fichero, puede ser asignado a una variable.
* readline:  lee solamente una línea del contenido del fichero.
* truncate:  vacia el fichero.
* write('stuff'):  escribe "stuff" en el fichero.
* seek(0):  mueve la ubicación read/write al comienzo del fichero.


```python
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
```


# 17 - Más ficheros

Copiar un fichero a otro, para poder realizar esta tarea, se necesita leer el contenido de un fichero y escribir ese contenido en otro fichero, usar "argv", "os.path", "input", "open".

```python
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
```


"os.path.exists" comprueba si el fichero existe retoran True o si no retorna False.

Los módulos se deben importar usando "import".





# 18 - Nombres, Variables, Código, Funciones

Funciones son parte de código aislado dentro de un fichero Python, que puede ser reutilizado cuantas veces sea necesario, puede recibir parametros u otras funciones para que estos sean usados dentro de esa porción del código.
Funciones pueden retornar valores, que pueden ser usados por el código principal.


```python
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
```


* *args:  toma todas los argumentos o parámetros y los "guarda" en una lista.
* **kwargs:  toma todas los argumentos o parámetros y los "guarda" en un diccionario.


# 19 - Funcion y Variables

Funciones tiene cantidad de códigos de información que se puede considerar aislado del resto del código del código de Python.

```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
   print(f"Tienes {cheese_count} quesos.")
   print(f"Tienes {boxes_of_crackers} cajas de crackers.")
   print("Es suficiente.\n")

print("Cantidad de números:")
cheese_and_crackers(20, 30)

print("O usar variables para la función.")
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print("Realizar aritmética para las variables de función.")
cheese_and_crackers(10 + 20, 5 + 4)

print("Se puede combinar.")
cheese_and_crackers(amount_cheese + 20, amount_crackers + 4)

```



# 20 - Funciones y Ficheros

Se puede crear una función para leer un fichero.

```python
from sys import argv

script, input_file = argv

def print_Content(file):
    print(file.read())

def rebobinar(file):
    file.seek(0)

def print_a_line(line_count, file):
    print(line_count, file.readline())

current_file = open(input_file)

print("Imprimiendo el fichero completo.")

print_Content(current_file)

print("Rebobinar el fichero, así como una cinta")

rebobinar(current_file)

print("Imprimir tres líneas")

linea = 4
print_a_line(linea, current_file)

linea = linea + 1
print_a_line(linea + 1, current_file)

linea = linea + 1
print_a_line(linea + 1, current_file)

```


# 21 - Funciones pueden retornar algo

Keyword "return" permite retornar algun valor desde una función, esta se puede asignar en una variable.

```python
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

```


# 23 - String, Bytes, y Carácteres de codificación.

* String
* Encode y Decode string Python en "bytes".
* Manejar errores en string y bytes.

```python
import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<====>", cooked_string)
    
languages = open("languages.txt", encoding='utf-8')

main(language, input_encoding, error)

```

## Switches, Convenciones y Encodificación

Computadores modernos son muy complejos, pero en principio es el mismo. Estos usan electriciadad para cambiar entre encendido (1) y apagado (0), 1 - 0 bits.

Se usan 8 bites para encodificar 256 números (0-255).
00000000 = 0
11111111 = 255
00001111 = 15

Para grandes números se usan 16, 32, 64 bits.

Una vez que tiene bytes puedes empezar a almacenar y mostrar texto para decidir otra convención para saber cómo mapear un número en una letra. Al principios de los días de la computación donde muchas convenciones que mapean 8 u 7 bits (o menos) en lista de carácteres dentro de un computador. La mayor convención popular acabó siendo un Código Estándar Americano para Intercambio de Información, o ASCII. Este estándar mapea un número a una letra, por ejemplo; el número 90 es Z, en bytes 1011010, ese mapa está en una tabla ASCII dentro deun computador.

En consola Python:

```python
>>> 0b1011010
90
>>> ord('Z')
90
>>> chr(90)
'Z'
>>>
```


Al escribir un número 90 en binario.
* ord():  Se convierte en numero pasando a una letra 'Z'.
* chr():  Se convierte en letra pasando un número.



Convención ASCII para codificar un carácter usando 8 bits (un byte), podemos usar un string para convertir en una secuencia de bytes. Por ejemplo, "Zed A. Shaw" - [90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119].

Unicode - Universal Encoding, esta provee una tabla Unicode es como una tabla ASCII.

Python la convención de encodificado es llamado "UTF-8", "Unicode Transformation Format 8 Bits". Esto es una convención para codificar carácteres Unicode en secuencia de bytes, que son secuencia de bits. Puedes tambien usar otras convenciones (codificar), pero UTF-8 es actualmente el estándar.


```python
>>> raw = b'\xe6\x96\x87\xe8\xa8\x80'
>>> string = '文言'
>>> raw.decode()
'文言'
>>> string.encode()
b'\xe6\x96\x87\xe8\xa8\x80'
>>> raw == string.encode()
True
>>> string == raw.decode()
True
```



* .encode() - codifica el string a codigo entregado, por defecto usa 'utf-8'.
* .decode() - decodifica el string en formato binario codificado.

**DBES - Decode Bytes, Encode String**, convertir bytes a string y viceversa.


# 24 - 25 - Práctica y Más Práctica

Variables, Strings, métodos string, funciones, import, operaciones aritméticas.


# 26 - Take A Test

Corregir código Python, http://learnpythonthehardway.org/python3/exercise26.txt
Copiar el código, corregir los errores y ejecutar el código.


# 27 - Memorizando Lógica

| Operador | Descripción |
|-|-|
| and | a y b |
| or | a o b |
| not | not a |
| != | no es igual |
| == | es igual |
| >= | mayor que |
| <= | menor que |
| True | Verdadero |
| False | Falso |

| NOT | True? |
|-|-|
| not False | True |
| not True | False |


| OR | True? |
|-|-|
| True or False | True |
| True or True | True |
| False or True | True |
| False or False | False |

| AND | True? |
|-|-|
| True and False | False |
| True and True | True |
| False and True | False |
| False and False | False |


| NOT OR | True? |
|-|-|
| not(True or False) | False |
| not(True or True) | False |
| not(False or True) | False |
| not(False or False) | True |


| NOT AND | True? |
|-|-|
| not(True and False) | True |
| not(True and True) | False |
| not(False and True) | True |
| not(False and False) | True |


| != | True? |
|-|-|
| 1 != 0 | True |
| 1 != 1 | False |
| 0 != 1 | True |
| 0 != 0 | False |


| == | True? |
|-|-|
| 1 == 0 | False |
| 1 == 1 | True |
| 0 == 1 | False |
| 0 == 0 | True |


# 28 - Práctica Booleana

Expresiones Booleana lógica, existe en cualquier lenguaje de programación y es una parte fundamental de la computación.

1. True and True	# True
2. False and True	# False
3. 1 == 1 and 2 == 1	# False
4. "test" == "test"	# True
5. 1 == 1 or 2 != 1	# True
6. True and 1 == 1	# True
7. False and 0 != 0	# False
8. True or 1 == 1	# True
9. "test" == "testing"	# False
10. 1 != 0 and 2 == 1	# False
11. "test" != "testing"	# True
12. "test" == 1		# False
13. not (True and False)	# True
14. not (1 == 1 and 0 != 1)	# False
15. not (10 == 1 or 1000 == 1000)	# False
16. not (1 != 10 or 3 == 4)	# False
17. not ("testing" == "testing" and "Zed" == "Cool Guy")	# True
18. 1 == 1 and (not ("testing" == 1 or 1 == 0))		# True
19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))	# False
20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))	# False



# 29 - 30 - Sentencia if, elif, else

Sintaxis:

```python
if operacion_logica:
    sentencia
elif operacion_logica:
    sentencia
else:
    sentencia
```

# 31 - Tomando decisiones

Utilizando if, elif, else, sentencia if anidadas.


# 32 - Loops y Listas

Ciclos for

Sintaxis:
```python
for item in multipleContents:
    print(item)
```

multipleContents, puede ser una string, lista, tupla, diccionario, agrupacion, matrices, cualquier estructura con contenido iterable.


* range(inicio, final, saltos)


```python
for i in range(10, 20, 5):
    print(i)
```

Resultado 10, 15, el rango cuenta de 5 en 5 desde el 10 hasta el 20 sin incluir el último.


# 33 - While loops

Ejecuta código eternamente mientras la expresión es True, si se detecta algun False, el ciclo termina.

Sintaxis:

```python
while sentencia_logica:
    codigo
```


```python
i = 0
numbers = []
while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
	print(num)

```


# 34 - Accediendo elementos de una lista

Listas son muy usadas, cada elemento se debe acceder por medio de índice.

```python
animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals[0]
# bear
```

```python
animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
```

1. The animal at 1.
```python
animals[1]
# python3.6
```

2. The third (3rd) animal.
```python
animals[2]
# peacock
```

3. The ﬁrst (1st) animal.
```python
animals[0]
# bear
```

4. The animal at 3.
```python
animals[3]
# kangoroo
```

5. The ﬁfth (5th) animal.
```python
animals[4]
# whale
```

6. The animal at 2.
```python
animals[2]
# peacock
```

7. The sixth (6th) animal.
```python
animals[5]
# platypus
```

8. The animal at 4.
```python
animals[4]
# whale
```


# 35 - Branches and Funciones

Utilización de varias funciones, while, if.

# 36 - Diseño y Depuración

Algunas reglas de diseño y depuración para *if*, *for*, *while*.

## Reglas de sentencias *if*

1. Cada *if* debe tener un *else*.
2. Si este *esle* nunca se ejecutará porque no hace sentido, debe usar una funcion die o función de salida en el *else* que imprima un mensaje de error y muera o se termine. Esto podria encontrar muchos errores.
3. Nunca anidar sentencias *if* más de dos "pisos" de profundidad y siempre hacer de un nivel.
4. Tratar cada sentencia *if* como un párrafo, cada *if-elif-else* agrupado como un grupo de sentencia, con lineas blancas antes y después.
5. Pruebas Booleanas deben ser simple, si son complejas, mover esos calculos a variables en una función y usar un buen nombre para la variable.

## Reglas de ciclos *for*

1. Usar ciclos-while solamente para loops eternos, y esto sea probablemente nunca. Sólo aplicable para Python, en otros es diferente.
2. Usar un ciclo-for para todos los temas de ciclos, especialmente para un número limitado de cosas.


Tips Debugging

1. Usar un "debugger" para obtener información necesaria para corregir errores.
2. La mejor forma de depurar es usar "print()" para imprimir valores de variables en puntos del programa para ver que está mal.
3. Asegurar que las partes del programa funcionen como se espera, no escribir ficheros masivos de código antes de intentar ejecutarlo. Escribir un poco de código, ejecutar, corregir, escribir otro poco, ejecutar, corregir, en ese ciclo.


# 37 - Revisión de símbolos

Tablas de simbolos

## Keywords

| Keywords | Description | Example |
|-|-|-|
| not | "no" logico | not True == False |
| or | "o" lógico | True or False == True |
| and | logica "y" | True and False == False |
| as | parte de sentencia *with* | with X as Y: pass |
| assert | Asegurarse que algo es True | asser False, "error!" |
| break | detiene un loop al momento | while True: break |
| class | define una clase | class Person(object) |
| continue | no procesa más el loop, hace un salto | while True: continue |
| def | define una funcion | def X(): pass |
| del | borra de un diccioanrio | del X[Y] |
| if | condición if | if: X; elif: Y; else: J |
| elif | condición else if | if: X; elif: Y; else: J |
| else | condicion else | if: X; elif: Y; else: J |
| except | si una excepción ocurre, has esto | except ValueError as e: print(e) |
| finally | Excepciones o no, finalmente hace esto | finally: pass |
| for | loop sobre colección de cosas | for X in Y: pass |
| import | importa un módulo | import os |
| from | importa parte especifica de un módulo | from x import Y |
| global | declara una variable global | global X |
| in | parte de loop for | for X in Y: pass also 1 in [1] == True |
| is | es como == | 1 is 1 == True |
| lambda | crea función anónima | s = lambda y: y ** y; s(3) |
| pass | pasa el bloque | def empty(): pass |
| print | imprime un string | print('imprime') |
| raise | eleva una excepción cuando algo anda mal | raise ValueError('NO') |
| return | sale de una función con un valor | def X(): return Y |
| try | intenta este bloque, y si existe una excepción ir a *except* | try: pass |
| while | loop while | while X: pass |
| with | con una expresión como una variable, hacer | with X as Y: pass |
| yield | pausa aca y retorna para llamarlo | def X(): yield Y; X().next() |


## Data Types

| Type | Description | Example |
|-|-|-|
| True | valor booleano True | True or False == True |
| False | booleano False | False and True == False |
| None | Nada o ningun valor | x = None |
| bytes | Almacena bytes, puede ser cualquier cosa | x = b'hello' |
| strings | texto | x = 'hello' |
| numbers | numeros | x = 100 |
| floats | decimales | x = 1.1 |
| lists | lista | j = [1,2,3] |
| dicts | diccionario - key:value | e = {"a": 1, "b": 3, "c": 0} |


## String

| Escape | Description |
|-|-|
| \\ | Backslash |
| \' | single-quote |
| \" | double-quote |
| \a | bell |
| \b | backspace |
| \f | formfeed |
| \n | newline |
| \r | carriage |
| \t | tab |
| \v | vertical tab |


## Formato estilo viejo

| Escap | Description | Example |
|-|-|-|
| %d | numeros enteros | "%d" % 45 == '45' |
| %i | igual a %d | "%i" % 45 == '45' |
| %o | Octal number | "%o" % 1000 == '1750' |
| %u | Unsigned decimal | "%u" % -1000 == '-1000' |
| %x | Hexadecimal lowercase | "%x" % 1000 == '3e8' |
| %X | Hexadecimal uppercase | "%X" % 1000 == '3E8' |
| %e | Exponential notation, lowercase “e” | "%e" % 1000 == '1.000000e+03' |
| %E | Exponential notation, uppercase “E” | "%E" % 1000 == '1.000000E+03' |
| %f | Floating point real number | "%f" % 10.34 == '10.340000' |
| %F | Same as %f | "%F" % 10.34 == '10.340000' |
| %g | Either %f or %e, whichever is shorter | "%g" % 10.34 == '10.34' |
| %G | Same as %g but uppercase | "%G" % 10.34 == '10.34' |
| %c | Character format | "%c" % 34 == '"' |
| %r | Repr format (debugging format) | "%r" % int == "<type 'int'>" |
| %s | String format | "%s there" % 'hi' == 'hi there' |
| %% | A percent sign | "%g%%" % 10.34 == '10.34%' |



## Operators

| Operator | Description | Example |
|-|-|-|
| + | Addition | 2 + 4 == 6 |
| - | Subtraction | 2 - 4 == -2 |
| * | Multiplication | 2 * 4 == 8 |
| ** | Power of | 2 ** 4 == 16 |
| / | Division | 2 / 4 == 0.5 |
| // | Floor division | 2 // 4 == 0 |
| % | String interpolate or modulus | 2 % 4 == 2 |
| < | Less than | 4 < 4 == False
| > | Greater than | 4 > 4 == False |
| <= | Less than equal | 4 <= 4 == True |
| >= | Greater than equal | 4 >= 4 == True |
| == | Equal | 4 == 5 == False |
| != | Not equal | 4 != 5 == True |
| ( ) | Parentheses | len('hi') == 2 |
| [ ] | List brackets | [1,3,4] |
| { } | Dict curly braces | {'x': 5, 'y': 10} |
| @ | At (decorators) | @classmethod |
| , | Commarange | (0, 10) |
| : | Colon | def X(): |
| . | Dot | self.x = 10 |
| = | Assign equal | x = 10 |
| ; | Semi-colon | print("hi"); print("there") |
| += | Add and assign | x = 1; x += 2 |
| -= | Subtract and assign | x = 1; x -= 2 |
| *= | Multiply and assign | x = 1; x *= 2 |
| /= | Divide and assign | x = 1; x /= 2 |
| //= | Floor divide and assign | x = 1; x //= 2 |
| %= | Modulus assign | x = 1; x %= 2 |
| **= | Power assign | x = 1; x **= 2 |


## Leer código

Imprmir las partes usando "print()" para entender mejor que está haciendo.

Luego revisar:
1. revisar las funciones y que hacen
2. dónde y cómo se reciben el valor las variables.
3. cualquier variable con el mismo nombre en diferentes partes del programa. Un problema grande.
4. cualquier sentencia *if* sin clausulas *else*, está bien?
5. cualquier loop *while* que no termina.
6. cualquier parte de código que no entiendas por algun razón.


Despues, de revisar y entender, poner comentarios marcando donde vas, explicar funciones, dónde se usan, qué hacen, variables involucradas y cualquier cosa que se descubra en el código.

La parte más dificil, es seguir las variables línea por línea, función por función, imprimir variable.

# 38 - Listas

Las listas son una estructura de información comun, son elementos ordenados en orden y accedidos por medio de índices.


Lista - list() - []


.append(valor)  -  agrega al final de la lista.
.clear()  -  elimina toda la lista.
.copy()  -  copia de lista (shallow copy).
.count(valor)  -  numeros de ocurrencias de un valor.
.extend(iterable)  -  extiende lista agregando elementos de un iterable.
.index(valor)  -  retorna el índice del primer elemento encontrado.
.insert(indice, valor)  -  inserta elemento antes del índice.
.pop(indice)  -  elimina un item y retorna el índice del item.
.remove(valor)  -  elimina la primera occurencia del valor.
.reverse()  -  revierte orden.
.sort()  -   ordena lista ascendente.


lista = [inicio:final:saltos]	- rangos y saltos
lista[::-1]		-- invierte orden
lista[-1]		-- numeros negativos entregan item en orden descendente.



# 39 - Diccionario

Forma de almacenar informacion mediante "llave" y "valores", en principio, de forma similar a una "base de datos" para organizar información.

Estructura de información muy usada, es usado para mapear o asociar cosas que se quieran almacenar.


Diccionario - dict() - {}

.clear()  -  elimina todos los items del diccionario.
.copy()  -  copia de diccionario (shallow copy).
.get(key)  -  retorna valor mediante una "key", retorna por defecto si está establecido.
.pop(key)  -  elimina y retorna el valor correspondiente, se puede entregar valor que corresponde a "key" para eliminar especifico.
.popitem()  -  elimina y retorna el par (key, value) ultimo.
.setdefault()  -  inserta llave con un valor por defecto si la llave no está en el diccionario.
.update()  -  actualiza item de diccionario. 
.items()  -  provee tupla de key, values de todos los pares del diccionario.
.keys()  -  provee todas las llaves de un diccionario.
.values()  -  provee todos los valores de un diccionario. 



# 40 - Módulos, Classes, Objects

OOP (Object Oriented Programming), existe un constructor en Python llamad *class* que permite estructurar el software en una forma particular. Usando clases, puedes agregar consistencia al programa para ser usado de una forma limpia.

## Módulos

Modulos son:
1. Ficheros con código Python con algunas funciones o variables en este.
2. Se pueden importar todo o parte de estos códigos.
3. Se puede acceder a esas funciones o variables con operador *.* (punto).


Por ejemplo:

module_ex40.py
```python
mystuff = {'apple': 'I am apples!'}
print(mystuff)

def apple():
    print("I am apples!")
```


```python
>>> import modulo_ex40 as ex40
{'apple': 'I am apples!'}
>>> ex40.apple()
I am apples!
>>> ex40.mystuff
{'apple': 'I am apples!'}
>>> ex40.mystuff['apple']
'I am apples!'
>>> ex40.tangerine
'Living reflection of a dream.'
>>> 
```

## Classes

Se puede importar un módulo que tenga clases, estos se deben usar con notación punto (.), para usar los métodos (funciones de una clase) se debe utilizar notación punto.

* *object*  -  clase base de jerarquía de clase. Cuando es llamado, no acepta argumentos y retorna nuevas instancia sin características que no tiene atributos y no se entrega nada.


Métodos:
	__init__(self, /, *args, **kwargs)
		Initialize self.  See help(type(self)) for accurate signature.
	__delattr__(self, name, /)
		Implement delattr(self, name).
	__dir__(self, /)
		Default dir() implementation.
	__eq__(self, value, /)
		Return self==value.
	__format__(self, format_spec, /)
		Default object formatter.
	__ge__(self, value, /)
		Return self>=value.
	__getattribute__(self, name, /)
		Return getattr(self, name).
	__gt__(self, value, /)
		Return self>value.
	__hash__(self, /)
		Return hash(self).
	__le__(self, value, /)
		Return self<=value.
	__lt__(self, value, /)
		Return self<value>.
	__ne__(self, value, /)
		Return self!=value.
	__reduce__(self, /)
		Helper for pickle.
	__reduce_ex__(self, protocol, /)
		Helper for pickle.
	__repr__(self, /)
		Return repr(self).
	__setattr__(self, name, value, /)
		Implement setattr(self, name, value).
	__sizeof__(self, /)
		Size of object in memory, in bytes.
	__str__(self, /)
		Return str(self).


**__init__()**, inicializa el código de la clase al momento de usar la clase.
Al no usar "__init__", el código no es claro para crear instancias con distintas valores de variables.

Por ejemplo, en una clase, cheese = 'Frank' es ambiguo, self.cheese = 'Frank' es claramente "self.cheese" un *atributo* parte del objeto.


```python
class MyStuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")
```


Importar una clase, es similar a importar un módulo, utilizando la notación punto (.) y  sus métodos.


```python
>>> from class40 import MyStuff
>>> myclass = MyStuff()
>>> myclass.apple()
I am classy apple!
>>> myclass.tangerine
'And now a thousand years between'
>>> 
```


1. Pytho mira a "MyStuff()" y ve que es una clase definida.
2. Python crea un objeto vacío con todas los métodos (funciones) de la clase definidas.
3. Python busca si está "__init__()", self.
4. En este caso, *self.tangerine* es una canción y será inicializado por el objeto.
5. Python puede tomar nuevamente un objeto y asignarlo a una variable.


Una clase es como un "plano" para construir una copia de un tipo de cosa.

* Clases son como planos o definiciones para crear nuevos "mini-modulos".
* Instanciación es cómo se hace uno de esos "mini-módulos" y los importa al mismo tiempo.
* El "mini-modulo" creado es llamado *Objeto*, este puede ser asignado a una varaible para trabajar con ello.


```python
# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
```


Ejemplo:

Canta una canción.

```python
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
		"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

```


## Palabras clave de Clases

* **class**  -  crear un nuevo objeto o cosa.
* **object**  -  significa dos cosas: tipo de objeto más básico, y una instancia de cualquier objeto o cosa.
* **instance**  -  un objeto derivado de un objeto padre.
* **def**  -  define métodos dentro de una clase.
* **self**  -  dentro de una funcion de clase, "self" es una variable para que sea accedido por una instancia/objeto.
* **inheritance**  -  es la obtención de métodos, atributos de una clase padre a una clase hija.
* **composition**  -  una clase compuesta de partes de otras clases.
* **attribute**  -  propiedad de composición de una clase y son usualmente variables.
* **is-a**  -  una fase que hereda algo de otra, ejemplo, "salmon" is-a "fish".
* **has-a**  -  una fase para decir que algo está compuesto de otras cosas, un "salmon" has-a "mounth".


| | |
|-|-|
| **class X(Y)** | Crea una clase nombrado X con is-a Y |
| **class X(object): def __init__(self, J)** | Clase X has-a __init__ que toma "self" y un parámetro J |
| **class X(object): def M(self, J)** | clase X has-a funcion nombrada M que toma "self" y un parámetro J |
| **foo = X()** | Establece una instancia "foo" de la clase X |
| **foo.M(J)** | De "foo", obtiene la función "M", y llama con parámetro "self", y J |
| **foo.K = Q** | De "foo", obtiene atributo K, y estalece a Q |



Se pueden usar los siguientes sentencias para ejercitar la relaciones y entender mejor los objetos con otros que puedes crear.

1. “Make a class named ??? that is-a Y.”
2. “class ??? has-a __init__ that takes self and ??? parameters.”
3. “class ??? has-a function named ??? that takes self and ??? parameters.”
4. “Set ??? to an instance of class ???.”
5. “From ???, get the ??? function, and call it with self=??? and parameters ???.”
6. “From ???, get the ??? attribute, and set it to ???.”




## is-a, has-a, Objects, Classes

Un importante concepto que debes entender es la diferencia entre clase y objeto.

¿Cúal es la diferencia entre un pez y un salmon?

Hay que tomar un minuto para pensar, un pez y un salmon son diferentes pero son lo mismo. Un salmon es un pez, es un *tipo* particular de pez, es diferente a otros peces.
Un salmón es un pez, pero no todos los peces son salmones, en este caso cla clase es "pez", "salmon" también es una clase.

Ahora a dos salmones se le pone nombre, Frank y Caty. Caty tiene una pinta blanca, Frank es de color salmon uniforme, los dos son peces, los dos son salmones, pero son diferentes. Frank y Caty son *instancias* de la clase "salmón" y que a su vez es una clase de "pez". Frank y Caty son objetos.


Class --> Class  --> object (instance), objects (instance)
pez   --> salmon -->  Frank,             Mary


Objeto es una clase es una clase.


**is-a**, usado para objetos y clases relacionados con cada uno de los otros por medio de una clase relacionada.
**has-a**, usado para objetos y clases que están relacionados solamente porque ellos son *referencia* a otro.


```python
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a object
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## is-a object
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## is-a object
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## is-a object
class Fish(object):
    pass

## is-a object
class Salmon(Fish):
    pass

## is-a object
class Halibut(Fish):
    pass

## rover is-a Dog is-a Animal
rover = Dog("Rover")

## is-a Cat is-a Animal
satan = Cat("Satan")

## is-a Person
mary = Person("Mary")

## has-a pet satan
mary.pet = satan

## is-a Employee is-a Person
frank = Employee("Frank", 120000)

## has-a pet over
frank.pet = rover

## is-a Fish
flipper = Fish()

## is-a Salmon is-a Fish
crouse = Salmon()

## is-a Halibut is-a Fish
harry = Halibut()
```


## class Algo(object)

En Python3, no se necesita agregar *(object)* después de la clase, pero la comunidad Python cree en **"explícito es mejor que implícito"**, entoncés los expertos en Python decidieron incluirlo.
Se puede omitir *(object)* en clases simples, estas clases están perfectamente bien cuando son simples y trabajan con clases para crear un *(objet)*.

En Python2, existen diferencia entre dos tipos de clases. Por ejemplo, "clase Name es una clase de tipo object", en otras palabras, "Name(object) es una clase básica simple".

Filosofía Python dicta: **explícito mucho mejor que implícito**.


## super()
**super(Employee, self).__init__(name)**  -  dice como ejecutar el método __init__ de una clase padre relacionada.

**super()** permite la herencia en paradigma orientada-objetos.

**super()** - permite llamar los métodos construidos previamente en la otra clase, ahorrando la necesidad de reescribir código en la subclase, permitiendo intercambiar superclases con mínimo de cambio de código.


```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

```


# 41 - Análisis básico Orientado-Objeto y Diseño

Pasos para programar Orientado a objetos, estos pasos no son una ley, sino, una guia de cómo poder resolver la mayoria de los problemas.

El proceso tiene lo siguiente:

1. Escribir o dibujar el problema.
2. Extraer conceptos claves e investigar sobre estos.
3. Crear una clase jerárquica y mapear objetos para los conceptos.
4. Codificar las clases, ejecutarlas, testearlas.
5. Repetir y mejorar.


Este proceso tiene el sentido de arriba hacia abajo, al comienzo es muy abstracto, lentamente las ideas las redefines hasta que se vuelva sólida y puedas programarla.

Comienza escribiendo sobre el problema, pensar en todos o gran parte de los conceptos sobre este. Dibujar un diagrama, mapear algunos temas, o incluso escribir una serie de textos describiendo el problema. Esto te permitirá expresar los conceptos claves en el problema y explorar lo que ya sabes sobre ese problema.

Notas, dibujos, descripciones, conceptos claves. Crear lista de todos los pronombres y verbos en los apuntes realizados y relacionar estos pronombres y verbos. Esto te dará una buena lista de nombre de clases, objetos, y funciones para el siguiente paso. Tomar esa lista de conceptos e investigar cualquier cosa que no se entienda para poder redifinirlos en el futuro si se necesita.

Listo eso, se puede crear un arbol de conceptos y como ellos se relacionan con las clases. Usualmente se puede tomar una lista de sustantivos y preguntarse, ¿es esto otro concepto sustantivo?, ¿tienen alguna clase padre en común?, ¿cómo se llaman?, hacer esto hasta que se tenga una herarquía de clases como un arbol  de clases o un diagrama.
Entonces tomar los verbos y ver si estos son nombres de métodos (funciones) para cada clase y ponerlos en el arbol.

Con la jerarquía de clase descubierta, sentarse a escribir la estructura básica del código que tendrán las clases, métodos.
Escribir las pruebas para el código y asegurarse que las clases trabajen con sentido. Algunas una prueba basta, otras más de una, hacer esto hasta tener todas las cosas construidas.

Finalmente, mantener el ciclo del proceso, repetir y mejorar, haciendo más claro cada vez la implementación.

Si te estancas en cualquier parte por un concepto o problema que no viste anteriormente, vuelve a el proceso hasta descubrir cómo resolverlo para continuar.



## Análisis de un simple motor de juego.

El juego que se quiere crear se llama "Gothons from Planet Percal #25", es una pequeña aventura. Con simplemente el concepto en mente, se puede explorar la idea de descubrir cómo se construirá el juego.

### Escribir o Dibujar el problema

Un pequeño párrafo del juego:

"Aliens han invadido una nave espacial y nuestro heroe tiene que ir a traves de un laberinto de habitaciones para que pueda escapar en una cápsula al planeta siguiente."

Este juego es de tipo "Zork or Adventure" con salidas de texto y formas divertidas de morir. El juego involucra un motor que ejecuta un mapa completo de habitaciones y escenarios. Cada habitación imprime su descripción propia cuando el jugador entra en este y el motor le dice qué habitación es la siguiente en el mapa.


A este punto se tiene una buena idea del juego y cómo se va a ejecutar, entonces:

* **Morir**, es cuando el jugador muere y pasa algo divertido.
* **Corredor central**, punto de inicio y tiene un "Gothon" listo esperando que el jugador lo derrote con una broma antes de continuar.
* **Armería Laser Weapon**, Esto es donde el jugador obtiene una bomba de neutro para explotar la nave antes de irse en la cápsula. Esta bomba tiene un teclado numérico para activarla y detonarla.
* **El puente**, otro escenario de batalla con un "Gothon" en la habitación donde el jugador debe poner la bomba.
* **Cápsula de escape**, Es en dónde el jugador escapa, pero solamente en la capsula correcta.


A este punto se dibuja un mapa de estos puntos, escribir una descripción de cada habitación, cualquier cosa que se viene a la mente para explorar este problema.


### Extraer conceptos claves e investigarlos

Ahora se tiene información suficiente para extraer algunos sustantivos y analizar sus clases jerarquicas.

Empezar por todos los sustantivos:

* Alien
* Player
* Ship
* Maze
* Room
* Scene
* Gothon
* Escape Pod
* Planet
* Map
* Engine
* Death
* Central Corridor
* Laser Weapon Armory
* The Bridge


También se puede explorar todos los verbos y ver si algunos de esos pueden ser buenos nombres de los métodos, opcional.

A este punto se está investigando cada uno de esos conceptos y cualquier cosa que no se sabía. Por ejemplo, se puede jugar algunos tipos similares de juego para asegurarse como este proyecto funcionará. Investigar como la nave son diseñadas o como funcionará la bomba. Quizas investigar algunos temas técnicos como almacenar el estado del juego en una base de datos.
Despues de investigar estos temas, volver al paso 1 basado en la nueva información obtenida, rescribir las descripciones y extraer nuevos conceptos.


### Crear una Clase jerarquica y Mapa de Objetos para los conceptos

Listo lo anterior, se debe convertir en clases jerarquicas respondiendo, ¿qué cosas similares tienen entre ellos?, ¿cuáles son básicamente los mismo pero con otras palabras?.

"Rooms" y "Scene" son básicamente la misma cosa dependiendo en cómo se quieren hacer las cosas.
Por ejemplo, al tomar "Scene" para este juego, podemos ver todas las salas específicas, como "Corredor central" es básicamente una "Scene", "Muerte" es básicamente una "Scene", confirmando la elección de "Scene" sobre "Rooms". "Maze" y "Map" son básicamente lo mismo, "Map" es más óptimo. No se busca un sistema de batalla, se retomará "Alien" y "Player" para después. "Planet" puede ser otro escenario en lugar de algo en específico.

Después de todo este proceso, se tiene una jerarquía inicial:

* Map
* Engine
* Scene
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * El Puente
  * Cápsula de escape


Descubriendo qué acciones se necesitan para cada cosa basado en verbos descritos.

* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * El Puente
  * Cápsula de escape


"- enter" está bajo de Scene porque se que todas las escenas lo heredarán y tendran que sobre-escribirlo después.


### Codificar las Clases y testearlas

Una vez que se tiene el arbol de clases y algunos métodos, se abre el editor y se escribe el código para estos. Usualmente, se copia y pega el arbol jerárquico de clases visto anteriormente y se completa con el código.

```python
class Scene(object):
    
    def enter(self):
    	pass

class Engine(object):
    
    def __init__(self, scene_map):
        pass

    def play(self):
    	pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):
    
    def enter(self):
	pass


class Laser Weapon Armory(Scene):
    
    def enter(self):
	pass


class ElPuente(Scene):
    
    def enter(self):
	pass


class EscapePod(Scene):
    
    def enter(self):
	pass


class Map(object):

    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

```


En este fichero, simplemente replicamos la jerarquía. Agregar el código al final para ejecutar y ver si todo funciona como está en la estructura básica. En las siguientes secciones se llena con el código y se hace que funcione acorde con la descripción del juego.


### Repetir y Mejorar

En este paso, no es más que un while-loop, vuelve sobre todo el proceso y mejora basado en la información que se aprendió hasta ahora. No siempre se tiene una ruta fija, a veces se logra hasta el paso 3 y se necesita trabajar en el paso 1 y 2, para volver a continuar. A veces, saltar al final para poder resolver problemas.

A veces procesar todo y no solamente en una parte puede ayudar a resolver los problemas particulares, por ejemplo, no se sabe como escribir el método "Engine.play", puedo detener y hacer todo el proceso solo en una función para describir cómo escrirlo.



## De arriba hacia abajo vs De abajo hacia arriba

El proceso es tipicamente etiquetado "arriba abajo" desde el inicio para las parte de conceptos más abstractos (parte de arriba o superior) y trabajo de forma descendiente para la implementación actual. Si se quiere usar este proceso se debe describir cuando se analizan los problemas en los libros desde ahora, pero deberías conocer que existen otras formas de procesos para resolver problemas en programación que inicia con código y va "hasta" conceptos abstractos. Existe otras formas de etiquetar "abajo arriba". Estos son los pasos generales que puedes seguir:

1. Tomar una pequeña pieza del problema, hackear algun código y hacer que se ejecute apenas.
2. Mejorar el código en algunas cosas más formal con clases y pruebas automatizadas.
3. Extraer conceptos claves que usarás e investigar.
4. Escribir una descripción de que se está haciendo.
5. Volver a redefinir el código, posiblemente saliendose y empezar otra vez.
6. Repetir, moviendo algunas parte del problema.


Este proceso es mejor cuando se tiene una habilidad de programación más sólida y de forma natural penzar en el código sobre el problema. Este proceso es bueno cuando se conoce las pequeñas piezas de un puzzle, quizas no se tenga suficiente información todavía sobre todos los conceptos.

Segmentando en pequeñas piezas y explorar con código irás lentamente escarbando hasta el problema hasta resolverlo. Sin embargo, recordar que la solución sea probablemente raro y confusa, entonces se debe volver a empezar en el proceso para encontrar cosa a investigar, limpiar cosas basados en lo que aprendiste.



## El código para “Gothons from Planet Percal #25”


Código "ex43.py", 




## Herencia versus Coposicion

En historias magicas sobre heroes derrotando villanos, siempre existen en un bosque oscuro o algo así. Puede ser una cueva, bosque, otro planeta, solamente algun lugar que cualquiera sabe que el héroe no debería ir. Por supuesto, el villano entra, y el héroe va a ese lugar a matar al malo. ALgunas situaciones requieren poner en riesgo la vida del héroe en ese lugar malvado.

En programación orientada a objeto, la "herencia", es el "bosque malvado". Programadores experimentados saben como evitar este "mal" porque saben que tan profundo es dentro del "bosque oscuro" de la herencia y está la reina malvada de herencias multiples, que añade complejidad a los softwares y a programadores, pero el bosque estan poderoso que cada programador debe entrar e intentar salir con vida antes de llamarse a sí mismos programadores reales. Debes resistir las herencias y seguir, después de la aventura, aprenderás a estar fuera del bosque estúpido y te entregará armas para tener más fuerza contra ese "mal" complejo.

> *Muchos de los usos de herencia pueden ser simplificados o reemplazados con composición, y multiples herencias deberían ser evitados a toda costa.*


## ¿Qué es herencia?

Es indicar que una clase obtiene muchas o todas las características de las clases padres. Esto pasa implícitamente cuando escribes una clase, por ejemplo, *class Foo(Bar)*, la cual dice "crear una clase Foo con herencia de Bar". Al hacer esto, el lenguaje crea alguna accion para hacer esto una instancia de Foo también trabaje como si fuera hecha para una instancia de Bar.
Haciendo esto permite poner funcionalidad comun en la clase Bar, entonces especializar la funcionalidad en clase Foo como se necesite.

Cuando estas haciendo estas especialización, existe 3 maneras que las clases padres e hijos puedan interactuar:

1. Acciones en el hijo implique una accion en el padre.
2. Acciones en el hijo sobre-escriba la acción en el padre.
3. Acciones en el hijo altere la acción en el padre.


### HErencia implícita

Muestra acciones implicitas que ocurren cuando se define una funcion en el padre pero no en el hijo.

```python
class Parent(object):

  def implicit(self):
    print("Parent implicit()")

class Child(Parent):
  pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
```

```bash
$ python ex44a.py
PARENT implicit()
PARENT implicit()
```


El hijo hereda todo del padre.


### Sobre-escritura explícita

El problema con las funciones implícitas es que a veces se quiere que el hijo tengan comportamiento diferente. En este caso se busca sobre-escribir la funcion en el hijo, reemplazando la funcionalidad.

```python
class Parent(object):
  def override(self):
    print("PARENT override()")
   
class Child(Parent):
  def override(self):
    print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
```

```bash
$ python ex44b.py
PARENT override()
CHILD override()
```


En este caso hijo sobre-escribe función "override()" del padre a la propia del hijo.


### Alterar antes o después

La tercera forma es usar herencia con un caso especial de sobreescritura donde se quiere alterar el comportamiento antes o después de la clase padre se ejecute.
Primero sobreescribe la función como el ejemplo anterior, pero entonces usar una función incorporada llamada **super()** para obtener la version padre para llamar.

```python
class Paret(object):
  def altered(self):
    print("PARENT altered()")
   
class Child(Parent):
  def altered(self):
    print('CHILD, Before PARENT altered()')
    super(Child, self).altered()
    print('CHILD, After PARENT altered()')

dad = Parent()
son = Child()

dad.altered()

son.altered()
```

```bash
$ python ex44c.py
PARENT altered()

CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
```



Las líneas de "altered()" de "Child" son importantes:
1. porque se sobre-escribió "Parent.altered" a la version de "Child.altered".
2. en este caso se hizo un "antes" y "despúes" de la línea "super()" de la version "Parent.altered".
3. Línea "super(Child, self).altered()", se ocupa de la herencia y obtendrá la clase "Parent" por ti. Se permite leer como "llamar *super* con argumentos *Child* y *self*, entonces llama la función *altered*".
4. A este punto, la version "Parent.altered" se ejecuta, y entonces imprime el mensaje "Parent".
5. Finalmente, retorna desde "Parent.altered" y la función "Child.altered" continua la impresión del mensaje.


### Todos los comandos juntos

```python
class Parent(object):
  def override(self):
    print("PARENT override()")

  def implicit(self):
    print("PARENT implicit()")

  def altered(self):
    print("PARENT altered()")

class Child(Parent):
  def override(self):
    print("CHILD override()")

  def altered(self):
    print("CHILD, BEFORE PARENT altered()")
    super(Child, self).altered()
    print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
```

```bash
$ python ex44d.py
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
```


## La razon para super()

Debería ser de sentido común, pero cuando tienes un problema con algo llamado multiples herencias. Esto ocurre cuando defines una clase que herede desde uno o más clases:

```python
class SuperFun(Child, BadStuff):
  pass
```

En este caso, cada vez que tenga acciones implícitas en cualquier instancia de SuperFun, Python tiene que buscar la posible función en la jerarquía de clases tanto para Child como para BadStuff, pero debe hacerlo en un orden coherente. Para hacer esto, Python usa el "orden de resolución del método" (MRO) y un algoritmo llamado C3 para aclararlo.

Debido a que el MRO es complejo y se usa un algoritmo bien definido, Python no puede dejar que usted lo haga correctamente. En cambio, Python le brinda la función super(), que maneja todo esto por usted en los lugares en los que necesita el tipo de acciones de alteración como lo hice en Child.altered. Con super() no tiene que preocuparse por hacerlo bien, y Python encontrará la función adecuada para usted.


### Usando super() con __init__

El más común de uso de *super()* es actualmente en funciones *__init__* en las clases base. Este es usualmente el único lugar donde se necesita ahcer alguna cosa en un hijo, entonces completa la inicialización en el padre.

```python
class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
```


Esto es mucho más parecidor a "Child.altered" del ejemplo anterior, excepto que está establecido en algunas variables en "__init__" antes de tener que inicializar "Parent" con su "Parent.__init__".


## Composicion

Herencia es muy usado, pero otra forma de hacer exáctamente lo mismo es *usar* otra clase y modulos, en lugar de usar herencia implícita.

Existen 3 formas de realizar herencia, dos de las tres escriben nuevo código para reemplazar o alterar funcionalidades. Esto es facil de replicar solo llamando funciones en un módulo.

```python
class Other(object):
  
  def override(self):
    print('other override()')
  
  def implicit(self):
    print('other implicit()')
  
  def altered(self):
    print('other altered()')


class Child(object):

  def __init__(self):
    self.other = Other()

  def implicit(self):
    self.other.implicit()

  def override(self):
    print('child override()')

  def altered(self):
    print('child, before other altered()')
    self.other.altered()
    print('child, after other altered()')


son = Child()
son.implicit()
son.override()
son.altered()
```

```bash
$ python ex44.py
other implicit()
child override()
child, before other altered()
other altered()
child, after other altered()
```


Se puede ver que mucho del código "Child" y "Other" contienen la misma cosas, la diferencia radica que en "Child.implicit" se especificó hacer una acción tomando "Other".


## Cuando usar Herencia o Composición

"Herencia vs Composition" viene a menos para intentar resolver el problema de código reusable. No se quiere duplicar código en el software, esto no es limpio y eficiente.
Herencia resuelve este problema para crear un mecanismo para que tengas implicados características en base a clases.
Composicion resuelve este problema entregando modulos y la capacidad de llamar funciones en otras clases.

Ambas soluciones resuelven el problema de reusar, ¿cuál es la opción más apropiada? La respuesta es subjetiva, aca hay una guía de elegir:

1. Evitar múltiple herencia a toda costa, esto es complejo para ser seguro. Si te estancas con esto, entonces debes conocer la jerarquía de clases y gastar tiempo encontrando dónde viene cada cosa.

2. Usar composición para empaquetar código dentro de módulos que son usados en muchos lugares diferentes sin relaciones y situaciones.

3. Usar herencia solamente cuando exista clara relación entre piezas reusables que están bajo el mismo concepto en común o si lo tienes que hacer porque lo estás usando tu.


POO es una convención social de programadores qe crean paquetes y comparten código.



# 45 - Crea un juego

Requisitos:

1. Crear un juego diferente al visto.
2. Usar más de un fichero, usar *import*.
3. Usar una *class* por habitación y entregar los nombre de clases acorde a sus propósitos.
4. Al ejecutar, debe conocer sobre esas habitaciones, entonces hacer una clase que los ejecute y conozca sobre ellos. Asegurarse de que cada habitación retornen la habitación siguiente o establezcan alguna variable para saber cuál es la habitación siguiente.


Usar el tiempo necesario.
Utilizar clases, funciones, diccionarios, listas, o cualquier método que requieras.

Programación es resolver problemas, esto quiere decir prueba cosas, experimenta, falla, hurga tu trabajo, y vuelve a intentar. Cuando te atasques, busca ayuda, muestra tu código. Enfócate en tu código, mantente trabajando en el, limpialo hasta que esté bueno y legible acorde a PEP y entonces haz algo más.


## Estilo de Funciones

* Mantener funciones pequeñas y simples.
* Nombres que tengan sentido con lo que haran.

## Estilo de Clases

* Las funciones deben usar "camel case", es decir, nombrarse del siguiente formato: "SuperGoldFactory" en lugar de "super_gold_factory".
* Intentar no usar mucho *__init__*. Esto hace dificil de usar.
* Métodos (funciones) deben usar formato guion bajo.
* Ser consistente en orgarnizar los argumentos de los métodos.
* Intentar no usar variables que sean desde el módulo o globales.
* Siempre tener formato *class Name(object)* o tendrás muchos problemas.

## Estilo de código

* Espacio vertical para que pueda ser leído.
* Prueba hacer cosas que la gente hizo en Python, hasta que tu tengas tu propio estilo.
* Si encuentras algo de tu estilo, intenta algo que se asemeje a ese estilo.

## Buenos comentarios

* Escribir comentario de lo que hace las partes involucradas.
* Por qué está haciendo eso.
* Ser preciso, breve y sensato para escribir comentarios o documentación. Que tenga sentido.

## Evalúate

Con papel y lapiz anota todos tus errores, lee tu código y escribe lo que mejorarías. Una vez listo, arregla eso y repite este paso.



# 46 - Esqueleto del proyecto

Directorio 'skeleton' tiene todo lo básico que necesita para queun proyecto esté listo y se pueda ejecutar. Este tiene el diseño del proyecto, pruebas automaticas, módulos y los scripts de instalación.

Cuando se crea un nuevo proyecto, solo copia este directorio a uno nuevo y edita los ficheros para comenzar.


## macOS/Linux Setup

Primero que todo, necesitas instalar algunos softwares para Python usando `pip`.

Instalar pip, setuptools.

```bash
$ python -m ensurepip --upgrade
$ pip install setuptools
$ pip install virtualenv
```

Una vez instalado, se debe crear una instalación "fake" de Python, el cual permite administrar versiones de los paquetes para los diferentes proyectos.

```bash
$ mkdir ~/.venvs
$ virtualenv --system-site-packages ~/.venvs/virtEnv
$ source ~/.venvs/virtEnv/bin/activate
(virtEnv) $
```

Con lo anterior:
* Se creó en el HOME el directorio "venvs".
* Se creó un entorno virtual con "virtualenv".
* Se activó ese entorno virtual con "source".


Instalar "nose", un framework de pruebas.

```bash
(virtEnv) $ pip install nose
```

Paquete `nose` fue abandonado, por lo que se debe buscar alternativa.


## Crear un Directorio de proyecto Skeleton

```bash
$ mkdir projects
$ cd projects
$ mkdir skeleton
$ cd skeleton
$ mkdir bin NAME tests docs
```

"projects" almacena todas las cosas necesarias para que funcione el programa.
"skeleton" es el directorio donde se pondrá lo básico del proyecto.
"NAME" debe ser renombrado con el nombre del proyecto, este tiene el módulo principal cuando se usa skeleton.

```bash
$ touch NAME/__init__.py
$ touch tests/__init__.py
$ 
```

```bash
$ touch setup.py
```

setup.py
```python
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
```

Este fichero tiene toda la información de contacto.

Ahora, se quiere crear algunas pruebas en "test/NAME_tests.py".

test/NAME_tests.py
```python
from nose.tools import *
import NAME

def setup():
	print("SETUP!")

def teardown():
	print("TEAR DOWN!")

def test_basic():
	print("I RAN!")
```


## Estructura final del directorio

Se debe tener una estructura igual, puede tener más ficheros, pero esta es la estructura básica de cualquier proyecto.

```
	skeleton/
		NAME/
		__init__.py
	bin/
	docs/
	setup.py
	tests/
		NAME_tests.py
		__init__.py
```

* `bin` es donde se ponen los scripts para que se puedan ejecutar en CLI, no poner módulos acá.

Ejecutar las pruebas que se escribieron, se debe estar en el directorio principal del directorio proyecto.

```bash
$ ls
NAME bin docs setup.py tests
$
$ nosetests
```

## En Resumen

Para crear un nuevo proyecto, este debe tener un directorio para contenerlo, este directorio debe tener lo siguiente:

1) Crear un directorio "skeleton", "bin", "docs", "tests".
2) Dentro de "skeleton" crear directorio "NAME" donde NAME es el nombre del proyecto, el fichero "__init__.py".
3) Dentro de "tests" crear ficheros "NAME_tests.py" donde NAME es el nombre del proyecto, "__init__.py".
4) Realizar pruebas usando "nosetests".
5) Eliminar todos los ficheros `*.pyc`.
6) Comenzar a escribir código.



# 47 - Pruebas automatizadas

Habiendo ejecutado el juego y comprobado que funciona como se espera, ¿se podría escribir código para probar el código del juego?.
Cuando se agregan cosas nuevas, se cambian o se borran, se puede ejecutar pruebas para asegurarse que las cosas todavía funcionan. Las pruebas no caturan bugs, pero acortan el tiempo gastado encontrando bugs y ejecutan el código.

Probar piezas de software es definitivamente tedioso y aburrido, por ello escribir un poco de código que lo haga por ti.


## Escribiendo Pruebas

Tomaremos una parte del código y haremos una prueba simple.
Usando el módulo "nose" podemos crear pruebas, debemos importar el código del juego que deseamos probar.

Por ejemplo:

Game1_tests.py
```python
from nose.tools import *
from game1.game import Room

def test_room():
	gold = Room("GoldRoom",
	"""This room has gold in it you can grab. There's a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
```

Se importa "Room" de "game1" el módulo "game", para realizar las pruebas.
* `assert_equal` comprueba que el resultado de una función o método entrege el mismo resultado del segundo parámetro.


## Guía de Pruebas

1) Pruebas van *tests/* y se nombra con *NOMBRE_tests.py*, de otro caso *nosetests*.
2) Escribir una prueba para cada módulo que creas.
3) Mantener cortos "test cases" (funciones).
4) Mantener limpio y eliminar cualquier código repetitivo que se pueda. Crear funciones que permitan hacer el trabajo si se necesitan pruebas similares.
5) No adaptes tantas pruebas. A veces, lo mejor ante rediseñar es comenza de cero.


\pagebreak


# 48 - Primer Sitio Web

*Flask* es un web framework, un framework es un conjunto de paquetes que hacen facil hacer algo.

```bash
$ pip install flask
```

## Creando un Hello World Web

```bash
$ mkdir webproject
$ cd webproject
$ mkdir bin GAME tests docs templates
$ touch GAME/__init__.py
touch tests/__init__.py
```


Crear fichero "app.py" que contendrá la aplicación web.

app.py
```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	grettings = 'world'
	return render_template("index.html", grettings=grettings)

if __name__ == '__main__':
	app.run()
```


Ejecutar la aplicación

```bash
$ python webproject/app.py
```


Para habilitar depuración de Flask, se debe crear variable de entorno.

```
$ export FLASK_DEBUG=1
```


La depuración activada en localhost es recomendada para encontrar bugs de la aplicación, y extremadamente peligrosa en Internet, cuando se esté usando en Internet se debe desactivar:

```
$ export FLASK_DEBUG=0
```


## Templates

Las planillas deben ser creadas en el directorio "templates" con el nombre respectivo que se esté usando en el fichero "app.py".

templates/index.html
```python
<html>
	<head>
		<title>Gothons Of Planet Percal #25</title>
	</head>
<body>

	{% if greeting %}
		I just wanted to say
		<em style="color: green; font-size: 2em;">{{ greeting }}</em>.
	{% else %}
		<em>Hello</em>, world!
	{% endif %}

	</body>
</html>
```


Usando lenguaje Jinja para las planillas, se pueden usar if, for, para personalizar las planillas.

* En "app.py" se importó "render_template" al inicio.
* "render_template" carga ficheros ".html" del directorio *templates/*.
* Función *index* se encarga de entregar los datos de la dirección '/'.
* *templates/index.html*, tiene el código HTML, lenguaje Jinja2, utilizando {% %} que actúan como piezas ejecutables para if, for, etc. {{ }} para variables.


# Cómo funciona la Web


---

	+------------------+                            +---------------+ 
	|    Tu Buscador   |                            |    Web App    |
	| http://test.com/ |                            |   index.GET   |
	+------------------+                            +---------------+
		   /\                                                 /\
		   ||                                            D)   ||
		   ||   A)           _____________                    \/
		   \/               (             )          +-------------+
		  Network    ---->  (  Internet   )  ------> |  My Server  |
		 Interface          (_____________)          +-------------+
		            B)                       C)


---


1) Cuando ingresas la url http://test.com/ en el buscador, este envía una petición (A) a la interfaz de red del computador.
2) La peticion quiere salir a Internet (B) y entonces el computador remoto (C) donde el servidor acepta la peticion.
3) Una vez aceptado, la aplicación web (D) y el código Python ejecuta el manejador *index.GET*.
4) La respuesta sale del servidor Python (D).
5) El servidor envía la respuesta es envíada a Internet (C).
6) Pasa por la interface de red (B) y llega al navegador (A).
7) Finalmente, el navegador muestra la respuesta.


Términos necesarios para aplicaciones web.

**Navegador**
	Software que toma una dirección, http://example.com, usa esa información para hacer una peticion al servidor de dicha dirección.

**Address**
	URL (Uniform Resource Locator), indica donde el navegado debe ir. Puede ser HTTP (HyperText Transfer Protocol) o FTP (File Transfer Protocol) la dirección buscar.
	
**Connection**
	Cuando el navegador sabe que protocolo usar y que recurso obtener del servidor, crea una conexión. El buscador simplemente pregunta al OS para abrir un puerto, usualmente 80. Entonces el SO envía o recibe bytes sobre la red entre los computadores (cliente-servidor).
	
**Request**
	El navegador está conectado con la dirección que le entregaste, ahora necesita preguntar que recurso se quiere, por ejemplo, ir a la URL /book/.
	Esta petición se envía al servidor, el servidor envía devuelta una respuesta a la petición.
	
**Response**
	Es el HTML, CSS, JavaScript, o imágenes que el servidor envía devuelta al navegador que hizo la consulta.

**Server**
	El servidor es un computador al final de la conexión que sabe como responder la petición del navegador. Muchos servidores envía ficheros, que actualmente es la mayoría del tráfico.



## Creando formulario

Editamos el fichero 'app.py'.

app.py
```python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/hello", methods=['POST', 'GET'])
def index():
	greeting = "Hello World"
	if request.method == "POST":
		name = request.form['name']
		greet = request.form['greet']
		greeting = f"{greet}, {name}"
		return render_template("index.html", greeting=greeting)
	else:
		return render_template("hello_form.html")

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
	app.run()
```


Creamos el formulario

templates/hello_form.html
```python
<html>
	<head>
		<title>Sample Web Form</title>
	</head>
	
	<body>
		<h1>Fill Out This Form</h1>
		<form action="/hello" method="POST">
			A Greeting: <input type="text" name="greet">
			<br/>
			Your Name: <input type="text" name="name">
			<br/>
			<input type="submit">
		</form>
	</body>

</html>
```


"<form action="/hello" method="POST">", le dice al navegador lo siguiente:

1) Recoletar información del usuario usando los campos del formulario.
2) Enviar al servidor usando una petición tipo POST.
3) Eviar a la dirección */hello*, declarada en *action=/hello*.
4) <input> tiene parametro "type" indica el tipo de input y "name" el cual indica el nombre de la variable enviado en POST.


Creando un diseño de planilla

templates/index.html
```python
{% extends "layout.html" %}

{% block content %}
	{% if greetings %}
		I Just wanted to say
		<em style='color: green; font-size: 2em;">{{ greeting }}</em>
	{% else %}
		<em>Hello</em>, World!
	{% endif %}

{% endblock %}
```


templates/hello_form.html
```python
{% extends "layout.html" %}

{% block content %}
	<h1>Fill Out This Form</h1>
	<form action='/hello' method='POST'>
		A Greeting: <input type='text' name='greet'>
		<br />
		Your Name: <input type='text' name='name'>
		<br />
		<input type='submit'>
	</form>
{% endblock %}
```

Plagina principal de la aplicación web, de esta heredarán el diseño las otras páginas que se crearán.

```python
<html>
	<head>
		<title>Gothons From Planet Percal #25</title>
	</head>
	<body>
		{% block content %}
		{% endblock %}
	</body>
</html>
```

## Test the aplicaction

tests/app_tests.py
```python
from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
	rv = web.get('/', follow_redirects=True)
	assert_equal(rv.status_code, 404)
	
	rv = web.get('/hello', follow_redirects=True)
	assert_equal(rv.status_code, 200)
	assert_in(b'Fill Out This Form', rv.data)
	
	data = {'name': 'Zed', 'greet': 'Hola}
	rv = web.post('/hello', follow_redirects=True, data=data)
	assert_in(b'Zed', rv.data)
	assert_in(b'Zed', rv.data)
```


Ejecutar las pruebas

```bash
$ nosetests
```
 
 
 Que se hizo:
 
Flask tiene una API simple para el proceso de peticiones, la información se envía en forma de dicionario.

En terminal se debe escribir.

```bash
$ export PYTHONPATH=$PYTHONPATH:.
```



