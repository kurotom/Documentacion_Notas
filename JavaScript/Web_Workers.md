# Web Workers

Hacen posible ejecutar la operación de un script en un hilo en segundo plano separado de la ejecución el hilo principal de la aplicación web.
Separa del hilo principal (UI) evitando que se bloquee o relentice.


Un worker es un *object* que se crea mediante el uso de **[Worker()](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker)**.

Los workers se ejecutan en un contexto global diferente al actual del navegador.


Puede usar muchos elementos de *window*, incluyendo **[WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)**, y *data storage* (localStorage, [indexesDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API), Data Storage API - Solo Firefox).

[Funciones y clases disponibles para workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Functions_and_classes_available_to_workers).

Tiene limitaciones, no se puede manipular el DOM directamente, usar algunos métodos y propiedades del objeto **[window](https://developer.mozilla.org/es/docs/Web/API/Window)**.

[Worker - doc](https://developer.mozilla.org/en-US/docs/Web/API/Worker).
[Usando Web Workers](https://developer.mozilla.org/es/docs/Web/API/Web_Workers_API/Using_web_workers).

## Cómo funciona.

Los datos se comunican entre los workers y el hilo principal a través de un sistema de mensajes.

* `myworker.postMessage()`  -  envía el mensaje.
* `myworker.onmessage`  -  evento que escucha los mensajes (función).
* `myworker.terminate()`  -  inmediatamente termina el worker.



Los mensajes están dentro de la propiedad `data` del evento, los datos se copian dentro del evento en lugar de compartirse.


## Sintaxis

```javascript
new Worker(aURL);
new Worker(aURL, options);
```

`aURL`:  ubicación del fichero javascript del worker.
`opctions`: opciones para crear una instancia del objeto.
    `type`
        Puede ser - `classic`, `module`.

    `credentials`
        Opciones - `omit`, `same-origin`, `include`.
        Si no se especifica o si `type` es `classic`, es usado `omit` (no requiere credenciales).

    `name`
    	Un string que especifica un nombre identificatorio para [DedicatedWorkerGlobalScope](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope) representando el alcance del worker.



## Excepciones

SecurityError [DOMException](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
	Lanzado si no se permite que el documento inicie trabajadores, p. si la URL tiene una sintaxis no válida o si se infringe la política del mismo origen.

NetworkError [DOMException](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
	Se lanza si el tipo MIME del script de trabajo es incorrecto. Siempre debe ser `text/javascript` (por razones históricas, se pueden aceptar [otros tipos MIME de JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#javascript_types)).

SyntaxError [DOMException](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
	Se lanza si no se puede analizar aURL.




## Ejemplo

my_worker.js
```javascript
postMessage("I\'m working before postMessage(\'ali\').");

onmessage = function (oEvent) {
  postMessage("Hi " + oEvent.data);
};
```


index.js
```javascript
var myWorker = new Worker("my_task.js");

myWorker.onmessage = function (oEvent) {
  console.log("Worker said : " + oEvent.data);
};

myWorker.postMessage("ali");
```







