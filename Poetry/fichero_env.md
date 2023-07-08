# Fichero `.env`

Fichero `.env` es un fichero de entorno en el que se puede almacenar y administrar todas las variables  de entorno de una aplicación.

Simplemente se crea el fichero en el mismo directorio donde está `manage.py`

Este **se debe agregar a <i>.gitignore<i>** para evitar compartir la información sensible que tenga.


# python-decouple

> [python-decouple - pip](https://pypi.org/project/python-decouple/)

Django tiene varios paquetes que permiten obtener las variables de los ficheros `.env`, *python-decouple* permite realiza esto.

<br>

## Instalar

```bash
pip install python-decouple
```

<br>

## Fichero `.env`

Formato variables fichero `.env`

```
#Comentario

KEY=value
```

Este fichero debe estar en el mismo directorio en donde el fichero que usará estas variables.

<br>

## Obtener variables

```python
from decouple import config


DEBUG = config(‘KEY’, cast=str)
```

*python-decouple* permite convertir los tipos de datos de las variables a los tipos correctos, por ejemplo, una variable debe ser un booleano, este lo hace mediante el parámetro `cast=tipo_dato`.


