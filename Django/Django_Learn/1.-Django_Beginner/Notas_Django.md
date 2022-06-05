# Django




## Dinamic Web Applications


## Protocolo HTTP


| Codigos estado | Descripcion |
|-|-
| 200 | OK |
| 301 | Moved Permanently |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

\pagebreak

## Instalacion
Para tener un entorno ordenado, se recomienda crear un entorno virtual que pemitira instalar paquetes separados del sistema principal:

```bash
$ pip install virtualenv
```

Crear el directorio contenedor del proyecto y nos movemos dentro:

```bash
$ mkdir [proyecto_nombre]
$ cd [proyecto_nombre]
```

Crear entorno virtual para el proyecto:

```bash
$ python -m venv [NOMBRE_ENTORNO]
```


Activar y desactivar entorno virtual:

```bash   
$ source virtuale/bin/activate
$ deactivate
```

Como el entorno virtual no contiene ningun paquete instalado, trae solo los por defecto Python, dentro del entorno instalamos los paquetes que necesitamos:

```bash
$ pip install django
```

\pagebreak


## Creando proyecto nuevo

Luego ejecutamos el siguiente comando para crear el proyecto Django que necesitemos:

```bash
$ django-admin startproject [Proyecto_nombre]
```

Con esto Django creará algunos ficheros iniciales automáticamente, para empezar a construir la aplicacion web.



Los ficheros creados corresponden a:

    Proyecto_Django/
    ├── manage.py
    └── Proyecto_Django
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py


`manage.py` = comandos administrativos para el proyecto django.

`urls.py` = fichero de URLs para del proyecto y las aplicaciones.

`Proyecto_Django` = directorio del proyecto principal

`asgi.py` = ""

`settings.py` = fichero de opciones del servidor.

`urls.py` = fichero URLs del proyecto, incluye las URLs de aplicaciones del proyecto.

`wsgi.py` = ""



Para ejecutar el servidor Django, se necesita el comando:

```bash
$ python manage.py runserver
```

Para ingresar al servidor se debe ingresar [http://127.0.0.1:8000/](http://127.0.0.1:8000/), localmente.


Un solo proyecto puede tener múltiples aplicaciones. Django viene pre-cargado con la habilidad para tomar un proyecto y dividirlo en múltiples aplicaciones distintas.


\pagebreak

## Crear aplicación del proyecto

Para crear una aplicacion dentro del proyecto, se ejecuta el comando:

```bash
$ python manage.py startapp [Nombre_APPlicacion]
```

Django creará un directorio con ficheros necesarios para la aplicacion creada:

    Nombre_APPlicacion/
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py


`admin.py` = fichero de administración mediante modelos de base de datos, ruta `http://127.0.0.1:8000/admin`, se debe crear un super usuario antes.

`apps.py` = configuración de aplicación, esta se usará por el fichero "settings.py" del proyecto principal.

`migrations` = directorio donde se registran los cambios de los modelos de base de datos de `models.py`.

`models.py` = fichero donde se escriben los modelos de base de datos que usará la aplicación, se debe migrar para aplicar los cambios hechos.

`tests.py` = fichero donde se escriben las pruebas para la aplicación, este pueden ser pruebas a las páginas `SimpleTestCase`, o a la base de datos `TestCase`.

`views.py` = fichero donde se escribe la lógica de las vistas de las rutas y designación de las planillas HTML a mostrar, o respuestas JSON (API).

\pagebreak


## Aplicacion y Django settings
Despues, se debe ir a modificar el fichero `settings.py` del proyecto y agregar cada aplicacion a este fichero.

```bash
$ cd [Proyecto_nombre]
$ vim settings.py
```

En el editor de `settings.py`, agregar el/los nombre/s de la/s aplicacion/es:

La variable `SECRET_KEY` es recomendable cambiarla por un string alfanumerico con caracteres, lo más random posible.

En #Applications definition, modificar la lista `INSTALLED_APPS` agregando el/los nombre/s de el/las aplicacion/es.

```python
[...]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = [NUEVO_STRING_SEGURO]


# Application definition

INSTALLED_APPS = [
    "Nombre_APPlicacion",    # <----- nueva aplicación
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

[...]
```


Editamos `urls.py` del proyecto para enlazar a las rutas de la aplicacion.

```bash
$ vim urls.py
```


```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
]
```

Luego de eso, volvemos al directorio de la aplicacion creada anteriormente.

```bash
$ cd [Nombre_APPlicacion]
```

\pagebreak

## Respuesta estáticas y con variables

Se pueden tener URLs y views estáticas (sin variables) o dinámicas (con variables), dependiendo de lo que se necesite hacer, la configuración de la aplicaiciones.

### Respuestas estáticas
Se puede crear views con información html estática (no varian) y con variables para ello dentro de la aplicacion editamos el fichero `views.py`, para agregar funcionalidad a la aplicacion:

```bash
$ vim views.py
```

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def foobar(request):
    return HttpResponse("Hello, foobar!!")

```

En las funciones "index" e "foobar" retornarán una respuesta HTTP con codigo html generado por Django.
Para que se pueda visualizar, se tiene que crear dentro de la aplicación creada `[Nombre_APPlicacion]`, este fichero se llamará `urls.py` y contendrá una lista `urlpatterns` con clase `path` con valor tupla de nombre de rutas, las funciones `views` creadas, y el nombre de esas rutas.

```bash
$ vim urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("foobar", views.foobar, name="foobar"),
        ]

