# Conflicto paquetes

Después de actualizar se presento un problema de conflicto de paquetes entre la versión anterior y la actual.

Por lo que necesita eliminar la versión antigua y volver a actualizar el sistema.


---

En este caso, los paquetes con conflicto eran *systemd* y *systemd-udev*

---


# Formas de realizar la tarea

Entorno Fedora 35.

## Manual

1. Identificar los paquetes con conflicto.

```
$ sudo dnf list installed | grep -i systemd
```

2. Eliminar todos los paquetes con conflicto.

```
$ sudo rpm -ev --nodeps systemd-[version.antigua].fc35.x86_64
```

3. Actualizar el sistema.

```
$ sudo dnf update -y
```


## Con el administrador de paquetes


1. Gestor de paquetes

```
$ sudo dnf remove --duplicates
```

Equivalente a:

```
$ yum's package-cleanup --cleandups):
```

2. Actualizar sistema.

```
$ sudo dnf update -y
```
