# Rollback

Cambiar a la version agregada y realizada ("commit"). 
```
$ git checkout COMIT
```

Hacer los cambios, agregar y enviar.
```
$ git add .
$ git commit -m "comentario"
$ git push origin HEAD:main
```

En este caso "main" es el nombre de rama principal.


Revisar los registros
```
$ git log --graph
```
