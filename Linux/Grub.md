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
