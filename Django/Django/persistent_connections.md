# Conexiones persistentes

> [CONN_MAX_AGE - doc](https://docs.djangoproject.com/en/4.0/ref/settings/#conn-max-age)

Tiempo de vida de una conexión a base de datos, como un número entero de segundos.

Usar **0** para cerrar la conexión al final de cada petición, comportamiento por defecto, y **None** para conexiones persistentes ilimitadas.

## Ejemplo

* *settings.py*

```python
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
```
