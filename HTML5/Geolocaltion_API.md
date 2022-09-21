# Geolocation API

HTML Geolocation API es usado para ubicar la posición geográfica del usuario.

El usuario *debe* aprobar el uso de esta funcionalidad.

Geolocation es más precisa en dispositivos con GPS, como los smartphones.

Utilizando **`navigator.geolocation`**.


Forma de acceder a la información de la ubicación:

* `Geolocation.getCurrentPosition()`: recupera la ubicación del dispositivo actual.

* `Geolocation.watchPosition()`: registra una función que automáticamente se llama cada vez que cambia la posición del dispositivo, retornando ubicación actualizada.
Para detener este método `clearWatch()`.


En ambas formas se requieren 3 argumentos:

* Un callback exitoso obligatorio: si se recibe la ubicación de forma exitosa, el callback ejecuta el objeto `GeolocationPosition`, este objeto es el único parámetro.

* Un callback de error opcional: si falla, el callback se ejecuta con un objeto `GeolocationPositionError` con este único parámetro, provee información de lo que falló.

* Un objeto opcional el cual provee opciones para recibir la información de la posición.


## Usando HTML Geolocation

`getCurrentPosition()` retorna la posición del usuario, la latitud y longitud.

```javascript
<script>

var x = document.getElementById("demo");
function getLocation() {
 if (navigator.geolocation) {
   navigator.geolocation.getCurrentPosition(showPosition);
 } else {
   x.innerHTML = "Geolocation is not supported by this browser.";
 }
}

function showPosition(position) {
 x.innerHTML = "Latitude: " + position.coords.latitude +
 "<br>Longitude: " + position.coords.longitude;
}

</script>
```


Primero comprueba si *Geolocation* es soportado, si lo soporta, obtiene los datos.


## Manejo de errores

Entregando un segundo parámetro al método `getCurrentPosition()` para manejar los errores.

Ejemplo de manejo de errores:
```javascript
function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred."
      break;
  }
}
```


## Métodos `getCurrentPosition()`

| Propiedad | Retorna |
|-|-|
| coords.latitude | The latitude as a decimal number (always returned) |
| coords.longitude | The longitude as a decimal number (always | returned)
| coords.accuracy | The accuracy of position (always returned) |
| coords.altitude | The altitude in meters above the mean sea level | (returned if available)
| coords.altitudeAccuracy | The altitude accuracy of position | (returned if available)
| coords.heading | The heading as degrees clockwise from North | (returned if available)
| coords.speed | The speed in meters per second (returned if available) |
| timestamp | The date/time of the response (returned if available) |



## `watchPosition()`


`watchPosition()`: retorna de forma continua la posición actual del usuario.
`clearWatch()`: detiene el método `watchPosition()`.


```javascript
<script>

var x = document.getElementById("demo");
function getLocation() {
 if (navigator.geolocation) {
   navigator.geolocation.watchPosition(showPosition);
 } else {
   x.innerHTML = "Geolocation is not supported by this browser.";
 }
}

function showPosition(position) {
 x.innerHTML = "Latitude: " + position.coords.latitude +
 "<br>Longitude: " + position.coords.longitude;
}

</script>
```
