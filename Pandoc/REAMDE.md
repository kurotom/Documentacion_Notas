# Pandoc




# Obtener estilo.

```bash
pandoc --print-highlight-style tango > file_style.theme
```

# Convertir Markdown a PDF

Margen de 1 pulgada, con estilo personalizado.

```bash
pandoc file_markdown -V geometry:margin=1in --pdf-engine=xelatex --highlight-style file_style.theme -s -o filename-out.pdf
```

Opciones:

* `-V fontsize:Npt`  :  tamaño de fuente en donde *N* es un número entero.
* `-V geometry=Nin`  :  tamaño del margen de la hoja PDF.

