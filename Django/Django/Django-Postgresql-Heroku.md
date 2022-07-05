
# Django - Postgres - Heroku

App Django desplegada en Heroku, este último usa por defecto la base de datos Postgres, este documento explica cómo cambiar de SQLite a Postgres.

**Realizar respaldo para evitar perdidas de datos, sea sensato.**


# Instalar paquetes necesarios.

  ```bash

  sudo dnf install python3-devel libpq-devel

  pip install django django-on-heroku psycopg2 whitenoise gunicorn
  ```


# Django

  [**Django-PostgreSQL**](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes)



  Fichero `settings.py` del proyecto base.

```
	import psycopg2

	[...]

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.getenv("DBname"),
            'USER': os.getenv("userDB"),
            'PASSWORD': os.getenv("pwdUserDB"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
		}
	}
```


### Generando las configuración de entorno para la base de datos.


export DBname="name_DB"
export userDB="username_DB"
export pwdUserDB="passwdUser"
export DB_HOST="localhost"
export DB_PORT="5432"



# PostgreSQL

### Ficheros de configuración

Ficheros principales de configuración de servidor postgresql.

  * `/var/lib/pgsql/data/postgresql.conf`

  * `/var/lib/pgsql/data/pg_hba.conf`



### Instalacion de software

  ` # sudo dnf install postgresql-server postgresql-contrib`



### Habilitar y preparar para primer inicio del servicio

  ` # sudo systemctl enable postgresql`


  ` # sudo systemctl start postgresql`


  Posiblemente se genere un error al iniciar por primera vez el servicio, revisar con:

  ` # journalctl -xn`


  El error se debe a que no existen los ficheros de configuración `postgresql.conf` y `pg_hba.conf`, para generarlos:

  ` # sudo postgresql-setup --initdb --unit postgresql`



### Configurar `firewall-cmd`.

  Recordar agregar la zona que usará el servicio postgresql, en este caso usará la por defecto.

  ` # sudo firewall-cmd --permanent --add-port=5432/tcp`

  ` # sudo firewall-cmd --reload`


# Ficheros del servicio posgresql

## Modificar fichero postgresql.conf

Para que acepte conexiones desde la red, se debe cambiar:


` # vim /var/lib/pgsql/data/postgresql.conf`


      listen_addresses = 'localhost'

          cambiarlo a

      listen_addresses = '*'



Para poder mejorar la seguridad cambiar la configuración de md5 a scram-sha-256 en `postgresql.conf`.

      password_encryption = scram-sha-256



Configurar el acceso al servidor de base de datos, agregando o modificando las reglas.

[Documentación **pg_hba.conf**](https://www.postgresql.org/docs/9.6/auth-pg-hba-conf.html)

` # vim /var/lib/pgsql/data/pg_hba.conf`


    # TYPE    DATABASE        USER            ADDRESS                 METHOD
      host    all             all             127.0.0.1/32            scram-sha-256
      host    all             all             ::1/128                 scram-sha-256
      local   all             postgres                                peer


Valores para campo `TYPE`:
* local — Unix-domain socket.
* host — plain or SSL-encrypted TCP/IP socket.
* hostssl — is an SSL-encrypted TCP/IP socket.
* hostnossl — plain TCP/IP socket.


Valores para campo `METHOD`:
* md5 — client has to supply password processed with MD5 algorithm.
* ident — obtain user name of connecting client from operating system and consult it with specified map.
* trust — anyone who is able to connect to PostgreSQL server may act as any user without supplying password.
* peer — obtains user's name from operating system and checks if it matches database user name.
* scram-sha-256 - change the authentication method specifications.


***

#### Advertencia

La siguiente configuración es totalmente insegura, y solo se debe usar para conexiones localhost.

```
    # TYPE    DATABASE        USER            ADDRESS                 METHOD
      host    all             all             127.0.0.1/32            trust
```

***

- [**Fedora-PostgreSQL - Source**](https://fedoraproject.org/wiki/PostgreSQL#link-pghba)


## Reiniciar el servicio postgresql

`sudo systemctl restart postgresql.service`

## Recargar postgresql data
Es la carpeta que contiene la información de postgresql, en el directorio home del usuario que `postgres`, en este caso es el usuario root de postgresql.

`# pg_ctl reload -D data/`

<br>

## Creacion de usuario y usuario de Base de Datos

Cambiar de usuario, usuario root.

  ` # su - postgres`


Ingresar a Postgresql.

  ` $ psql`



Cambiar contraseña de usuario "postgres".

`postgres=# \password postgres`



### Creacion de Base de Datos

`CREATE DATABASE appdatabase;`


### Creacion de usuario de la base de datos y contraseña
Copiar y pegar el hash generado.

` CREATE USER usuariodatabase WITH PASSWORD 'password';`



### Optimizacion de base de datos Postgresql para Django

```
ALTER ROLE usuariodatabase SET client_encoding TO 'utf8';
ALTER ROLE usuariodatabase SET default_transaction_isolation TO 'read committed';
ALTER ROLE usuariodatabase SET timezone TO 'UTC';
```


###  Dar privilegios a la base de datos.

Dependiendo de los requisitos se deben aplicar los privilegios necesarios, para fines explicativos se utilizará el siguiente ejemplo:

`GRANT ALL PRIVILEGES ON DATABASE appdatabase TO usuariodatabase;`



### Salir de la Postgresql y del entorno de usuario "postgres"

` \q`

` # exit`


<br>

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

<br>

# Django


## Crear la migración y migrar de la aplicación y los archivos estáticos.

  ` # python manage.py check`

  ` # python manage.py collectstatic`


  ` # python manage.py makemigrations`


  ` # python manage.py migrate`


  ` # python manage.py createsuperuser`




##  Iniciar el servidor, ;)

  ` # python manage.py runserver 0.0.0.0:8000`


<br>

Si todo está correcto, ahora tenemos una aplicación en Heroku y con acceso desde cualquier parte.