```


Listo eso, se dirige a la carpeta contenedora del proyecto, `Proyecto_nombre`, y se tiene que editar `urls.py`.

```bash
$ cd Proyecto_nombre
$ vim urls.py
```

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path("foobar", include("hello.urls")),

]
```

`hello/` es la ruta de la aplicacion creada. en el buscador seria: 127.0.0.1:8000/hello.
Los valores de `path` son todas las rutas y valores `include` con los datos de la aplicacion y las rutas , `Nombre_APPlicacion.urls`.


Luego comprobamos el funcionamiento, ejecutamos el servidor:

```bash
$ python manage.py runserver
```

Ahora las rutas cambiaron, tenemos rutas: 127.0.0.1:8000/hello/, 127.0.0.1:8000/hello/foobar. Cualquier otra ruta dará error 404 porque no se ha configurado ninguna otra.


### Respuestas variables
Para generar respuestas con variables necesitamos editar nuevamente el fichero `views.py` de la aplicacion, agregando una nueva funcion, y una variable, retornando una respuesta con variable.

```bash
$ vim Nombre_APPlicacion/views.py
```

```python
[...]
def saludo(request, nombre):
    return HttpResponse(f"Hello, {nombre.capitalize()}")

[...]
```


Luego editamos `urls.py` de la aplicacion.

```bash
$ vim Nombre_APPlicacion/urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("foobar", views.foobar, name="foobar"),
        path("<str:nombre>", views.saludo, name="saludo"),
        ]
```

Donde **path("<str:nombre>", views.saludo, name="saludo")**, `"<str:nombre>"` donde el nombre de la variable debe ser igual en "views.py" como en "urls.py".


Falta editar el fichero "urls.py" del directorio del Proyecto.

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path("foobar", include("hello.urls")),
    path("saludo", include("hello.urls")),

]
```

\pagebreak


## Templates
Para utilizar ficheros con diseño de planillas (templates) en la aplicacion se debe crear un directorio llamado `templates`, dentro de este directorio se guardarán todas las planillas de las paginas que se requieran.

```bash
$ mkdir -p Nombre_APPlicacion/templates/hello
```

Para crear una planilla que usará la aplicacion, debemos crearla dentro del directorio "templates":

```bash
$ vim Nombre_APPlicacion/templates/hello/index.html
```

En donde, "hello" es el nombre de la alplicacion creada y dentro de esta tendrá todos los ficheros web que se requieran. **Esto es una buena practica y es recomendada. Hazlo así.**

Agregamos el codigo html que sea necesario y guardamos.



Ahora, para usar las planillas dentro de la aplicacion, se debe modificar el fichero `views.py` de la aplicacion.

```bash
$ vim Nombre_APPlicacion/views.py
```

```python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "Nombre_APPlicacion/index.html")

