# Simple adventure Game

Las cuatros habitaciones principales desde el punto 'start', se ordenarán aleatoreamente, permitiendo elegir al usuario, pudiendo retonar a las habitaciones.

Las "entidades" del juego son: el jugador y tres tipos de enemigos, estos comparten una clase padre.

El propósito es utilizar clases, herencia, métodos, funciones, variables, módulos, input, strings.

Posee:
* Sistema de lucha, la posibilidad de enfrentar o huir, enemigos múltiples, encuentros aleatorios.
* Sistema por turnos, el sistema de lucha se determina por turnos, entre enemigo y el jugador, puede existir más de un enemigo.
* Sistema de vida, mediante sistema de lucha, determinar si el enemigo o el jugador al realizar ataque exitoso le quita vida al contrincante, desencadenando la derrota de dicho enemigo.

[FUTURAS CARACTERÏSTICAS]

El diagrama de las habitaciones que tiene el juego
---

		     +-----------+
		     |   Room    |
		     | something |
		     +-----------+
	+-------+        |            +-------+
	| Chest |        |            | Enemy |
	| room  |----- start ---------| room  |
	+-------+        |            +-------+
		         |
		    +--------+
		    | Silent |
		    |  room  |
		    +--------+      +--------+
		         |          | Choice |     +-------+
		         +----------|  path  |-----| Death |
		                    +----+---+     | room  |
		                         |         +-------+
		                         |
		                     +--------+
		                     | Finish |
		                     |  room  |
		                     +--------+

---

Habitaciones con posible aparición de enemigos: Chest room, Enemy room, Finish room.


# Como ejecutar

- Clonar el juego.
- Cambiar directorio dentro de la carpata del juego.
- Ejecutar
```bash
$ python EngineGame.py
```


