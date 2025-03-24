# Docs_programacion

Repositorio de documentación de diferentes temas de interés.

Si te sirvió algo, una :star: a este repositorio ayuda a continuar.


# Notas y experiencias.

Anotaciones de sucesos con los que me he topado y he resuelto o estoy en proceso.

# Fuentes en desarrollo web

Utilizar **siempre** más de una fuente, y agregar fuente adicional de sistema por si las otras no cargan.

Artículos:

- [https://www.silocreativo.com/4-combinaciones-de-tipografias-google-font-para-usar-en-tu-web/](https://www.silocreativo.com/4-combinaciones-de-tipografias-google-font-para-usar-en-tu-web/)

- [https://www.canva.com/es_mx/aprende/guia-definitiva-para-combinar-fuentes/](https://www.canva.com/es_mx/aprende/guia-definitiva-para-combinar-fuentes/)

- [https://baronilustra.es/mejores-combinaciones-tipografias-web/](https://baronilustra.es/mejores-combinaciones-tipografias-web/)


## Django 4.1 - DRF - 19-08-2022

Error collectstatic - solución downgrade a Django 4.0.7

## CORS, Django REST Framework (API), REACT.

Desde distintos servicios (heroku, render, vercel) los métodos GET los tuve que hacer sin escribir headers en las peticiones.

Métodos POST, se necesitaban para autenticación.

CORS siempre al lado del servidor.

---

## Pulsar Editor

Al crear fichero y agreagar líneas automáticamente.

1. **Pulsar** y busca en la paleta de comandos (`Ctrl+Shift+P`):
   - `Application: Open Your Init Script`

2. Dentro del archivo `init.js`, agrega este código:

   ```javascript
    atom.workspace.observeTextEditors((editor) => {
        const filePath = editor.getPath();
        if (!filePath || !filePath.endsWith('.py')) return;
    
        const firstLine = editor.lineTextForBufferRow(0);
        if (!firstLine.startsWith('# -*- coding: utf-8 -*-')) {
            editor.setText(`# -*- coding: utf-8 -*-\n${editor.getText()}`);
        }
    });
   ```

3. Guarda el archivo y reinicia Pulsar.
