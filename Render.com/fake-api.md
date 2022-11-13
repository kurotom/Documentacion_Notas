# Fake api

El desarrollo frontend necesita de una api para poder construir páginas web utilizando [json-server](https://github.com/typicode/json-server) podemos lograr esto, `json-server` permite tener en local un api rest.

Además podemos implementar uno en línea utilizando los servicio de [render.com](https://render.com/).


# En local

1. Creamos el fichero *package.json*, `npm init`.
2. Editamos el fichero *package.json*, agregamos la línea `start` para poder iniciar el servicio con parametros específicos.
```
  [...],
  
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"                              //  <---- Agregar
  },
  
  [...],
```
2. Instalamos `json-server`, `npm install json-server`.
3. Creamos fichero `server.js`
```
const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults();
const port = process.env.PORT || 3000;

server.use(middlewares);
server.use(router);

server.listen(port)
```
5. Creamos `.gitignore` y dentro `node_modules` para evitar envíar datos innecesarios.
6. Enviamos los cambios al repositorio.

# En Render.com

Creamos una cuenta, agregamos los datos necesarios.

7. Creamos un nuevo servicio web free tier.
8. Conectamos con Github y agregamos el repositorio que tiene los datos de la fake api.
9. En las opciones, *Build Command*, `npm install`.
10. En las opciones, *Start Command*, `npm start`.
11. Creamos el servicio, esperamos y podremos tener un `json-server` - fake api en línea.


