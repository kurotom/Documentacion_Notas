# Agregar un repositorio local a GitHub utilizando Git

Por defecto, branch inicial se llama `master`, para cambiar la banch.

```
$ git init && git branch -m main
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


