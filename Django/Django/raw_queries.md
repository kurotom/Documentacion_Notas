# Raw queries

Realizar consultas usando leguaje SQL directamente estas retornan instancias de modelo.

```python
 Manager.raw(raw_query, params=(), translations=None)
```

Toma una consulta raw SQL y retorna una instancia *django.db.models.query.RawQuerySet*, esta puede ser iterada como una consulta *QuerySet* normal.

Ejemplo:


Modelo
```python
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
```

Raw SQL
```python
for p in Person.objects.raw('SELECT * FROM myapp_person'):
  print(p)

#John Smith
#Jane Jones
```

**raw()** ordena o mapea automáticamente las consultas.

```python
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')

Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')

Person.objects.raw('''SELECT first AS first_name,
  last AS last_name,
  bd AS birth_date,
  pk AS id,
  FROM some_other_table''')
```



[Queries - Django docs](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.raw)
[Raw Queries - Django docs](https://docs.djangoproject.com/en/4.0/topics/db/sql/)
