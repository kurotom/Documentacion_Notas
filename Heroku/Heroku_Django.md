# Configurar Django App para Heroku

Heroku requiere de ficheros `Procfile`, `runtime.txt`, `requirements.txt`, este fichero declara explícitamente tipo de procesos de la aplicación será usado y los puntos de entrada, está ubicado en al carpeta raíz del proyecto.

Se debe tener en cuenta que Heroku opera con `stacks` de software, es decir, la version del lenguaje a usar, a continuación dejo enlaces con la información:

- [stack-support-details](https://devcenter.heroku.com/articles/stack#stack-support-details)

- [supported-runtimes](https://devcenter.heroku.com/articles/python-support#supported-runtimes)


Por ejemplo, si la aplicación usa Python 3.9.9, el fichero runtime debe contener `python-3.9.9`, de lo contrario, se pueden generar errores de compatibilidad.


## Procfile

  `web: gunicorn proyecto.wsgi`


Procfile requiere Gunicorn, el servidor web de producción que se recomienda para aplicaciones Django.

## runtime.txt

Se puede definir que versión de Python se ejecuta en la aplicación, se necesita el fichero `runtime.txt`.

```
  #  cat runtime.txt
  python-3.9.9
```


### Instalar gunicorn

  `pip install gunicorn`

Recordar poner "gunicorn" dentro del fichero "requirements.txt".


## settings.py

Heroku, almacena información sensible en [entornos de variables](https://devcenter.heroku.com/articles/config-vars), que tradicionalmente está configurado en aplicaciones Django.

El paquete [`django-on-heroku`](https://github.com/pkrefta/django-on-heroku) configura automáticamente la aplicación Django para que funcione en Heroku, es compatible con aplicaciones Django 2.0 y Python 3.
Permitiendo leer `DATABASE_URL`, configuracion de registro, un [Heroku CI](https://devcenter.heroku.com/articles/heroku-ci) compatible con `TestRunner`, y configurar automáticamente 'staticfiles' para que funcione.


### Instalar django-on-heroku

  `pip install django-on-heroku`

Recordar poner "gunicorn" dentro del fichero "requirements.txt".


En el fichero `settings.py` del proyecto, importar y configurar.

```
  import django_on_heroku

  [...]

  # Activar django-on-heroku
  django_on_heroku.settings(locals())
```


# Django y ficheros estáticos

Puede ser un poco dificultoso configurar y depurar opciones para elementos estáticos, sin embargo, si se agregan las siguientes lineas en `settings.py`, todo funcionará como se espera.

*settings.py*
```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

Django no crea automáticamente el directorio objeto `STATIC_ROOT` que usa `collectstatic` si esté no está disponible. Debes crear este directorio en la raíz, y estará disponible cuando `collectstatic` sea ejecutado.
Git no soporta directorios vacíos, puedes crear un fichero vacío dentro de el para solucionar el problema.


## Whitenoise

Django no soporta servir ficheros estaticos en producción. Existe el proyecto WhiteNoise (muchas gracias!) que se puede integarar a tu aplicación Django.

[WhiteNoise documentación](http://whitenoise.evans.io/en/stable/)


### Instalar WhiteNoise

  `pip install whitenoise`

Recordar poner "gunicorn" dentro del fichero "requirements.txt".


Editar, fichero `settings.py`, agregar en la sección middleware al principio de la tupla.

```
MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
)
```

Si quieres habilitar la funcionalidad gzip, agregar en `settings.py`.


```
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Ahora tu aplicación sirve elementos estáticos directamente desde Gunicorn en producción. Esto es perfectamente adecuado para muchas aplicaciones, pero aplicaciones mucho más complejas pueden requerir usar CDN con [Django-Storages](http://django-storages.readthedocs.org/en/latest/).


## Generando requirements.txt

  ` # pip freeze > requirements. txt`

Con ello generamos el archivo con los modulos necesarios para la aplicación y Heroku.



## Collectstatic durante la construcción

Cuando una aplicación Django es desplegada en Heroku, el comando `$ python manage.py collectstatic --noinput` se ejecuta automáticamente durante la construcción, una construcción fallida si la etapa collectstatic no es exitosa.

## Debugging

Si collectstatic falla durante la construcción, un mensaje de seguimiento se entrega para ayudar a diagnosticar el problema. Si se necesita información adicional sobre el entorno collectstatic que se ejecutó, usar:

  `$  heroku config:set DEBUG_COLLECTSTATIC=1`

Esto muestra la salida de la construcción de todas las variables de entorno disponibles para Python cuando collectstatic fué ejecutado.


A veces, es posible que no desee que Heroku ejecute collectstatic, para deshabilitar simplemente se utiliza:

  `$  heroku config:set DISABLE_COLLECTSTATIC=1`

Con esto deshabilitas el paso collectstatic de la construcción.
