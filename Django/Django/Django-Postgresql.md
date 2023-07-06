# Django - Postgres 

Django por defecto usa SQLite, pero se puede usar otras como MySQL, MariaDB, PostgreSQL, Oracle.

Este documento explica cómo cambiar de SQLite a Postgres.

**Realizar respaldo para evitar perdidas de datos, sea sensato.**

---

Entorno Linux RPM.

---

# Instalar paquetes necesarios.

```bash

sudo dnf install python3-devel libpq-devel

pip install django psycopg2 whitenoise gunicorn
```


# Django

  [**Django-PostgreSQL**](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes)

Fichero `settings.py` del proyecto base.

```python
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

## Variables de entorno

```bash
export DBname="name_DB"
export userDB="username_DB"
export pwdUserDB="passwdUser"
export DB_HOST="localhost"
export DB_PORT=5432
```

<br>

# PostgreSQL

Los principales ficheros de configuración son:

  * `/var/lib/pgsql/data/postgresql.conf`

  * `/var/lib/pgsql/data/pg_hba.conf`

## Instalacion de software

```bash
# sudo dnf install postgresql-server postgresql-contrib
```

## Habilitar y preparar para primer inicio del servicio

```bash
# sudo systemctl enable postgresql
```

```bash
# sudo systemctl start postgresql
```

Posiblemente se genere un error al iniciar por primera vez el servicio, revisar con:

```bash
# journalctl -xn
```

El error se debe a que no existen los ficheros de configuración `postgresql.conf` y `pg_hba.conf`, para generarlos:

```bash
# sudo postgresql-setup --initdb --unit postgresql
```

## Configurar `firewall-cmd`.

Recordar agregar la zona que usará el servicio postgresql, en este caso usará la por defecto.

```bash
# sudo firewall-cmd --permanent --add-port=5432/tcp
```

```bash
# sudo firewall-cmd --reload
```


# Ficheros del servicio posgresql


## Modificar fichero postgresql.conf

Para que acepte conexiones desde la red, se debe cambiar:

```bash
# vim /var/lib/pgsql/data/postgresql.conf
```

`listen_addresses = 'localhost'` cambiarlo a **`listen_addresses = '*'`**.

Para poder mejorar la seguridad cambiar la configuración de md5 a scram-sha-256 en `postgresql.conf`.

`password_encryption = scram-sha-256`

Configurar el acceso al servidor de base de datos, agregando o modificando las reglas.

[Documentación **pg_hba.conf**](https://www.postgresql.org/docs/9.6/auth-pg-hba-conf.html)

```bash
# vim /var/lib/pgsql/data/pg_hba.conf
```

```
    # TYPE    DATABASE        USER            ADDRESS                 METHOD
      host    all             all             127.0.0.1/32            scram-sha-256
      host    all             all             ::1/128                 scram-sha-256
      local   all             postgres                                peer
```

Valores para campo `TYPE`:
* `local` — Unix-domain socket.
* `host` — plain or SSL-encrypted TCP/IP socket.
* `hostssl` — is an SSL-encrypted TCP/IP socket.
* `hostnossl` — plain TCP/IP socket.

Valores para campo `METHOD`:
* `md5` — client has to supply password processed with MD5 algorithm.
* `ident` — obtain user name of connecting client from operating system and consult it with specified map.
* `trust` — anyone who is able to connect to PostgreSQL server may act as any user without supplying password.
* `peer` — obtains user's name from operating system and checks if it matches database user name.
* `scram-sha-256` - change the authentication method specifications.


## Advertencia

La siguiente configuración es totalmente insegura, y solo se debe usar para conexiones **localhost**.

```
    # TYPE    DATABASE        USER            ADDRESS                 METHOD
      host    all             all             127.0.0.1/32            trust
```

> [**Fedora-PostgreSQL - Source**](https://fedoraproject.org/wiki/PostgreSQL#link-pghba)


## Reiniciar el servicio postgresql

```bash
sudo systemctl restart postgresql.service
```

## Recargar *postgresql data*

Es la carpeta que contiene la información de postgresql, en el directorio *home* del usuario `postgres` (usuario "root" de postgresql).

```bash
# pg_ctl reload -D data/
```

<br>

# Creacion de usuario y usuario de Base de Datos

Cambiar de usuario, usuario root.

```bash
# su - postgres
```

Ingresar a Postgresql.

```bash
$ psql
```

Cambiar contraseña de usuario "postgres".

```bash
postgres=# \password postgres
```

# Creacion de Base de Datos

```sql
CREATE DATABASE appdatabase;
```

# Creacion de usuario de la base de datos y contraseña

Copiar y pegar el hash generado.

```sql
CREATE USER usuariodatabase WITH PASSWORD 'password';
```

# Optimizacion de base

Django necesita de algunas optimizaciones de la datos Postgresql.

```sql
ALTER ROLE usuariodatabase SET client_encoding TO 'utf8';
ALTER ROLE usuariodatabase SET default_transaction_isolation TO 'read committed';
ALTER ROLE usuariodatabase SET timezone TO 'UTC';
```

#  Dar privilegios a la base de datos.

Dependiendo de los requisitos se deben aplicar los privilegios necesarios, para fines explicativos se utilizará el siguiente ejemplo:

```sql
GRANT ALL PRIVILEGES ON DATABASE appdatabase TO usuariodatabase;
```

# Salir de la Postgresql y del entorno de usuario "postgres"

` \q`

` # exit`

<br>

# Migración, ficheros estáticos, superusuario

Una vez puesta a punto la base de datos, se debe migrar las tablas de Django y las que se estaban usando y se debe preparar los ficheros estáticos.

Además de crear el super-usuario o admin de la aplicación.

```bash
python manage.py check

python manage.py collectstatic

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

# Comprobar posibles errores

```bash
python manage.py check
```

#  Iniciar el servidor, ;)

```bash
python manage.py runserver 0.0.0.0:8000
```

# FIN
