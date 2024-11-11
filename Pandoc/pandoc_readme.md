Paquetes Pandoc

```bash
dnf install -y pandoc pandoc-common librsvg2 librsvg2 librsvg2-tools texlive-xetex
```


Conversión de Markdown a PDF, settings por defecto

```bash
pandoc file.md --pdf-engine=xelatex -s -o test1.pdf
```


Obtener estilo por defecto, permite editarlo

```bash
pandoc --print-highlight-style tango > estilo.theme
```

Convertir fichero/s Markdown a PDF usando estilo determinado

```bash
pandoc file.md -V geometry:margin=1in --pdf-engine=xelatex --highlight-style estilo.theme -s -o final.pdf
```


Concatenar ficheros PDF

```bash
pdfunite index.pdf f1.pdf final.pdf
```