[...]

```

Donde los valores de `render` son "request", y el nombre del directorio y la planilla que se usara, en este caso "Nombre_APPlicacion/index.html".


Todo esto generará ficheros html estáticos, no cambiaran su contenido dinamicamente a no ser que se editen manualmente, para evitar tener que crear ficheros .html para cada uno de los requerimientos, se puede crear planillas dinamicas.


### Planillas dinámicas

Dentro de la aplicacion editamos `views.py`, la funcion "saludo" esta tomará tres parametros, "request" y "nombre" y un diccionario de todas las variables que se requieran.

```bash
$ vim Nombre_APPlicacion/views.py
```

```python
[...]

def saludo(request, nombre):
    return render(request,"hello/saludo.html", {
        "name": nombre.capitalize()
        })

```

El diccionario contendrá todas las variables que usará "templates/hello/saludo.html".


Crear y editar "saludo.html" del directorio "templates/hello" de la aplicacion.

```bash
$ vim templates/hello/saludo.html
```

```python
<!DOCTYPE html>
<html lang="es">
        <head>
                <title>Welcome - template/hello/</title>
        </head>
        <body>
                <h1>Hello, {{ name }} </h1>
        </body>
</html>
```

Todas las variables que se usen deben ir entre **{{ variable }}** para que el lenguaje de Django lo pueda usar, el nombre de variable debe coincidir con el nombre de variable que se usó en `views.py`.


Comprobar que la rutas esten correctas en `urls.py` de la aplicacion.

```python
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("foobar", views.foobar, name="foobar"),
        path("<str:nombre>", views.saludo, name="saludo"),
        ]

```


Entonces, `urls.py` (ruta) toma un dato string, usa la funcion de `views.py` y muestra (render) la planilla mostrando en el buscador.


### Lógica en Templates

Para poder explicar mejor, crearemos una nueva aplicación que nos informará si el día de hoy es año nuevo o no.

Para ello, vamos a iniciar una nueva aplicación dentro del directorio del proyecto "Proyecto_nombre":

```bash
$ python manage.py startapp newyear
```

Editamos, incluimos `newyear` a `settings.py`, y creamos la ruta en `urls.py`, del directorio del proyecto.

```bash
$ vim Proyecto_nombre/settings.py
```

```python
[...]

# enlaces a aplicaciones

INSTALLED_APPS = [
    "hello",
    "newyear",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

[...]
```

```bash
$ vim Proyecto_nombre/urls.py
```

```python
    from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path("foobar", include("hello.urls")),
    path("saludo", include("hello.urls")),
    path("newyear/", include("newyear.urls")),
]
```


Ahora, creamos en el directorio de la aplicacion `newyear` el fichero de las rutas `urls.py`

```bash
$ vim newyear/urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        ]                
```

La el valor de ruta `""` quiere decir que al momento de ingresar en el navegador "127.0.0.1:8000" usará esa ruta, "index".



Editamos el fichero `views.py` de "newyear". Acá es donde escribimos la **lógica** que nos dirá si hoy es año nuevo o no y entregaremos la planilla corespondiente.

```bash
$ vim newyear/views.py
```

```python
from django.shortcuts import render
from datetime import datetime as date


# Create your views here.
def index(request):
    fecha = str(date.now()).split()[0].split("-")

    return render(request, "newyear/index.html", {
       "newyear": int(fecha[2]) == 1 and int(fecha[1]) == 1
      })
