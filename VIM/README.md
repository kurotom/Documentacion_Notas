# VIM

# Modos

* Visual - *Esc*

# Copiar

Modo Visual + `y`

# Cortar

Modo Visual + `c`


# Pegar



# Edit multiple lines

* En modo `visual`.
* `Ctrl + v` seleccionar las líneas.
* Presionar `Shift + i`.
* Escribir o pegar el texto (previamente copiado).
* Presionar `Esc` y el texto se aplicará.



# Comentar múltiples líneas

1. Dentro del texto, habilitar la numeración de las líneas.

```
:set number
```

2. Establecer las líneas y sustituir mediante regex.

```
:1,4s/^/# /
```


