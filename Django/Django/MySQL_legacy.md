# MySQL existentes

Django soporta veriones 5.7 o mayores de MySQL.

Django **inspectdb** usa la base de datos **information_schema**, la cual contiene información de todos los esquemas de la base de datos.

[Databases - Django](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes)


## Usando una base de datos.

1) Instalar paquetes necesarios para usar mysql.

```shell
    pip install pymysql
```

2) Para poder conectar una aplicación Django se debe configurar en *settings.py*, incorporar el paquete instalado a la configuración.

```python
[...]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('USER_DB'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('HOST_DB'),
        'CONN_MAX_AGE': 60,
        'PORT': '3306',
    }
}

[...]

pymysql.install_as_MySQLdb()
```

2) Luego ejecutar el comando para generar el nuevo fichero *models.py*.

```shell
    python manage.py inspectdb > models.py
```

Por defecto, *inspectdb* crea modelos sin administrar, *managed = False*, en **Meta** de las clases de models.py.

Ejemplo, models.py
```python
class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
```

[managed - documentación](https://docs.djangoproject.com/en/4.0/ref/models/options/#django.db.models.Options.managed)

[inspectdb - documentación](https://docs.djangoproject.com/en/4.0/ref/django-admin/#django-admin-inspectdb)

3) Luego instalar tablas core Django, ejecutando el comando *migrate*, siempre y cuando el usuario de la base de datos tenga permisos necesarios para crear nuevas tablas o modificar, de lo contrario dará error.

```shell
    python manage.py migrate
```

[databases_legacy - documentación](https://docs.djangoproject.com/en/4.0/howto/legacy-databases/)

[MySQL-notes - Django](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes)
