# Django on Render

[Documentación django on render](https://render.com/docs/deploy-django#create-a-django-project)

En el proyecto se debe utilizar con [Poetry](https://python-poetry.org/) para administrar el entorno virtual.

Se necesita modificar el código base del proyecto para poder desplegar en [render.com](https://render.com).

Render tiene compatibilidad con Python 3.7.


* [Poetry](poetry.md)


Pasos:

1. Instalar "poetry".

```
$ pip install poetry
```


2. Crear estructura proyecto.

```
$ poetry new nombre_proyecto
```

Projecto existente, ir al directorio.
```
$ poetry init
```


3. Establecer versión Python.

```
$ poetry env use pythonX.X
```


4. Agregar dependencias.

```
$ poetry add paqueteX
```


5. Crear proyecto.

```
$ poetry run django-admin startproject nombre_proyecto .
```


6. Crear aplicaciones.

```
$ python manage.py nombre_app .
```

7. Enviar el proyecto al repositorio.

8. Conectar Render.com al repositorio Github desde la web.

9. Agregar fichero `.build.sh`, ejecutable para todos, contiene comandos bash:
```
python manage.py migrate
python manage.py makemigrate
python manage.py collectstatic --noinput
```

10. Configurar parámetros del servicio web, agregar en la sección comandos './build.sh', 'gunicorn aplicacion.wsgi'.

11. Agregar variables de entorno, si las tiene.

12. Esperar que la construcción termine.



## Declarando servicio dentro del repositorio.

Utilizando fichero *render.yaml*, en la raíz del directorio, los cambios se enviarán al repositorio, render.com automáticamente detectará el fichero y realizará las configuraciones correspondientes.

```YAML
databases:
  - name: mysite
    databaseName: mysite
    user: mysite

services:
  - type: web
    name: mysite
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn mysite.wsgi:application"
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: mysite
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: WEB_CONCURRENCY
        value: 4
```


## Manualmente

1. Crear base de datos [PostgreSQL en Render](https://render.com/docs/databases), utilizar la dirección **internal database URL**.

2. Crear un nuevo **Web Service** apuntando al repositorio (entregando los permisos correspondientes).

3. Seleccionar entorno Python.

4. Agregar fichero `.build.sh`, ejecutable para todos, contiene comandos bash:
```
python manage.py migrate
python manage.py makemigrate
python manage.py collectstatic --noinput
```

5. Comando inicio del servicio: `gunicorn mysite.wsgi`.

6. Agregar variables de entorno en Render.com.

7. Desplegar y esperar que termine.

