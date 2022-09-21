# Drag and Drop API

Interface Drag and Drop habilita que aplicaciones usar característica drag-and-drop en navegadores.

Seleccionar un elemento arrastrable con el mouse, botar ese elemento en otro elemento por medio del botón del mouse.


## Evento `Drag`

HTML drag-and-drop usa `modelo evento DOM` y `evento drag` heredados del `evento mouse`. Operaciones *drag* típicamente comienza cuando un usuario selecciona un elemento arrastrable, arrastrarlo a un elemento hacia un elemento a botar, y entonces libera el elemento arrastrable.

Durante la operaciones, varios tipos de eventos se desencadena, algunos más de una vez, como eventos [`drag`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drag_event) y [`dragover`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event).


Cada [tipo de evento Drag](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent#event_types) tiene eventos asociados:

| Evento | Cuando se desencadena... |
|-|-|
| drag | un elemento arrastrable se arrastra. |
| dragend | operación arrastrable termina, como liberar el botón del mouse o usando `Esc`. |
| dragenter | item arrastrable ingresa un objeto válido drop. |
| dragleave | item arrastrable en un elemento drop válido. |
| dragover | item arrastrable se termina en un objeto drop válido. |
| dragstart | el usuario comienza arrastrable. |
| drop | item es botado en un objetivo drop válido. |



Ejemplo
```javascript
<!DOCTYPE HTML>
<html>
<head>
<style>
#div1, #div2 {
  float: left;
  width: 100px;
  height: 35px;
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
}
</style>

<script>

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}

</script>

</head>
<body>

<h2>Drag and Drop</h2>
<p>Drag the image back and forth between the two div elements.</p>

<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)">
  <img src="img_w3slogo.gif" draggable="true" ondragstart="drag(event)" id="drag1" width="88" height="31">
</div>

<div id="div2" ondrop="drop(event)" ondragover="allowDrop(event)"></div>

</body>
</html>
```


1. Establecer el elemento arrastrable, `ondragstart=`, `draggable="true"`.
2. Determinar qué pasa con el elemento es arrastrable, `function drop(ev)`.
3. Establecer elemento drop, `ondrop="drop(event)"`, `ondragover="allowDrop(event)`.
4. Determinar qué hacer en drop, `drop(ev)`.



## Files - Drag and Drop

[Files - drag & drop](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API/File_drag_and_drop)

Interfaces Drag and Drop permite arrastrar y soltar ficheros en una página web.

[HTML drag and drop](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API) tiene dos APIs diferentes para soportar arrastrado y soltado de ficheros.

* Interface [DataTransfer](https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer)
* Interfaces [DataTransferItem](https://developer.mozilla.org/en-US/docs/Web/API/DataTransferItem) y [DataTransferItemList](https://developer.mozilla.org/en-US/docs/Web/API/DataTransferItemList)


Necesita de los siguientes elementos.

1. Definir zona drop, con evento `ondrop`, dentro de un elemento como un `<div>`.
```
<div
  id="drop_zone"
  ondrop="dropHandler(event);"
  ondragover="dragOverHandler(event);">
  <p>Drag one or more files to this <i>drop zone</i>.</p>
</div>

```

`ondragover`, entrega una función que deshabilita el comportamiento por defecto drag.


2. Procesar el drop, cuando el usuario bota ficheros, el navegador utiliza la interface `DataTransferItemList`, usando el método `getAsFile()` para cada fichero; de otra manera, se utiliza la interface `DataTransfer` usando la propiedad `files` para acceder a cada fichero.

```javascript
function dropHandler(ev) {
  console.log('File(s) dropped');

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();

  if (ev.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    [...ev.dataTransfer.items].forEach((item, i) => {
      // If dropped items aren't files, reject them
      if (item.kind === 'file') {
        const file = item.getAsFile();
        console.log(`… file[${i}].name = ${file.name}`);
      }
    });
  } else {
    // Use DataTransfer interface to access the file(s)
    [...ev.dataTransfer.files].forEach((file, i) => {
      console.log(`… file[${i}].name = ${file.name}`);
    });
  }
}
```

3. Prevenir comportamiento default drag.

```javascript
function dragOverHandler(ev) {
  console.log('File(s) in drop zone');

  // Prevent default behavior (Prevent file from being opened)
  ev.preventDefault();
}
```


## Fuente

* [https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
* [https://www.w3schools.com/html/html5_draganddrop.asp](https://www.w3schools.com/html/html5_draganddrop.asp)
