# Establecer kernel por defecto

1. Identificar los kernels instalados

```bash
sudo grubby --info=ALL | grep -E "^kernel|^index"
```

2. Establecer el nuevo kernel por defecto

```bash
sudo grubby --set-default-index=N
```

3. Obtener el kernel por defecto

```bash
sudo grubby [--default-kernel|--default-title]
```


# Reinstalar Grub

1. Listar kernels instalados

```
$ dnf list kernel
```

2. Comprobar cuál grub se está usando

```
$ sudo grubby --default-kernel
```

3. Reinstalar kernel corrupto

```
$ sudo dnf install kernel-core-[version]
```
