# Configurar variables entorno en Heroku

Se puede realizar por medio de Dashboard o por CLI.

## CLI

Estando dentro de la carpeta del proyecto se debe ejecutar el siguiente comando:

```shell
#  heroku config:set NOMBRE_VARIABLE='VALOR_VARIABLE'
```





## Ejemplo

Configurar variables para base de datos.

```shell
#  heroku config:set DB_NAME='DB_nombre'
#  heroku config:set USER_DB='usuario'
#  heroku config:set DB_PASS='password'
#  heroku config:set HOST_DB='db_direccion.web.com'
#  heroku config:set KEY_APP='key_random'

```
