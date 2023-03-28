# SQL Dump

[SQL Dump](https://www.postgresql.org/docs/current/backup-dump.html)


Recrear la base de datos en el mismo estado cuando se creó el respaldo.


[**pg_dump** ](https://www.postgresql.org/docs/current/app-pgdump.html) - extrae una base de datos PosgreSQL dentro de un script u otro fichero.


## Backup

```
pg_dump dbname > dumpfile
```

Escribe el resultado a una salida estándar, se puede crear un backup desde un equipo remoto que tenga acceso a la base de datos. No opera con permisos especiales.

Opciones **-h** para especificar equipo, **-p** para especificar el puerto, **-U** especifica usuario, por defecto es localhost.


## Restaurando la copia de seguridad

Para restaurar usando *psql*:

```bash
psql -f ficheroDumpDB DataBaseName -h IP_HOST_DB -U usuarioDB  -W
```

**dbname** debe existir, *pg_dump* no crea una base de datos.


**pg_dumpall** - respalda cada base de datos en un clúster, también conserva los datos de todo el clúster, como las definiciones de roles y espacios de tabla.
La base de datos debe existir para poder ser respaldado y restaurado y tener acceso a ella.

```bash
  pg_dumpall > dumpfile
```


## Manejando grandes bases de datos

Se puede comprimir los datos respaldados, usando la salida estandar del comando *pg_dump* redirigido o tomado por un comando Unix para comprimir dicha salida a un fichero.

```bash
  pg_dump dbname | gzip > filename.gz
```

Recargar con:

```bash
  gunzip -c filename.gz | psql dbname
```

o usar:

```bash
  cat filename.gz | gunzip | psql dbname
```


Usando el comando **split**, permite dividir en partes grandes archivos (pedazos o chunks):

```bash
  pg_dump dbname | split -b 2G - filename
```

Recargar con:

```bash
  cat filename* | psql dbname
```


Usando GNU split junto con gzip.

```bash
  pg_dump dbname | split -b 2G --filter='gzip > $FILE.gz'
```


## Backup base de datos remota

Se debe tener la direccion del host, el usuario, contraseña, puerto, la base de datos a respaldar.

```bash
  pg_dump -h <direccion> -U <my_username> -p <port> -f <nombre_fichero_respaldo> <base_de_datos>
```

[source](https://stackoverflow.com/a/31886007)
