# argparse

Analiza opciones CLI, argumentos y sub-comandos.

*argparse* define los argumentos y analiza cómo analizarlos fuera de `sys.argv`. Automáticamente genera mensajes de uso cuando se usa incorrectamente.

```python
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()

print(args.accumulate(args.integers))
```

```bash
$ python prog.py 1 2 3 4 --sum
10

$ python prog.py --help
```

<br>


# `argparse`

1. Crear `argparse`, crea un objeto `ArgumentParser`.

```python
>>> parser = argparse.ArgumentParser(description="blah blah blah")
```

2. Agregar argumentos

```python
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
>>> parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
```

3. Analizar los argumentos.

```python
parser.parse_args()
```

<br>


# ArgumentParser object

```python
class argparse.ArgumentParser(
            prog=None,
            usage=None,
            description=None,
            epilog=None,
            parents=[],
            formatter_class=argparse.HelpFormatter,
            prefix_chars=’-’,
            fromfile_prefix_chars=None,
            argument_default=None,
            conflict_handler=’error’,
            add_help=True,
            allow_abbrev=True,
            exit_on_error=True
        )
```

| argumento | descripción |
|-|-|
| prog | nombre del programa, por defecto `os.path.basename(sys.argv[0])` |
| usage | breve descripción del uso del programa. |
| description | descripcon del programa. |
| epilog | texto para mostrar después de la ayuda. |
| parents | lista de objetos `ArgumentParser` que deben ser incluidos. |
| formatter_class | personaliza salida de ayuda. |
| prefix_chars | establece carácter de argumetnos. |
| fromfile_prefix_chars | grupo de carácteres de los prefijos de ficheros con argumentos adicionales debe ser leidos. |
| argument_default | valor global por defecto |
| conflict_handler | estrategia para resolver conflictos. (general no necesario). |
| add_help | agrega *-h*/*--help*. |
| alow_abbrev | comandos largos pueden ser abreviados. |
| exit_on_error | determina si no existe ArgumentParser, sale con información del error cuando uno ocurra. |


# .add_argument()

```python
ArgumentParser.add_argument(name or flags...[, action ][, nargs ][, const ][, default ][, type ][, choices ][, required ][, help ][, metavar ][, dest ])
```

| argumento | descripción |
|-|-|
| name or flags | lista de opciones, ejemplo: *-f*, *--foo*. |
| action | accion básica que ocurrirá cuando el argumeto coincida. |
| nargs | numero de argumentos cli que deben ser consumidos. |
| const | valor constatnte requerido por alguna accion y seleccion nargs. |
| default | valor producido si el argumento se ausenta desde cli y si este se ausenta desde el objeto. |
| type | tipo del argumento. |
| choices | serie de valores permitidos para un argumento. |
| required | argumento requerido. |
| help | mensaje de ayuda del programa. |
| metavar | nombre para el argumento en mensaje de uso. |
| dest | nombre del atributo para ser agregado al objeto `parse_args()`. |

* action
    * 'store' : default, almacena el nombre de la variable y el valor.
    * 'store_const' : almacena el valor 'const'.
    * 'store_true'|'store_false' : almacena valores True o False.
    * 'append' : almacena una lista de cada valor de argumento.
    * 'append_const' : almacena en una lista y agrega los valores 'const'.
    * 'count' : cuenta los cantidad de veces que ocurre un argumento.
    * 'help' : mensaje de ayuda.
    * 'version' : imprime la versión del programa.
    * 'extend' : almacena una lista y extiende con cada valor de argumento a la lista.


# Ejemplo

```python
    parser = argparse.ArgumentParser(
                        prog='update_mods_cli.py',
                        description='Actualiza mods a la versión especificada.',
                        epilog='Ayuda en el proceso tedioso de actualizar varios mods.'
                    )
    parser.add_argument(
            '-f',
            '--filename',
            type=str,
            help='txt con lista de todos los mods',
        )
    parser.add_argument(
            '-m',
            '--mod',
            type=str,
            help='nombre del fichero del mod'
        )
    parser.add_argument(
            '-g',
            '--gameVersion',
            type=str,
            help='versión del juego'
        )
    parser.add_argument(
            '-k',
            '--key',
            type=str,
            help='key API',
            required=True
        )

    args = parser.parse_args()

    filename = args.filename
    mod = args.mod
    gameVersion = args.gameVersion
    apiKey = f'{args.key}'

    if apiKey == "":
        parser.print_help()
    else:
        if filename is not None or mod is not None and gameVersion is not None:
            reg = re.search(r'^1\.([0-9]{,2}.+)?', gameVersion)
            if reg is None:
                print()
                print("Ingrese una versión correcta")
                print("https://minecraft.fandom.com/wiki/Java_Edition_version_history")
                print()
            else:
                if filename is not None:
                    auto = AutoUpdate(key=apiKey, version=gameVersion)
                    auto.load_txt(filename)
                    tr1 = threading.Thread(target=auto.download)
                    tr1.start()
                elif mod is not None:
                    auto = AutoUpdate(key=apiKey, version=gameVersion)
                    auto.search(mod)
        else:
            parser.print_help()

```
