# Commits

# Eliminar commits por su id

Eliminará los directorios creados después del *commit* a eliminar, no es reversible.

```bash
git reset --hard <sha1-commit-id>
```

Con ayuda  de `git log` para buscar en el historial el *commit* deseado.

# Eliminar commit actual

Se eliminará el *commit* actual y se volverá al anterior

```bash
git reset --hard HEAD~1
```

`HEAD~1` indica el *commit* anterior al actual o *head*.


# Enviar los cambios

Una vez realizado la operación y añadido los cambios, se envía.

```bash
git push origin <branch> --force
```


