# Comandos Heroku

Los comandos se pueden ejecutar solamente, o por lo menos a mí, estando en el directorio del proyecto de la aplicación que será desplegada en la plataforma Heroku.


## Instalación

Heroku CLI requiere que la máquina tenga instalado [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


Verificar la versión de HerokuCLI:

  ` # heroku --version`


### Desinstalar

Dependiendo de la forma que se instaló el software y el sistema operativo que se esté usando, existen diferentes formas de realizar esta tarea, acá dejo las que considero las más generales para los SO que utilizo.


- Fedora

  ` # sudo snap remove heroku --classic`


- Windows

  ` > Inicio > Panel de control > Programas > Programas y características > heroku `



## Ficheros logs

| OS | Ubicación |
|-|-|
| macOS | ~/Library/Caches/heroku/error.log |
| Windows | %LOCALAPPDATA%\heroku\error.log |
| Linux/Other | ~/.cache/heroku/error.log (or XDG_CACHE_HOME if set) |


## Comando ayuda

Muestra todos los comandos dispoibles.

  ` # heroku --help`


## Login con Heroku CLI

Después de finalizar la instalación de Heroku CLI se debe ejecutar el siguiente comando para ingresar.

  ` # heroku login`


Se debe presionar una tecla o salir con "q", abrirá una página que pedirá los datos correspondientes.

También permite utilizar autenticación multi-factor usando la opción *-i*

  ` # heroku login -i`


Token API y email se guardan en la ruta `~/.netrc`, ver [documentción autenticación](https://devcenter.heroku.com/articles/authentication).


## Comandos generales

Estos comandos operan en la cuenta Heroku como un todo sin centrarse en una aplicación en particular

  ` # heroku apps`
  === mi@email.com Apps
  app1
  app2
  etc


## Comandos de aplicación

Son ejecutados dentro del directorio de la aplicación, detecta automáticamente el nombre de la aplicación mostrando información de la aplicación.

  ` # heroku apps:info my-app`

```
=== myapp
Addons:         heroku-postgresql:hobby-dev
Auto Cert Mgmt: false
Dynos:          web: 1
Git URL:        https://git.heroku.com/myapp-app.git
Owner:          mi@email.com
Region:         us
Repo Size:      48 KB
Slug Size:      67 MB
Stack:          heroku-20
Web URL:        https://myapp-app.herokuapp.com/
```


<br>

También se puede usar para obtener información de otra aplicación se debe agregar la opción `--app`


##  Crear aplicación

Para crear una nueva aplicación se debe cambiar al directorio donde se quiera empezar el nuevo proyecto y usar:

  ` # cd directorio_proyecto`  
  ` # heroku create nombre_aplicación`

Este comando se usa para inicializar un repositorio git.


## Clonando proyecto Heroku existente

Crea una copia del repositorio guardado en Heroku-hosted que contiene todos los ficheros del proyecto.

  ` # heroku git:clone -a myapp`

## Enviando los cambios realizados al repositorio remoto Heroku

Una vez que se han agregado y comentado los cambios se deben enviar al repositorio.

  ` # git push heroku master`


## Ejecutar la aplicación localmente, servidor para pruebas.

Asegurarse que la aplicación cuenta con los ficheros Procfile, requirements.txt, runtime.txt, listo eso se puede ejecutar.

  ` # heroku local`


Leerá el fichero Profile local, para desplegar un proceso en particular se debe especificar el tipo de proceso, por ejemplo: "web" o "worker".

  ` # heroku local web`


Para finalizar estos procesos, se debe usar `Ctrl + C`.


Opciones:

  * *-f*  :  usa un Procfile diferente, `heroku local -f Procfile.diferente`.

  * *-e*  :  usa un fichero de entorno diferente, `heroku local -e .env.test`.

  * *-p*  :  utiliza un puerto diferente al por defecto que es "5000", `heroku local -p 7000`


Más información, `heroku help local`.


### Revisando las configuraciones de entorno

Para poder revisarlas se debe usar `heroku config`, mostrará todas las configuraciones de entorno establecidas para la aplicación.

Recordar que estas variables son información sensible y **por ningún motivo se deben subir a la nube, en ninguna**, para evitar la incorporación de estos archivos a un eventual "push" se debe agregar el nombre del fichero a `.gitignore`, por ejemplo:

```
  # cat .env
  S3_KEY=keysecreta
  S3_SECRET=mysecret

  # echo .env >> .gitignore
```

**Información sensible como contraseña, usuario, base de datos, llave secreta de applicación, etc.**


Copiar una variable de entorno específica usando el comando `heroku config` a un fichero *.env*.

  ` # heroku config:get CONFIG_VAR_NAME -s >> .env`



## Manejando llaves SSH

Se utiliza SSH para habilitar tunneling para Escudo de Espacios Privado (Shield Private Spaces).

### Generar una llave SSH

  ` # ssh-keygen -t rsa`

### Agregar la llave a la cuenta Heroku

  ` # heroku keys:add`

  o

  ` # heroku keys:add --yes`

  o

  ` # heroku keys:add ~/.ssh/id_rsa.pub`


### Revisar llaves SSH asociadas

Para poder ver qué llaves tenemos asignadas a la cuenta Heroku se puede usar el comando:

  ` # heroku keys`


Usando `--long` mostrará la llave completa, tambien se puede guardar en un archivo usando tuberías.


### Eliminar llaves SSH

Se puede realizar utilizando dirección correo.

  ` # heroku keys:remove usuario@workstation.local`

Se puede realizar utilizando una porción de la llave SSH.

  ` # heroku keys:remove AAAAAAAAAA`

Se puede eliminar todas las llaves.

  ` # heroku keys:clear`

<br>

Un problema común con llaves SSH es que no coincidan, o que se cambió de directiorio o que se creó una nueva y no se acuarda.
Para poder resolver estos problemas, simplemente asocie una nueva llave SSH.


## Renombrar aplicaciones

Se puede renombrar una aplicación cuando quieras usando el comando:

  ` # heroku apps:rename NuevoNombreApp`

  ` # heroku apps:rename NuevoNombreApp --app nombreViejoApp`

### Actualizando Git remotos

Si se renombra la aplicación dentro del diretorio del proyecto asociado con Heroku esta operación se hace automáticamente, pero a veces se debe actualizar remotamente de forma manual.

```
  # git remote rm heroku
  # heroku git:remote -a NuevoNombreApp
```


## Comprobar las instancias en ejecucion de las aplicaciones

  ` # heroku ps`



### Activar la aplicacion
Una vez que la aplicación está desplegada en la "nube" Heroku, se debe "activar" la aplicación.
Desde la consola local.

Activa aplicación:

  ` # heroku ps:scale web=1`


Desactiva applicación:

  ` # heroku ps:scale web=0`



### Revisar los "logs" de la aplicación

  ` # heroku logs --tail`

  ` # heroku logs -a [APPNAME]`


### Ejecutar shell de la nube Heroku.
Este comando nos dará acceso a la shell con comandos limitados para manejar ficheros, aplicar configuración a la aplicación remotamente como variables de entorno.

  ` # heroku run bash`
