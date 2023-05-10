# Mover ficheros con guión en nombre

```bash
$ mv ./*.png img/
```


# Uso de `xargs`

Actualizar paquetes Python usando `pip` y `xargs`.

```bash
$ pip list --outdated | cut -d " " -f 1 | xargs -I {} bash -c "echo {}"
```

* `-I {}` : reemplaza el contenido en un string, es una variable entregado por el comando anterior.
