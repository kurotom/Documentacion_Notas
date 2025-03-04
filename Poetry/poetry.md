# Poetry

Herramienta para administrar dependencias y paquetes en Python, permite instalar, actualizar, eliminar paquetes en un entorno aislado del sistema.

> Requiere Python 3.5+


## Instalar *poetry*.

```
$ pip install poetry
```

---

En Linux, ubicación entornos virtuales **`/home/[USERNAME]/.cache/pypoetry/virtualenvs/`**.

---

## Actualizar poetry.

```
$ poetry self update
```

<br>

# Uso Básico

# Crear un nuevo proyecto

```
$ poetry new [proyecto_name]
```

# Usar poetry en un proyecto existente.

```
$ cd [projecto_existente]
$ poetry init
```


# Instalar dependencias.

```
$ poetry add "paquete^version.number"


$ poetry add "paquete"
```

---

# Poetry Export

> [poetry-plugin-export](https://github.com/python-poetry/poetry-plugin-export)

Poetry 2.0+, necesita instalar un plugin para exportar ficheros "lock" en varios formatos.

* **poetry self**
```
poetry self add poetry-plugin-export
```

* **pipx**

```
pipx inject poetry poetry-plugin-export
```

* **pip**
```
pip install poetry-plugin-export
```

## Uso

```
$ poetry export --without-hashes --format=requirements.txt --output requirements.txt
```

# Poetry Shell

Permite ctivar entornos virutales en una subshell, en versiones **Poetry 2.0+** se debe instalar plugin [poetry-plugin-shell](https://github.com/python-poetry/poetry-plugin-shell).

```bash
$ poetry self add poetry-plugin-shell
```

## Uso

Activar la shell virutal y salir.

```
$ poetry shell

$ exit
```

Opcionalmente se puede usar `deactive` o combinacion de teclas `Control + D`.

---

<br>

# Instalar dependencias.

Fichero *poetry.lock*, permite replicar el entorno en otras máquinas, mantienen la información de los paquetes usados.

```
$ poetry install
```

Se generará a usar el comando anterior, **poetry.lock se debe incoporar al seguimiento GIT.**

Si no está el fichero se utilizará el fichero *pyproject.toml* y descarga la última versión del fichero.


# Comandos

Comandos línea de comando utilizando la interfaz, comando ayuda `$ poetry --help`.

## Globales

* `--verbose | -v|vv|vvv`: incrementa mensajes, "-v" normal, "-vv" más verboso, "-vvv" debug.
* `--help | -h`: help.
* `--quiet | -q`: no mostrar mensajes.
* `--ansi`: salida ANSI.
* `--no-ansi`: deshabilitar ANSI.
* `--version | -V`: version.

## new

`$ poetry new nuevo_paquete`: crea una estructura nueva.

`$ poetry new my-folder --name nuevo_paquete`

`$ poetry new --src paquete_existente`


## init

`$ poetry init`: crea un proyecto `pyproject.toml` interactivamente para proveer información básica sobre el paquete, en un directorio de projecto existente.

Opciones:
* --name: nombre de paquete.
* --description: descripción del paquete.
* --author: author del paquete.
* --python: versión python compatible.
* --dependency: versión paquete que requiere, `foo:1.0.0`.
* --dev-dependency: requisitos de desarrollo.


## install

`$ poetry install`: lee el fichero `pyproject.toml` desde el proyecto actual y los instala.

`$ poetry install --remove-untracked`: elimina dependencias viejas presentes en el fichero lock.

`$ poetry install --extras "paquete1 paquete2"`: especifica paquetes extras para ser instalados.

`$ poetry install --no-root`: saltarse la instalación.


## update

`$ poetry update`: obtiene las últimas versiones de dependencias del fichero `poetry.lock`.

`$ poetry update paquete1 paquete2`: obtiene las útlimas versiones de los paquetes entregados.


## add

`$ poetry add "paquete>=version"`: agrega paquetes requeridos en `pyproject.toml` y los instala.

`$ poetry add "paquete@^version"`

`$ poetry add git+https://github.com/sdispater/pendulum.git`
`$ poetry add git+ssh://git@github.com/sdispater/pendulum.git`
`$ poetry add git+https://github.com/sdispater/pendulum.git#2.0.5`


## remove

`$ poetry remove "paquete@^version"`: elimina paquete de la lista de paquetes instalados.


## show

`$ poetry show`: muestra todos los paquetes disponibles.
`$ poetry show paquete`


## build

`$ poetry build`: comando construye la fuente y archivos wheels.


## config

`$ poetry config [opciones] []`

`$ poetry config --list`: muestra todas las configuraciones y repositorios.



## run

`$ poetry run [comando]`: ejecuta un comando dentro del entorno virtual.

`$ poetry run python manage.py runserver`


## shell

`$ poetry shell`: ejecuta dentro del entorno virtual.


## check

`$ poetry check`: valida estructura del fichero *pyproject.toml* y retorna un reporte detallado de cualquier error.


## search

`$ poetry search [paquete]`: busca paquete en un índice remoto.


## lock

`$ poetry lock`: bloquea dependencias especificadas en *pyproject.toml*.
`$ poetry lock --no-update`: no actualiza dependencias bloquedas.



# Administrar entornos

Permite tener control explícito sobre el entorno, usando el comando `env use` podemos especificar que versión Python usar.

```
$ poetry env use PYTHON.VERSION
```

Si da error, se tiene que editar fichero *pyproject.toml*.


## Mostrar informacion

```
$ poetry env info
```


## Lista entornos

```
$ poetry env list
```


## Borrar entornos

```
$ poetry env remove /full/path/to/python
$ poetry env remove python3.7
$ poetry env remove test-environment-version

$ poetry env remove --all
```

## Ejecutar comando

Se puede ejecutar comandos python dentro del entorno sin entrar en el.

```
$ poetry run python name_script.py

$ poetry run pytest
```

<br>

# pyproject.toml

Documentación - [https://python-poetry.org/docs/pyproject/](https://python-poetry.org/docs/pyproject/)

Fichero **pyproject.toml** orquesta el proyecto y las dependencias.

Un ejemplo:

```
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## name

Nombre del paquete

```
name = "my-package" 
```

## version

Versión del paquete

```
version = "0.1.0"
```

## description

Descripción del paquete

```
description = "short string"
```

## license

Licencia del proyecto

* Apache-2.0
* BSD-2-Clause
* BSD-3-Clause
* BSD-4-Clause
* GPL-2.0-only
* GPL-2.0-or-later
* GPL-3.0-only
* GPL-3.0-or-later
* LGPL-2.1-only
* LGPL-2.1-or-later
* LGPL-3.0-only
* LGPL-3.0-or-later
* MIT

```
license = "MIT"
```

## authors

Autores del paquete

```
authors = [
    "Sébastien Eustace <sebastien@eustace.io>",
]
```

## maintainers

Mantenedores del paquete

```
maintainers = [
    "John Smith <johnsmith@example.org>",
    "Jane Smith <janesmith@example.org>",
]
```

## readme

Ruta del fichero README.md

```
[tool.poetry]
# ...
readme = "README.md"
```

## homepage

Pagina del proyecto.

```
homepage = "url"
```

## repository

Url repositorio del proyecto.

```
repository = "https://github.com/python-poetry/poetry"
```

## documentation

Documentación del proyecto.

```
documentation = "https://python-poetry.org/docs/"
```


## keywords

Palabras relacionadas con el paquete.

```
keywords = ["packaging", "poetry"]
```

## classifiers

Lista de clasificadores PyPi que describe al proyecto.

```
[tool.poetry]
# ...
classifiers = [
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules"
]
```


Se establecen automáticamente al usar *license*.


## packages

Lista de paquetes y módulos para incluir en la distribución final del paquete.

```
[tool.poetry]
# ...
packages = [
    { include = "my_package" },
    { include = "extra_package/**/*.py" },
]
```

Si el paquete es almacenado en directorio *lib*, se debe especificar.

```
[tool.poetry]
# ...
packages = [
    { include = "my_package", from = "lib" },
]
```

## include y exclude

Lista de patrones que se incluyen en el paquete final.

```
[tool.poetry]
# ...
include = ["CHANGELOG.md"]

exclude = ["my_package/excluded.py"]
```


## dependencies y dependency groups

Poetry está configurado para mirar dependencias en PyPi por defecto, el nombre y la versión.

```
[tool.poetry.dependencies]
requests = "^2.13.0"
```

Usando un repositorio privado.

```
[[tool.poetry.source]]
name = "private"
url = "http://example.com/simple"
```

Especificar paquetes.

```
[tool.poetry.dependencies]
requests = { version = "^2.13.0", source = "private" }
```

Agrupar dependencias para hacer más granular las dependencias.

```
[tool.poetry.group.test.dependencies]
pytest = "*"

[tool.poetry.group.docs.dependencies]
mkdocs = "*"
```

## scripts

Describe los scripts y ejecutables que serán instalados cuando se instale el paquete. Además, permite apuntar a un método para ejecutar un fichero Python como comando en terminal.

```
[tool.poetry.scripts]
my_package_cli = 'my_package.console:run'
```

* Script a instalar: *my_package*
* Ejecutará la función la función *run* de la función *console* del paquete *my_package*.

Se puede especificar un script que depende en un extra.

```
[tool.poetry.scripts]
devtest = { callable = "mypackage:test.run_tests", extras = ["test"] }
```

## extras

Poetry soporta extras para permitir expresiones de:

* dependencias opcional, el cual mejora un paquete, pero no requerido.
* cluster de dependencias opcionales.

```
[tool.poetry]
name = "awesome"

[tool.poetry.dependencies]
# These packages are mandatory and form the core of this package’s distribution.
mandatory = "^1.0"

# A list of all of the optional dependencies, some of which are included in the
# below `extras`. They can be opted into by apps.
psycopg2 = { version = "^2.9", optional = true }
mysqlclient = { version = "^1.3", optional = true }

[tool.poetry.extras]
mysql = ["mysqlclient"]
pgsql = ["psycopg2"]
databases = ["mysqlclient", "psycopg2"]
```

Para instalar los paquetes extras.

```
poetry install --extras "mysql pgsql"
poetry install -E mysql -E pgsql
```


Los extras no especificados se eliminarán. Instalarán todos los extras.

```
poetry install --al-extras
```


## urls

Se puede espicificar ulr en la sección.
Adicionalmente `homepage`, `repository` y `documentation`.

```
[tool.poetry.urls]
"Bug Tracker" = "https://github.com/python-poetry/poetry/issues"
```

<br>

# Versionamiento

Poetry usa versionamiento [PEP 440](https://peps.python.org/pep-0440), no es obligatorio, pero sí recomendado.

```
1.0.0-post1
1.0.0.post1
```

<br>

# Empaquetado

Para publicar un proyecto se necesita empaquetarlo primero.

```
poetry build
```

Tiene dos formatos:

* *wheel*
* *compiled*

<br>

# Publicar

Por defecto *Poetry* publica en [**PyPi**](https://pypi.org/).

Cualquier paquete publicado en *PyPi* esta disponible en *Poetry*.

```
poetry publish
```

Usando `--build` se empaqueta y publica.

Para un repositorio privado.

```
poetry publish -r reppositorio_privado
```


