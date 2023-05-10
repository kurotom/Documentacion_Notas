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