```

La variable se ubicó dentro de la funcion index y la lógica que se usó fue por medio de booleanos dentro del diccionario con llave "newyear".

\pagebreak


## Sentencias y Condicionales

[if/elif/else - Template](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatetag-if)

En las planillas que utiliza "views" para cada ruta, se puede escribir lógica utilizando lenguaje Jinja2.

### IF
Sintaxis ejemplo:

```python
  {% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
  {% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
  {% else %}
    No athletes.
  {% endif %}
```

Ahora, hay que crear el directorio `templates` de "newyear" para ahí guardar los ficheros web.

```bash
$ mkdir -p newyear/templates/newyear
```

Crear la planilla en "templates/newyear/"

```bash
$ vim newyear/templates/newyear/index.html
```

```python
<!DOCTYPE html>
 <html lang="en">
        <head>
                <title>Is New Year?</title>
        </head>
        <body>
                {% if newyear %}
                        <h1>YES</h1>
                {% else %}
                        <h1>NO</h1>
                {% endif %}
        </body>
</html>
```

En Django la lógica está se debe escribir entre **{% if %}**, **{% elif %}**, **{% else %}** y se cierra con **{% endif %}**.
Para utilizar variables se utiliza **{{ variable }}**.

\pagebreak


###  Bucles for

Sintaxis con ejemplo:

```python
{% for key, value in data.items %}
  {{ key }}: {{ value }}
{% endfor %}
```

Algunos ejemplos:

```python
<ul>
  {% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
  {% endfor %}
</ul>
```

```python
<ul>
  {% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
  {% empty %}
    <li>Sorry, no athletes in this list.</li>
  {% endfor %}
</ul>
```

El uso de **{% empty %}** es para cuando no existen items dentro del ciclo for (vacio) y se puede terminar sin errores.
Crearemos una lista no ordenada con varios items y que se despliegue automaticamente usando planillas y ciclo for.


Crearemos una aplicacion nueva llamada "tasks".

```bash
$ python manage.py startapp tasks
```


Editamos `settings.py` y `urls.py` del directorio del proyecto.

```bash
$ vim Proyecto_nombre/settings.py
```

```python
[...]
INSTALLED_APPS = [
    "hello",
    "newyear",
    "tasks",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
[...]
```

```bash
$ vim Proyecto_nombre/urls.py
```

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", include("hello.urls")),
    path("foobar", include("hello.urls")),
    path("saludo", include("hello.urls")),
    path("newyear/", include("newyear.urls")),
    path("tasks/", include("tasks.urls")),

]
```


Cambiamos de directorio a `tasks` y editamos fichero `views.py` y `urls.py`

```bash
$ vim tasks/views.py
```

```python
from django.shortcuts import render

tareas = ["uno", "dos", "tres"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tareas
        })
```

Acá la lista de tareas se usará una lista de items y se enviarán a la planilla usando un diccionario con llave "tasks".

```bash
$ vim tasks/urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index")
        ]
```


Crear dentro de directorio de app "tasks", los directorios `templates` y "tasks" que contendrá el fichero index.html.
```bash
$ mkdir -p tasks/templates/tasks
```


Crear y editar planilla index.html de tasks.
```bash
$ vim tasks/templates/tasks/index.html
```

```python
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <ul>
            {% for item in tasks %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

---

Recordar:

`{% for item in tasks %}` <---- inicio de bucle

`<li>{{ item }}</li>`     <---- operación a realizar

`{% endfor %}`            <---- fin de bucle

---


Acá se utiliza el ciclo for agregar a la lista no ordenada , &lt;ul&gt;, &lt;ul&gt;, lista los items de la lista "tasks" usando marcadores &lt;li&gt;, &lt;li&gt; para cada item.

\pagebreak


## Herencia de planillas

Crear y escribir cada HTML que tenga items en comun se vuelve tedioso y repititivo, Django permite usar herencia de planillas para que se puedan usar una y otra vez evitando perder consistencia de la pagina web ,cambio de diseño, estilo, etc. Se le denomina herencia de planilla.

Usando:

```
{% block NOMBRE_BLOQUE %}
  Contenido variable
{% endblock %}
```

Abre y cierra el bloque, este bloque cambiará dependiendo de los requisitos, pero conservará el mismo diseño para las las paginas, ya sea diseño de la pagina web, el estilo.


Poniendo en práctica, crearemos una planilla usando la aplicacion "tasks".


Creamos la planilla en "templates" de "tasks":

```bash
$ vim tasks/templates/tasks/planilla_herencia.html
```

```python
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        {% block cuerpo %}
        {% endblock %}
    </body>
</html>
```


Ahora en la apliacion "tasks" borraremos el contenido del fichero "index.html" dejando solamente el bloque que necesitemos, en este caso los datos de la lista no ordenada.

```bash
$ vim tasks/templates/tasks/index.html
```

```python
{% extends "tasks/planilla_herencia.html" %}

{% block cuerpo %}
    <h1>Tasks</h1>
    <ul>
        {% for item in tasks %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

Ahora al momento de cargar la pagina web "tasks" usará la planilla de "planilla_herencia.html" y reemplazará los valores dentro del bloque con lo escrito.

\pagebreak


##  Formularios

[Working with forms](https://docs.djangoproject.com/en/3.2/topics/forms/)


Formularios sirven para que el usario envíe informacion al servidor y podamos usar dicha informacion.

Trabajaremos con la aplicacion `tasks` para agregar una nueva capacidad de enviar datos ingresados por el usuario y poder agregar nuevas tareas.


Crear una nueva ruta, "add" para "tasks":

```bash
$ vim tasks/views.py
```

```python
[...]
def add(request):
    return render(request, "tasks/add.html")

[...]
```

```bash
$ vim tasks/urls.py
```

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
    ]

```

Aprovechando la planilla creada en "herencia", craremos el fichero "add.html":

```bash
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}

{% block cuerpo %}
<h1>Add your tasks</h1>
    <form>  
        <input type="text" name="task">
        <input type="submit">
    </form>
{% endblock %}
```


Ahora la cuestiones, ¿cómo conectamos las dos paginas web sin necesidad de escribir la direcciones cada vez?, agregamos un link, y usaremos una nueva funcion de Django:
**{% url 'NOMBRE_URL' variable=dato %}**

Esta función toma los valores "name" del fichero `urls.py` que se escribieron permitiendo la creacion de links facilmente sin necesidad de escribir la ruta evitando posible errores debido a cambios de rutas de esos ficheros.


Modificaremos "index.html" de "tasks"

```bash
$ vim tasks/templates/tasks/index.html
```

```python
{% extends "tasks/planilla_herencia.html" %}

{% block cuerpo %}
    <h1>Tasks</h1>
    <ul>
        {% for item in tasks %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add'  %}">Add a New Tasks</a>
{% endblock %}

```

Ahora usamos las variables de `name` de `urls.py` para crear enlaces.

Hacer lo mismo en el fichero `add.html` para enlazar a la "index.html" de tasks.

```bash
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}

{% block cuerpo %}
    <h1>Tasks</h1>
    <ul>
        {% for item in tasks %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add'  %}">Add a New Tasks</a>
{% endblock %}
```

\pagebreak


## Conflictos de colisión

Sucede cuando en el fichero **`urls.py`** de una aplicacion tiene el mismo valor para la variable **`name`**, para resolver este problema se debe agregar una variable llamada `app_name`

```bash
$ vim tasks/urls.py
```

```python
from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
        path("", views.index, name="index"),
        path("add", views.add, name="add")
        ]
```


Ahora editamos `add.html`

```
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}


{% block cuerpo %}
    <h1>Add your tasks</h1>
    <form>
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```


Al declarar **'tasks:index'**, Django usara las rutas de la variable `app_name`, en simple se le dice a Django que use las rutas de "url.py" de la aplicacion "tasks".


Modificamos "index.html" de tasks.

```bash
$ vim tasks/templates/tasks/index.html
```

```python
{% extends "tasks/planilla_herencia.html" %}

{% block cuerpo %}
    <h1>Tasks</h1>
    <ul>
        {% for item in tasks %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'tasks:add'  %}">Add a New Tasks</a>
{% endblock %}
```

**'tasks:add'** Django usará las rutas de la aplicación "tasks" descrita por la variable `app_name` de `urls.py`.

\pagebreak


## Metodo POST y GET

[Get y POST en DJANGO](https://docs.djangoproject.com/en/3.2/ref/request-response/)

Hasta ahora la aplicacion **tasks** no agrega las tareas enviadas, solamente hemos echo enlaces entre las paginas index y add, para agregar necesitamos que el formulario de "add" envie los datos por medio de metodo `POST` y que index reciba esos datos por metodo `GET`.

```bash
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}


{% block cuerpo %}
    <h1>Add your tasks</h1>
    <form action="{% url 'tasks:add' %}" method="POST">
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```



## Seguridad en formularios por el lado del cliente

Para evitar posibles ataques, necesitamos validar los datos enviados, el CSRF (del inglés Cross-site request forgery o falsificación de petición en sitios cruzados) es un tipo de exploit malicioso de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía. Esta vulnerabilidad es conocida también por otros nombres como XSRF, enlace hostil, ataque de un clic, secuestro de sesión, y ataque automático.

Validación de CSRF permitirá agregar los datos de manera segura y confiable, este se realizará por medio de `tokens` únicos para cada usuario u operaciones POST/GET, si no coinciden esta informacion se rechazará.

Django tiene validacion CSRF por defecto activado, tambien se puede agregar un paquete llamado `Django Middleware`, permite intervenir la respuesta de una peticion Django.

En el fichero **`settings.py`** del directorio del proyecto

```python
[..]

MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

[..]
```

Entonces, en el fichero `add.html`, en el formulario necesitamos agregar un "token" para que Django pueda autenticar y validarlo, para ello debemos agregar **`{% csrf_token %}`**:


```bash
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}


{% block cuerpo %}
    <h1>Add your tasks</h1>
    <form action="{% url 'tasks:add' %}" method="POST">
        {% csrf_token %}
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```


Al usar **`{% csrf_token %}`**, Django generará un "input" oculto con atributo name y value con un string largo que es el token.



## Seguridad en formularios por el lado del servidor
Tenemos que asegurarnos que los datos enviados sean validos, y por el lado del servidor, los datos se pueden obtener y comparar mediante uso de codigo o patrones usando modulo "re" agregando condicionales si se cumple o no los requisitos.


Modificamos "views.py" de aplicacion "tasks":

```python
from django import forms
from django.shortcuts import render

tareas = ["uno", "dos", "tres"]

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Tasks ")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
   return render(request, "tasks/index.html", {
       "tasks": tareas
       })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            tareas.append(tasks)
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
        })
