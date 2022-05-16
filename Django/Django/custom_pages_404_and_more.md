# Usar planillas personalizadas de errores.

[Source stackoverflow](https://stackoverflow.com/a/64527996/17234863)

[pythoncircle](https://pythoncircle.com/post/564/displaying-custom-404-error-page-not-found-page-in-django-20/)

[Documentacion customizing-error-views](https://docs.djangoproject.com/en/4.0/topics/http/views/#customizing-error-views)

[Documentacion django.conf.urls](https://docs.djangoproject.com/en/4.0/ref/urls/#django.conf.urls.handler404)





## urls.py

Fichero `uls.py` principal del proyecto, no de las aplicaciones dentro de este.

```python
from django.contrib import admin
from django.urls import path, include, re_path


from django.conf.urls import handler404, handler500
handler404 = 'app.views.error_404_view'
handler500 = 'app.views.error_500_view'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
]
```


## views.py

Fichero `views.py` de la aplicación dentro del proyecto.

```python
from django.shortcuts import render

[...]

def error_404_view(request, exception):
    return render(request, 'app/404.html')

def error_500_view(request):
    return render(request, 'app/500.html')

```
