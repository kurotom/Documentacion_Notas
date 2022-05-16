# Query

Cuando los modelos son creados, Django automáticamente entrega un API de abstracción de base de datos que permite crear, recibir, borrar objetos.



[Queries](https://docs.djangoproject.com/en/4.0/topics/db/queries/)


# Condicional de consulta

```python
Restaurant.objects.filter(
  pizzas__vegetarian=True,     pizzas__name__icontains='mozzarella',
)
```

```python
filtrado = Product.objects.filter(name__icontains=busqueda).order_by('name')
```

## Sintaxis

```
name__icontains
```

`nombre_columna__` = es la columna que se quiere realizar la concidencia, termina con doble guión bajo.

`icontains` = case insensitive para cualquier coincidencia.





[Filtrado de consulta](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filteredrelation-objects)
