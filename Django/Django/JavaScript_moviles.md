# Codigo JavaScript en móviles

Hace poco tuve un problema con el código JavaScript de la aplicación en la que trabajaba, al momento de seleccionar alguna opción dentro del item html "select" funcionaba como se esperaba en un computador, pero en dispositivos móviles no funcionaba, estuve tratando de solucionar el problema y no podía hasta que encontré la solución.

Resulta que el código que escribí, de alguna manera, no lo reconocían en los navegadores .

Mi código era el siguiente:

```javascript
let seleccion = document.querySelector("#select").querySelectorAll(".opciones");
seleccion.forEach(elemento => {
  elemento.addEventListener('click', () => {
    console.log(elemento.value);
  })
})
```

Y lo tuve que cambiar al siguiente:

```javascript
let seleccion = document.getElementById('select');
seleccion.addEventListener('change', () => {
  console.log(seleccion.value);
})
```

Ahora funciona,  :)


La fuente de la solución:

- [Brandon G - stackoverflow](https://stackoverflow.com/a/38087038)

- [codegrepper](https://www.codegrepper.com/code-examples/javascript/select+option+event+listener+click)
