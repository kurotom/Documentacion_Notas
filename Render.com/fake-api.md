# Fake api

El desarrollo frontend necesita de una api para poder construir páginas web utilizando [json-server](https://github.com/typicode/json-server) podemos lograr esto, `json-server` permite tener en local un api rest.

Además podemos implementar uno en línea utilizando los servicio de [render.com](https://render.com/).


# En local

1. Creamos un nuevo paquete.
```
$ npm init
```

2. Editamos el fichero *package.json*, agregamos la línea `start` para poder iniciar el servicio con parametros específicos.
```
  [...],
  
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"                              //  <---- Agregar
  },
  
  [...],
```
2. Instalamos `json-server`.
```
$ npm install json-server
```

3. Creamos fichero `server.js`
```
const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults();
const port = process.env.PORT || 3000;

server.use(middlewares);
server.use(router);

server.listen(port);
```

5. Creamos `.gitignore` y dentro `node_modules` para evitar envíar datos innecesarios y ficheros con información sensible como `.env`.

6. Enviamos los cambios al repositorio.



# En Render.com

1. Creamos una cuenta, agregamos los datos necesarios.

2. Creamos un nuevo **[Web Service](https://dashboard.render.com/select-repo?type=web)**.

3. Conectamos con Github y agregamos el repositorio que tiene los datos de la fake api.
Podemos hacerlo de 2 formas:
	a) El repositorio en Github es público, copiarmos la URL del repositorio y lo agregamos en la sección **Public Git repository**.

	b) Si el repositorio es privado, debemos conectar *render.com* a *Github*, para ello:
		b.1) Ir a `Account Settings`, en la sección **Profile**, conectamos con Github, damos permisos y aceptamos/conectamos.
		b.2) Clic en `+ Connect account` en la sección Github.
		b.3) Nos mostrará información y permisos que tendrá en los repositorios. Podemos dar acceso a todos los repositorios o tendrá acceso en algunos que seleccionaremos.
		b.4) Seleccionar `Only select repositories` y elegimos el repositorio.
		b.5) Clic en el botón, `Install`.
		b.6) Ahora nos mostrará el repositorio a que `render` podrá acceder y le damos a `Connect`.
	
4. Completar los parámetros de despliegue que utilizará la aplicación.
* Name: nombre del servicio
* Region: seleccionar región más próxima o menos latencia.
* Branch: la rama que se utilizará
* Root Directory
* Environment: selecionar el lenguaje que se utilizará, en este caso, `Node`.
* Build Command, agregar `npm install`.
* Start Command, agregar `npm start`.
* Seleccionamos el tipo de plan **Free**.
* Opcional - sección `Advanced`, si la aplicación utiliza variables de entorno, ficheros `.env` o cualquier otro fichero con información sensible como claves, url de base de datos, etc., se debe agregar. Damos clic en `Add Environment Variable` o agregamos el fichero en `Add Secret File`.
* Auto-Deploy, *render* realizará un nuevo despliegue por cada `git push` nuevo que se haga, o lo hacemos manualmente.

5. Clic en `Create Web Service` y esperar a que se complete el proceso.
6. Nos mostrará un dashboard con la url, logs, settings, entre otras, algunas funciones más avanzadas se necesita pagar, pero la versión **Free** es suficiente para crear aplicaciones para practicar y aprender.

---

En Github podemos editar, agregar o revocar los permisos cuando queramos, ir a `Settings` y en la sección `Applications`.

---
