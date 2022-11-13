# base64

[https://developer.mozilla.org/en-US/docs/Glossary/Base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64)

`Base64` is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding.


# Convertir una imagen a base64

Se puede convertir un fichero a base64 y este se puede almacenar en un fichero JSON (por ejemplo), pero el [tamaño de la imagen aumenta siendo una desventaja notable](https://en.wikipedia.org/wiki/Base64#MIME).

Calculo de bytes
```
bytes = (string_length(encoded_string) − 814) / 1.37
```


# Ventajas de imágenes base64

* Removes separate HTTP Requests for image loading by wrapping encoded image code inside css or HTML.
* Image encoded data can be saved inside database and can generate image file. Just incase we lost image file copy.

# Desventajas de imágenes base64

* Though Base64 increases performance but be careful. Doing so will increase image size approximately 20-25%. than what it is actually in its binary form. So more data has to be transferred on internet. For mobile devices it is a bit drawback.
* Even if we apply gzip compression, doing so will only decrease css file size to around 10-12%.
* IE6 & IE7 not supports Data URI which means base64 images will not be loaded in ie6 & ie7 browsers.
* If you apply base64 encoding to lots of medium sized images it will increase HTML content size or CSS content size. So browser has to do roundtrip to get full content.

[Fuente](http://www.coderiddles.com/base64-images/)



## FileReader

[FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader)

`FileReader` object lets web applications asynchronously read the contents of files (or raw data buffers) stored on the user's computer, using `File` or `Blob` objects to specify the file or data to read.



### Eventos FileReader

| Event | Description |
|-|-|
| abort | Fired when a read has been aborted, for example because the program called FileReader.abort(). |
| error | Fired when the read failed due to an error. |
| load | Fired when a read has completed successfully. |
| loadend | Fired when a read has completed, successfully or not. |
| loadstart | Fired when a read has started. |
| progress | Fired periodically as data is read. |


# Código

```javascript

let imageBase64Stringsep;
let base64String = "";

let fileReader = new FileReader();

fileReader.onload = function () {
  base64String = fileReader.result.replace("data:", "").replace(/^.+,/, "");
  imageBase64Stringsep = base64String;

  console.log(imageBase64Stringsep);
  
}
fileReader.readAsDataURL(file);

```


Es una funcion asincrona, esta se puede usar dentro de una "Promesa" para cuando se adquiera el string base64 se usa el "resolve" para devolverlo.


```
const convertToBase64 = (file) => {

  return new Promise((resolve, reject) => {

    if (file.size === 0) {
      reject(new Error("Sin fichero"));
    }

    let formato = "";
    let headerBase64 = "";

    let pngRE = /.*\w+\.png$/gm
    let jpgRE = /.*\w+\.jpg$/gm
    let webpRE = /.*\w+\.webp$/gm

    if (file.name.match(pngRE).length > 0) {
      formato = "png"
    } else if (file.name.match(jpgRE) > 0) {
      formato = "jpg"
    } else if (file.name.match(webpRE) > 0) {
      formato = "webp"
    }


    headerBase64 = `data:image/${formato};base64,`;


    let imageBase64Stringsep;
    let base64String = "";

    let fileReader = new FileReader()
    fileReader.onload = function () {
      base64String = fileReader.result.replace("data:", "").replace(/^.+,/, "");
      imageBase64Stringsep = base64String;
      resolve(headerBase64 + base64String);
    }
    fileReader.readAsDataURL(file);

  });
}

convertToBase64.then(
  (resolve) => {
    console.log(resolve);
  },
  (reject) => {
    console.log(reject);
  }
)
```




Para guardar en un fichero JSON debe iniciar el string con `data:image/[FORMATO_IMAGEN];base64,` y se puede guardar dentro del fichero JSON.
