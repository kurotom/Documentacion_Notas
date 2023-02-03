# Cortar un string

Para cortar un string en bash mediante un patrón de forma sencilla, se debe utilizar carácter escape (`\`) para quitar la funcionalidad de los carácteres especiales.

# Sintaxis

```bash
variable=${stringCortar%patronCorte*}
```


# Ejemplo

```bash
name="unfichero.final"
var=${name%\.final*}

echo $name "--->"  $var
# unfichero.final ---> unfichero
```





