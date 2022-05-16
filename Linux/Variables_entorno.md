# Variables de entorno

> Una variable de entorno es una variable dinámica que puede afectar al comportamiento de los procesos en ejecución en un ordenador, [Wikipedia](https://es.wikipedia.org/wiki/Variable_de_entorno).


Cuando estaba estudiando no le encontré sentido a esto, lo aprendí, pero en mi mente no lograba conectar con situaciones.

Hasta que construí una aplicación web, leí la documentación que se utilizaban variables de entorno como forma de asegurar información sensible que utiliza la aplicación, como usuario de base de datos, contraseña de este, la dirección de la base de datos, entre otros, y en ese momento lo entendí, bueno pasemos a lo que importa.


## Configurar variables de entorno.

Se puede realizar de dos formas temporales o permanentes.

### En Linux.

* Temporales

```
  # export NOMBRE_VARIABLE=lo_que_hace
```

* Permanente

Se deben agregar al ficehro *.bash_profile*

```
  # vim .bash_profile
  [...]
  export NOMBRE_VARIABLE=lo_que_hace
```

Para listar todas las variables.

```
  # export -p
```


### En Windows

* Con entorno gráfico:
```
Este equipo > Propiedades > Configuración avanzada del sistema > Opciones avanzadas > Variables de entorno
```

Se pueden agregar, editar o eliminar variables para el usuario o del sistema, una vez finalizado se guarda y se acepta.


* Con comandos, para usuario:
```
setx NOMBRE_VARIABLE "lo_que_hace"
```

* Con comando, para todo el sistema, con los permisos necesarios:
```
setx /M NOMBRE_VARIABLE "lo_que_hace"
```


Mostrar todas las variables

```
set
```
