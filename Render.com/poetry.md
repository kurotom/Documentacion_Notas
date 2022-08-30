## Poetry

Herramienta para administrar dependencias y paquetes en Python, permite instalar, actualizar.

Requiere Python 3.5+


Instalar *poetry*.
```
$ pip install poetry
```


Actualizar poetry.
```
$ poetry self update
```

Generar requirements.txt.
```
$ poetry export --without-hashes --format=requirements.txt --output requirements.txt
```

### Uso Básico

Crear un nuevo proyecto
```
$ poetry new [proyecto_name]
```

Usar poetry en un proyecto existente.
```
$ cd [projecto_existente]
$ poetry init
```


Instalar dependencias.
```
$ poetry add "paquete^version.number"
```


Utilizar shell poetry y salir entorno virtual.
```
$ poetry shell

$ deactive
```


Instalar dependencias, utilizando fichero *poetry.lock*.
```
$ poetry install
```

Si no está el fichero se utilizará el fichero *pyproject.toml* y descarga la última versión del fichero.


### Comandos

Comandos línea de comando utilizando la interfaz, comando ayuda `$ poetry --help`.

#### Globales

* `--verbose | -v|vv|vvv`: incrementa mensajes, "-v" normal, "-vv" más verboso, "-vvv" debug.
* `--help | -h`: help.
* `--quiet | -q`: no mostrar mensajes.
* `--ansi`: salida ANSI.
* `--no-ansi`: deshabilitar ANSI.
* `--version | -V`: version.

#### new

`$ poetry new nuevo_paquete`: crea una estructura nueva.

`$ poetry new my-folder --name nuevo_paquete`

`$ poetry new --src paquete_existente`


#### init

`$ poetry init`: crea un proyecto `pyproject.toml` interactivamente para proveer información básica sobre el paquete, en un directorio de projecto existente.

Opciones:
* --name: nombre de paquete.
* --description: descripción del paquete.
* --author: author del paquete.
* --python: versión python compatible.
* --dependency: versión paquete que requiere, `foo:1.0.0`.
* --dev-dependency: requisitos de desarrollo.


#### install

`$ poetry install`: lee el fichero `pyproject.toml` desde el proyecto actual y los instala.

`$ poetry install --remove-untracked`: elimina dependencias viejas presentes en el fichero lock.

`$ poetry install --extras "paquete1 paquete2"`: especifica paquetes extras para ser instalados.

`$ poetry install --no-root`: saltarse la instalación.


#### update

`$ poetry update`: obtiene las últimas versiones de dependencias del fichero `poetry.lock`.

`$ poetry update paquete1 paquete2`: obtiene las útlimas versiones de los paquetes entregados.


#### add

`$ poetry add "paquete>=version"`: agrega paquetes requeridos en `pyproject.toml` y los instala.

`$ poetry add "paquete@^version"`

`$ poetry add git+https://github.com/sdispater/pendulum.git`
`$ poetry add git+ssh://git@github.com/sdispater/pendulum.git`
`$ poetry add git+https://github.com/sdispater/pendulum.git#2.0.5`


#### remove

`$ poetry remove "paquete@^version"`: elimina paquete de la lista de paquetes instalados.


#### show

`$ poetry show`: muestra todos los paquetes disponibles.
`$ poetry show paquete`


#### build

`$ poetry build`: comando construye la fuente y archivos wheels.


#### config

`$ poetry config [opciones] []`

`$ poetry config --list`: muestra todas las configuraciones y repositorios.



#### run

`$ poetry run [comando]`: ejecuta un comando dentro del entorno virtual.

`$ poetry run python manage.py runserver`


#### shell

`$ poetry shell`: ejecuta dentro del entorno virtual.


#### check

`$ poetry check`: valida estructura del fichero *pyproject.toml* y retorna un reporte detallado de cualquier error.


#### search

`$ poetry search [paquete]`: busca paquete en un índice remoto.


#### lock

`$ poetry lock`: bloquea dependencias especificadas en *pyproject.toml*.
`$ poetry lock --no-update`: no actualiza dependencias bloquedas.



### Administrar entornos

Permite tener control explícito sobre el entorno, usando el comando `env use` podemos especificar que versión Python usar.

```
$ poetry env use python3.7
```


#### Mostrar informacion

```
$ poetry env info
```


#### Lista entornos

```
$ poetry env list
```


#### Borrar entornos

```
$ poetry env remove /full/path/to/python
$ poetry env remove python3.7
$ poetry env remove test-environment-version
```


### pyproject.toml

Documentación - [https://python-poetry.org/docs/pyproject/](https://python-poetry.org/docs/pyproject/)