```


Creamos una clase "NewTaskForm" que nos permitira crear formularios más facilmente y heredarlos a los ficheros que los usen pasandolo como parametro en un diccionario.
"NewTaskForm" agrega una etiqueta "label", agrega atributo "priority".

La funcion "add", agrega la seguridad de validacion de formulario por parte del servidor.

* **request.method** entrega el metodo usado en forma de string.

* **form.is_valid()** comprueba si es valida la informacion comprobando los tokens.

* **form.cleaned_data** entrega un diccionario con los dantos enviados por metodo POST.

Si se cumple la sentencia se agrega a la lista "tareas" que será agregado y se verá en "index.html". De no cumplirse se retorna el formulario "tasks/add.html" con el bloque "{form}" que es una instancia del objeto NewTaskForm(). Esto se usará en el bloque {{ form }} de add.html.


Modificamos "add.html":

```bash
$ vim tasks/templates/tasks/add.html
```

```python
{% extends "tasks/planilla_herencia.html" %}


{% block cuerpo %}
    <h1>Add your tasks</h1>
    <form action="{% url 'tasks:add' %}" method="POST">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```


Ahora que existe verificación por parte del servidor y cliente, podemos agregar una funcion que nos redireccione a index cada vez que enviemos un formulario.


Editamos "views.py" de "tasks":

```bash
$ vim tasks/views.py
```

```python
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


