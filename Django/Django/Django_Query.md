# Query

> [Queries - doc](https://docs.djangoproject.com/en/4.0/topics/db/queries/)

Cuando los modelos son creados, Django tiene  una API de abstracción de base de datos que permite crear, recibir, filtrar, borrar objetos.

# Condicional de consulta

```python
Restaurant.objects.filter(
  pizzas__vegetarian=True, pizzas__name__icontains='mozzarella',
)
```

```python
filtrado = Product.objects.filter(name__icontains=busqueda).order_by('name')
```

* `nombre_columna`  : es la columna que se quiere realizar la coincidencia.

* `__icontains`  : case insensitive para cualquier coincidencia, comienza con doble guión seguido del nombre de columna.


# Filtrar datos

> [filter - doc](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filteredrelation-objects)


