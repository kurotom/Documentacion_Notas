# Pandoc




# Obtener estilo.

```bash
pandoc --print-highlight-style tango > file_style.theme
```

# Convertir Markdown a PDF

Margen de 1 pulgada, con estilo personalizado.

```bash
pandoc markdown_file.md --pdf-engine=xelatex -V geometry:margin=1in  -V "mainfont:DejaVu Sans" -V "monofont:DejaVu Sans Mono"  --highlight style.theme -o final.pdf
```

Opciones:

* `-V fontsize:Npt`  :  tamaño de fuente en donde *N* es un número entero.
* `-V geometry=Nin`  :  tamaño del margen de la hoja PDF.



# Packages Styles

```
sudo dnf install -y texlive-framed
```
