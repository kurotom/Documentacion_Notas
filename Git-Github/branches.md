# Ramas - Branches

# Agregar branch al repositorio 

Por defecto, branch inicial se llama `master`, para cambiar la banch.

```
$ git init
$ git branch -m main
```

Agregar los archivos a tu nuevo repositorio local.
```
$ git add .
```

Confirmar los archivos que has preparado en tu repositorio local.
```
$ git commit -m "First commit"
```

En Terminal, agrega la URL para el repositorio remoto donde se subirá tu repositorio local.
```
$ git remote add origin  <REMOTE_URL> 
# Sets the new remote

$ git remote -v
# Verifies the new remote URL
```

Sube los cambios en tu repositorio local a GitHub.com.
```
$ git push origin main
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```

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



# Renombrar ramas

[Doc Github](https://docs.github.com/es/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch)

```bash
  git branch -m main principal
  git fetch origin
  git branch -u origin/principal principal
  git remote set-head origin -a
```


En caso de mostrar un error usando el comando "git branch -u origin/principal principal", se realiza lo siguiente:

```bash
git fetch

git branch --unset-upstream

git push --set-upstream origin principal
```


Ahora, si todo está correcto, se puede usar la nueva rama.


# Eliminar ramas local y remotas

Listar ramas

```bash
git branch -a
```

Eliminar ramas locales

```bash
git branch -D RAMA_LOCAL
```

Eliminar ramas remotas

```bash
git push origin -d RAMA_REMOTA
```

