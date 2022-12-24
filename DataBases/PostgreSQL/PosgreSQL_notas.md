# PosgreSQL

# Instalar repositorio RPM:

```bash
  sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/F-35-x86_64/pgdg-fedora-repo-latest.noarch.rpm
```

# Install PostgreSQL:

```bash
  sudo dnf install -y postgresql14-server postgresql14-contrib
```

[Install - postgresql.org](https://www.postgresql.org/download/linux/redhat/)

<br>

### Ficheros de configuración

Ficheros principales de configuración de servidor postgresql.

  * `/var/lib/pgsql/data/postgresql.conf`

  * `/var/lib/pgsql/data/pg_hba.conf`



### Habilitar y preparar para primer inicio del servicio

```bash
  sudo /usr/pgsql-14/bin/postgresql-14-setup initdb

  sudo systemctl enable postgresql-14

  sudo systemctl start postgresql-14
```


Si se genera un error se debe a que no existen los ficheros de configuración `postgresql.conf` y `pg_hba.conf`, para generarlos:

```bash
  sudo postgresql-14-setup initdb
```

Usar el comando para revisar el error:
s
` # journalctl -xn`


### Configurar `firewall-cmd`.

  Recordar agregar la zona que usará el servicio postgresql, en este caso usará la por defecto.

```bash
  sudo firewall-cmd --permanent --add-port=5432/tcp

  sudo firewall-cmd --reload
```


# Ficheros del servicio posgresql

## Modificar fichero postgresql.conf

Para que acepte conexiones desde la red, se debe cambiar:

```bash
  sudo vim /var/lib/pgsql/14/data/postgresql.conf
```

      listen_addresses = 'localhost'

          cambiarlo a

      listen_addresses = '*'



Para poder mejorar la seguridad cambiar la configuración de md5 a scram-sha-256 en `postgresql.conf`.

      password_encryption = scram-sha-256



Configurar el acceso al servidor de base de datos, agregando o modificando las reglas.

[Documentación **pg_hba.conf**](https://www.postgresql.org/docs/9.6/auth-pg-hba-conf.html)

```bash
  sudo vim /var/lib/pgsql/14/data/pg_hba.conf
```


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



# Uso de postgresql

PostgreSQL usa modelo cliente/servidor, `postgres` es el "administrador" del servicio PostgreSQL.

Para usarlo debemos cambiar la contraseña con permisos root usando `passwd`.

```bash
$ sudo passwd postgres
```

Ahora se puede cambiar a "posgres" y poder configurar la base de datos y el/los usuario/s que tendrán acceso a estos.

```bash
$ su -l postgres
```

# Administración del servidor

Configurar, administrar usuarios y base de datos.

## Crear, borrar una base de datos

`createdb` crea una nueva base de datos PostgreSQL.

```bash
$ createdb [opciones] db_name
```
Opciones:
U|--username : username.
W|--password : password.
h|--host : dirección servidor.
p|--port : puerto TCP.


`dropdb`, elimina una base de datos

```bash
$ dropdb db_name
```

## Crear nombre_usuario

`createuser` defina cuenta de usuario PostgreSQL.

```bash
$ createuser [opciones] username
```
Opciones:
d|--createdb : el nuevo usuario podrá crear base de datos.
s|--superuser : el nuevo usuario será super-usuario.
h|--port
U|--username
W|--password


`dropuser` elimina usuario.

```bash
$ dropuser username
```

## Roles base de datos

Para crear un rol usar `CREATE ROLE`.

Comando `\du` para listar todos lo roles existente en la base de datos.

```bash
=# CREATE ROLE name_rol ATTRIBUTE_ROL
```

ATTRIBUTE_ROL : nombre de los roles.

* LOGIN
* SUPERUSER
* CREATEDB
* CREATEROLE
* PASSWORD


## Roles de miembros

Primero se deben crear los roles. Luego se puede usar `GRANT` o `REVOKE` a los miembros.

```
GRANT grupo_rol TO role1, ...;
REVOKE group_rol FROM role1, ...;
```

```
CREATE ROLE joe LOGIN INHERIT;
CREATE ROLE admin NOINHERIT;
CREATE ROLE wheel NOINHERIT;
GRANT admin TO joe;
GRANT wheel TO admin;
```


## Tipos de datos

### Character

|-|-|
| varchar(n) | n = tamaño string |
| char(n) | n = tamaño string |
| text | variable tamaño ilimitado |


### Numeric

|-|-|
| integer | 4 bytes size, -2147483648 to +2147483647 |
| decimal&#124;numeric | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point |
| serial | 4 bytes size, 1 to 2147483647 |
| bigserial | 8 bytes size, 1 to 9223372036854775807 |


### Date/Time

|-|-|
| timestamp | sin zona horaria, yyyy-mm-dd HH:MM:SS |
| timestamptz | con zona horaria, yyyy-mm-dd HH:MM:SS |

Al usar `timestamptz` cambiará de acuerdo a `timezone` de la tabla.
Para declarar una zona horaria `SET timezone = 'time_zone'`.


### Monetary

|-|-|
| money | 8 bytes size, -92233720368547758.08 to +92233720368547758.07 |


### JSON

|-|-|
| json | permite guardar datos formato JSON |


## Tablas


### Crear PRIMARY KEY AUTOINCREMENT

Se debe utilizar `SERIAL` para la llave auto incremental y declarar `PRIMARY KEY`.

```
CREATE TABLE datos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  descripcion VARCHAR(255),
  cantidad integer NOT NULL
);

```


### 'SEQUENCE' - 'SERIAL' - id autoincremental
> 8.1.4. Serial Types - page 147]

Crear una secuencia para declarar 'id' en cada fila de datos ingresada.

```
CREATE SEQUENCE name_sequence;

CREATE TABLE name_table (
	col_name integer NOT NULL DEFAULT nextval('name_sequence')
);

ALTER SEQUENCE name_sequence OWNED BY name_table.col_name;
```

Se puede usar *col_name integer PRIMARY KEY DEFAULT nextval('name_sequence')*.

Lo siguiente es equivalente:

```
CREATE TABLE name_table (
	id SERIAL,
	colName varchar(10)
);
```


### INSERT

```
INSERT TO name_table (col1, col2, ...) VALUES ( val1, val2, ...);
```

### DELETE

```
DELETE FROM name_table WHERE col_name = 'value';
```


### QUERY

```
SELECT * FROM name_table;
SELECT (col2, col3) FROM name_table;
SELECT (col2, col3) FROM name_table WHERE col3 = 'algo';
```


### JOIN

```
SELECT * FROM table1 JOIN table2 ON colX = 'value';
```

Formas:
* JOIN
* INNER JOIN
* LEFT JOIN
* LEFT OUTER JOIN
* RIGHT JOIN
* RIGHT OUTER JOIN
* FULL OUTER JOIN


```
SELECT * FROM products INNER JOIN category USING (id);

SELECT * FROM products JOIN category ON (products.category_id = category.id);

```




### Aggregate Functions

* count
```
SELECT max(column_value) FROM name_table;
```

* max
```
SELECT city FROM weather WHERE temp_lo = (SELECT max(temp_lo) FROM weather);
```

* sum
* avg
* min


### UPDATE

```
UPDATE weather SET colum1 = 'new value', column2 = 'new value2' WHERE name_column = 'información';
```


### FOREIGN KEY

*references name_table(col)*.

```
CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name varchar(255),
  category integer references category(id)
);
```

Es equivalente:

```
CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name varchar(255),
  CONSTRAINT fk_category
    FOREIGN KEY (category)
      REFERENCES category(id)
);

```


## Administración PostgreSQL


### Listar conexiones en base de datos

```
SELECT * from pg_stat_activity ;
```