tareas = []

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Tasks ")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
   return render(request, "tasks/index.html", {
       "tasks": tareas
       })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            tareas.append(tasks)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
        })
```

* **HttpResponseRedirect** nos redireccionará a la ruta que le entregamos.

* **reverse** usa las rutas de `urls.py` en formato `nombre_app:ruta_nombre`.

Ahora podemos dejar vacía la lista de "tareas" para que pueda ser llenada con cada envío de formulario valido.

\pagebreak


## Sesiones

[Autenticacion](https://docs.djangoproject.com/en/3.2/topics/auth/default/)

[How to use Session](https://docs.djangoproject.com/en/3.2/topics/http/sessions/)


Hasta ahora, podemos enviar y visualizar los datos en la aplicacion "tasks", pero tenemos un gran problema, cualquier persona puede ver la misma lista de tareas, necesitamos separar cada usuario con sus tareas, para ello necesitamos crear sesiones que guarden los datos de manera segura.


Hay un problema, no tenemos acceso porque no existen las "tablas" de base de datos, podemos crear una usando Django o crear y usar una base de datos independiente, veremos esto mas tarde.

Por ahora Django nos permite crear una pequeña base de datos que nos servirá para la aplicacion usando el comando:

```bash
$ python manage.py migrate [nombre_aplicación]
```

Al no especificar la aplicación, se realizará una migración total, esto es malo para seguir los cambios en los registros. Es recomendable migrar en una aplicación específica si se necesita, y en algunos casos realizar una migración completa.

Más adelante aprenderemos a crear base de datos, tablas y almacenaremos datos para usarlos con Django.

Modificaremos "views.py" para que no se crucen las tareas para diferentes usarios (sessiones):

```bash
$ vim tasks/views.py
```

```python
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Tasks ")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            tareas = form.cleaned_data["tasks"]
            request.session["tasks"] += [tareas]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
        })
