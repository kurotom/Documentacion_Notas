# Enviar los cambios a una rama

El propósito de separar los cambios de la rama principal es evitar romper la continuidad del proyecto, y una vez que se ha revisado se une esa rama con la principal.


[source](https://docs.github.com/es/get-started/using-git/pushing-commits-to-a-remote-repository)


```bash
  git push origin <branch>
```



# Recibir los cambios de la rama remota

Une los cambios obtenidos, por lo que antes de ejecutar este comando se debe estar seguro que no se han realizados cambios locales.

```bash
  git pull <remote> <branch_name>
```
