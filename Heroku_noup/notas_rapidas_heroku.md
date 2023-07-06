# Heroku

Preparando la aplicacion para desplegarla en Heroku, agregaremos opciones en el fichero `settings.py` del proyecto Django, crearemos directorio `staticfiles`.


  ` # vim proyecto/settings.py`

        import django_on_heroku

        [...]

        # SECURITY WARNING: don't run with debug turned on in production!
        DEBUG = False

        ALLOWED_HOSTS = ['*']


        MIDDLEWARE = [
            [...]
            'whitenoise.middleware.WhiteNoiseMiddleware',
        ]

        [...]

        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

        [...]

        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        # Activate django-on-heroku.
        django_on_heroku.settings(locals())

        [...]



El fichero "runtime.txt" guarda la version de Python que se ejecutará.

```
  # cat runtime.txt
    python-3.10
```



El fichero "requirements.txt" guarda los paquetes python que se usará en la aplicacion.

```
  # cat requirements.txt
    django
    gunicorn
    django-on-heroku
    whitenoise
    psycopg2
```


El fichero declara explicitamente que comandos se deben ejecutar al inicio de la aplicacion.

```
  # cat Procfile
    web: gunicorn project4.wsgi
```


Crear una cuenta en [*Heroku*](Heroku.com), con la cuentas free sin verificar podemos tener hasta 5 aplicaciones desplegadas.

Creamos una nueva aplicación en Heroku, se le da el nombre al proyecto y se elige la región disponible.


Descargar e instalar Heroku CLI, si ya se tiene instalado, ingresar el siguiente comando para crear una llave SSH publica.

  ` # heroku login`


Clonar el repositorio creado, usando Git, por ejemplo:

  `# heroku git:clone -a repositorio_proyectoHeroku`


Cambiarse al directorio del repositorio.

  ` # cd repositorio_proyectoHeroku`


Desplegar los cambios hechos localmente a la "nube" Heroku.

` # git add .`

` # git commit -am "comentario de cambios"`

` # git push heroku master`


Revisar los logs para ver si todo está funcionando.

  ` # heroku logs`

