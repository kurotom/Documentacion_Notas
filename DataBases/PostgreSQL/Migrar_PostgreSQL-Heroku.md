# De PostreSQL Local a Heroku y viceversa

Para poder realizar una migración de una base de datos in-promise a Heroku, necesitamos:

1. Crear un respaldo de la base de datos local.
2. Envíar los datos a la base de datos PostgreSQL Heroku.


Requisitos:
* Se debe haber iniciado o enlazado Heroku al directorio actual, 'heroku login', 'heroku git:remote -a app_heroku'.
* Este procedimiento solo sirve para entorno "dentro de heroku", si se realiza fuera del directorio iniciado no funcionará.

## Crear dump base de datos.

Cambiamos al usuario `postgres`, creamos el respaldo.

```bash
$ su -l postgres

$ pg_dump db_Data > db_Data-dump
```

## Enviar los datos a Heroku.

Se usará la herramienta heroku-cli para "enviar" los datos a Heroku PostgreSQL.

```bash
$ heroku pg:psql --app nombre_app_heroku < db_Data-dump
```


# Entorno fuera del directorio

Necesitamos tener el fichero 'dump' de la base de datos, la url de la base de datos, el nombre de la aplicación, y heroku-cli.

Desde usuario `postgres`.

```bash
$ heroku pg:push your-database-name DATABASE_URL -a your-app-name
```

DATABASE_URL: se encuentra en 'https://data.heroku.com/datastores/' de la aplicación, en la sección Heroku CLI (postgresql-xxxx).



