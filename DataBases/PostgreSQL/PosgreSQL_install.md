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
