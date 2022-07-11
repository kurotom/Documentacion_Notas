# Sets

Data type: **sets**

Usado para almacenar múltiples ítems en una única variable.

* No tienen orden, no se pueden referir por índice o key.
* No se pueden cambiar los valores.
* No se permiten duplicados.

```python
myset = {1, 2, "item", True, 2.1}
```


Se puede declarar usando constructor **set()** y como parámetro una tupla, valores no repetidos.
O creándolo usando **{ }** y los valores, valores no repetidos.

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

a = set('abracadabra')
# {'a', 'r', 'b', 'c', 'd'}
```

| Métodos | Descripción |
|-|-|
| len(set) | retorna la cantidad de elementos del set |
| x in s | retorna booleano. |
| x not in s | retorna booleano. |
| isdisjoint(other_set) | retorna True si existen elementos no en común. |
| set_uno <= set_dos | comprueba cada elemento esté en el otro. |
| set_uno < set_dos | |
| .union(set_otro) | concatena sets. |
| set_uno | set_dos | concatena sets. |
| set_uno & set_dos | retorna un nuevo set con elementos en común. |
| .intersection(otro_set) | retorna nuevo set con elementos en común. |
| .difference(otro_set) | retorna nuevo set con elementos NO en común. |
| set_uno - set_dos | retorna nuevo set con elementos NO en común. |
| .copy() | crea una shadow copy. |
| .update({'elementos'}) | actualiza el set, agrega elementos. |
| .add({elementos}) | agrega elementos al set. |
| .remove(elemento) | elimina elemento si existe. |
| .discard(elemento) | elimina elemento si existe. |