```

Eliminamos la lista "tareas".
Agregamos condicional "tasks" a "request.session". Recordar que "request" es un diccionario.
* "tasks": request.session["tasks"] = enviamos los valores del formulario que se uso en la session para que sea agregado a index.html.
* request.session["tasks"] += [tareas] = agregamos los datos obtenidos del formulario enviados en la sesion y lo agregamos a request.session["tasks"].


Las sesiones están determinadas por cookies, son huellas pequeñas que ayudan a los navegadores a entregar informacion a Django para decirles quienes son y Django sepa que información mostrar.

\pagebreak


## Ficheros Estaticos

Django permite manejar ficheros estáticos como estilos "ficheros CSS", imagenes, ficheros JavaScript, permitiendo un rápido acceso y congruencia en las paginas web para el caso de ".css".
En proyectos grandes, estos ficheros están en servidores CDN (Content Delivery Network).

Por convencion el directorio `static` contiene todos los ficheros estáticos de la aplicacion que se está trabando.

El siguiente item usaremos estilo para una pagina web, el fichero CSS será estático y lo cargará mediante uso de lenguaje Django en el fichero `index.html` de la aplicacion `newyear`.


### Lidiando con Estilos - CSS

Retomando la aplicación `newyear`, daremos estilo a la pagina para que se vea un poco mejor, para ello, se debe crear el directorio `static`.

```bash
$ mkdir newyear/static
```


Agreguemos estilo a la aplicacion "newyear".

```bash
$ mkdir newyear/static/newyear
$ vim newyear/static/newyear/styles.css
```

```css
h1 {
    font-family: sans-serif;
    font-size: 90px;
    text-align: center;
}
```


Editamos `index.html` de la aplicacion newyear.

```bash
$ vim  newyear/templates/newyear/index.html
```

```python
{% load static %}


<!DOCTYPE html>
 <html lang="en">
        <head>
                <title>Is New Year?</title>
                <link href="{% static 'newyear/styles.css'  %}" rel="stylesheet">
        </head>
        <body>
                {% if newyear %}
                        <h1>YES</h1>
                {% else %}
                        <h1>NO</h1>
                {% endif %}
        </body>
</html>
```

* **`{% load static %}`** = Django cargará los ficheros de directorio "static".

* **`{% static 'newyear/styles.css'  %}`** = es la variable en lenguaje Django para decir explicitamente que .css usar, ubicado en newyear/statics/newyear/style.css.


Similarmente se puede trabajar con imágenes, iconos, para las paginas web
