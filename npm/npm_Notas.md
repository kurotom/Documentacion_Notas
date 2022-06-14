# Errores

Lista de errores que he tenido usando [node](https://docs.npmjs.com/).


# errno: -28

```bash
[...]
  errno: -28,
  syscall: 'watch',
  code: 'ENOSPC',
[...]
```


Define límites de usuario en la cantidad de recursos de *inotify* y las vigilancias de archivos de *inotify*. Si se alcanzan estos límites, es posible que experimente procesos que fallan con mensajes de error relacionados con los límites.

---

**inotify** - monitoring filesystem events

The inotify API provides a mechanism for monitoring filesystem events. Inotify can be used to monitor individual files, or to monitor directories.  When a directory is monitored, inotify will return events for the directory itself, and for files inside the directory.

---

Para obtener el límite del sistema:

```bash
$ getconf ARG_MAX
```


Se puede solucionar de dos formas:

* Se puede cambiar el límite, como root.

	**Cambios Temporales**
	
	Revisar los límites que se tienen.

	```bash
	$ cat /proc/sys/fs/inotify/max_user_instances
	$ cat /proc/sys/fs/inotify/max_user_watches
	```
	
	Actualizar los límites, si es necesario.
	```bash
	$ sudo sysctl fs.inotify.max_user_instances=8192
	$ sudo sysctl fs.inotify.max_user_watches=524288
	$ sudo sysctl -p
	```

	**Cambios Permanentes**
	
	```bash
	$ echo fs.inotify.max_user_instances=8192 | sudo tee -a /etc/sysctl.conf
	$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
	$ sudo sysctl -p
	```


* Cambiar a una ruta más corta, como el "home" del usuario, usar nombres para los ficheros que sean cortos y distintivos.

---

Tratar de evitar el uso de **soft-link** para "acortar" el camino a el directorio del proyecto *React*, dará *errno: -24*, y se debe cambiar los parámetros anteriormente explicados.

---



