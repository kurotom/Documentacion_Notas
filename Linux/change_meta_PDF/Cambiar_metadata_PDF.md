# Cambiar metadata en pdf


# Instalar Ghostscript
```
$ sudo dnf install ghostscript
```

# Crear fichero contenedor de marcas

Contendrá los datos como título, autor, fecha de creación, modificación, etc.
El formato de la fecha es año, mes, día, hora, minuto, segundo, ejemplo: `20221017170000 -> 2022/10/17 17:00:00`

```
[ /Title (titulo)
  /Author (autor)
  /Subject (nuevos datos)
  /Keywords (separadas,por,coma)
  /ModDate (D:20221017170000)
  /CreationDate (D:20221017170000)
  /Creator (nuevos datos)
  /Producer (productor pdf o notproductor pdf o nota)
  /DOCINFO pdfmark
```


# Usar Ghostscript

Utilizar ghostscript con el fichero de las marcas.

```
$ gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=OUTPUT.pdf FICHERO_INPUT.pdf fichero_marcas
```


* [Fuente](https://askubuntu.com/questions/27381/how-to-edit-pdf-metadata-from-command-line)
