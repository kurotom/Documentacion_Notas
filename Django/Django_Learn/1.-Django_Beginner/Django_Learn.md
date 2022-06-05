# Django

Es un framework libre, codigo abierto escrito en Python, es popular entre programadores principiantes y avanzados.

Es robusto para crear sitios web a nivel mundial, como Instagram, Pinterest, Bitbucket, Disqus, pero tambien flexible para ser una buena elección para startups y para proyectos personales.

Django es una colección de herramientas modular que abstrae mucho de las tareas dificultosa y repetitivas inherente del desarrollo web.
Django hereda "baterías incluidas" de Python aprovechando e incluyendo soporte fuera de la caja para tareas comunes en desarrollo web.

* Autenticación de usuario.
* Planillas, rutas, y views.
* Interface admin.
* Seguridad robusta.
* Soporte backend para múltiples bases de datos.
* Mucho más.

Se mantiene bajo desarrollo activo contínuo y tiene comportamiento de liberación de nuevas versiones continuamente. Además de contar de documentación abundante y una comunidad grande que mejora las características y seguridad, además de crear nuevas características.

Crear aplicaciones modernas, robustas con mínima cantidad de código.


# 1 - Preparando el entorno de desarrollo

Instalar Python, en Fedora:

```bash
$ sudo dnf install python
```

Instalar paquetes pip

```bash
$ python -m ensurepip --upgrade

```

Actualizar pip

```bash
$ python -m pip install --upgrade pip
```

[Documentación Python - Pip install](https://docs.python.org/3/library/ensurepip.html?highlight=pip#module-ensurepip)


Instalar virtualenv

```bash
$ pip install virtualenv
```


Crear el directorio contenedor del proyecto y nos movemos dentro:

```bash
$ mkdir [proyecto_nombre]
$ cd [proyecto_nombre]
```

Sintaxis para crear entorno virtual para el proyecto:

```bash
$ python -m venv [NOMBRE_ENTORNO]
```

Crear directorio entorno virtual, activar y desactivar entorno virtual:

```bash
$ python -m venv DirVenv
$ source DirVenv/bin/activate
$ deactivate
```

Estando dentro del entorno virtual, actualizamos "pip" e instalamos "Django":

```bash
$ source Directorio_Virtual/bin/activate
(DirVenv) python -m pip install --upgrade pip
(DirVenv) pip install django
```


## Empezar un nuevo proyecto Django

Para construir los cimientos del proyecto y futuras aplicaciones se deben crear usando el siguiente comando:

```bash
(DirVenv) $ django-admin startproject test_project .
```

Donde:
	- "startproject" indica a Django para crear un proyecto.
	- "test_project" es el nombre del proyecto, se creará directorios y ficheros necesarios.
	- "." Opcional, es el parámetro de ruta, en este caso, indica en la ruta actual de trabajo, por defecto se creará en la ruta actual de trabajo.


Se creará una estructura similar a la siguiente:

```
test_project/
├── manage.py
└── test_project
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


* manage.py:  permite el uso de comandos para tareas administrativas.
* test_project/:  directorio del proyecto creado.
* urls.py:  ficheros de rutas del proyecto.
* asgi.py, wsgi.py:  ficheros para el estándar Python emergente para aplicaciones y servidores web asincrónicos.



Para iniciar del proyecto Django se utiliza el comando, por ahora mostrará una aplicación por defecto para entregarnos una prueba exitosa.

Se debe ingresar al directorio "test_project" y ejecutar el comando:

```bash
(DirVenv) $ cd test_project
(DirVenv) $ python manage.py runserver
```


Para terminar el proceso de ejecución, desde la terminal se utiliza las teclas "Ctrl + c".


## Instalar Git

[Git](https://git-scm.com/) es parte fundamental del desarrollo de software moderno. Este es un [sistema de control de version](https://en.wikipedia.org/wiki/Version_control) que registra y sigue cambios en ficheros, permite la colaboración con otros desarrolladores, revertir cambios.

```bash
$ sudo dnf install git
```

### Configurando Git

```bash
$ git config --global user.name "UserName_Git"
$ git config --global user.email "username@emailgit.com"
```

Esta configuración es básica, se puede agregar otros parámetros, también se puede modificar.


## Editor de texto

Se puede usar Atom, vim, vi, Emacs, nano, cualquier editor de texto que se quiera.

En este caso se usará Atom

```bash
$ sudo dnf install atom
```


# 2 - Aplicación "Hello World"

Primera aplicación Django y trabajar con git para controlar el código.

Creamos un proyecto nuevo "helloworld"
```bash
$ cd test_project
$ source bin/activate
(DirVenv) $ python manage.py startproject helloworld_project
(DirVenv) $ cd helloworld_project
(DirVenv) $
(DirVenv) $ python manage.py startapp pages
```

Creando un nuevo conjunto de directorios y ficheros en el directorio "pages", dejando una estructura similar a:

```bash
pages/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```


* admin.py:  fichero de configuración incorporado en aplicación Django Admin.
* apps.py:  fichero de configuración para la aplicación en sí.
* migrations/:  mantiene cualquier cambio del fichero *models.py* de la base de datos y mantiene sincronizado *models.py*.
* models.py:  fichero en donde se definen modelos de base de datos, Django automáticamente traduce en tablas de base de datos.
* tests.py:  fichero especifica pruebas para la aplicación.
* views.py:  fichero en donde manejaremos la lógica request/response para la aplicación web.


## Registrando una aplicación

En Django se tiene que registrar las aplicaciones creadas para que funcionar, el fichero **settings.py** que está en el directorio principal del proyecto, en este caso, está en el directorio "helloworld_project".

```bash
(DirVenv) $ vim helloworld_project/settings.py
[ ... ]

# Application definition

INSTALLED_APPS = [
    'pages',                      #  nombre directorio de la app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

[ ... ]
```

[Documentación INSTALLED_APPS](https://docs.djangoproject.com/en/4.0/ref/settings/#installed-apps)

Con esto, se pueden acceder a los recursos como planillas, ficheros estáticos, administración, modelos, entre otros.


Además, se debe registrar la ruta a cada aplicación en el fichero **urls.py** del proyecto (helloworld_project) que apunte a la/s nueva/s aplicación/es.

```bash
(DirVenv) $ vim helloworld_project/settings.py
[ ... ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls")),
]

[ ... ]
```



## Views y URLConf

En Django, *views.py* determina qué se mostrará en una página mientras que *urls.py* determina dónde el contenido está, la ruta.

Si el fichero *urls.py* no existe, se debe crear y configurar como se requiera.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```


Donde se importa "path" de django, se configura la lista "urlpatterns" con las rutas usando "path" en donde:

1) el primer campo es el "nombre de ruta"

2) el segundo es "función views" donde esta función se escribe en el fichero "views.py" de la aplicación.

3) tercer campo se establece el "nombre" de la ruta.



Cuando un usuario realiza una petición, URLConf usa expresiones regulares para mapear la petición a la función apropiada que retornará la información correcta.

La línea *"from . import views"*, indica que desde la ruta actual se importe el fichero completo "views", este será usado en cada "path" indicando la función a usar por dicha ruta.



El ciclo request/response:

```
URL  -->  View  -->  Model  -->  Template
```


Ahora que tenemos una ruta, se debe configurar una función "views" para la ruta escrita, en este caso, necesitamos una función "index".

```python
(DirVenv) $ cat pages/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')
```


"HttpResponse" del objeto "http" del módulo "django", sirve para entregar una versión simple html, entregando un string como mensaje de la página.


Para poder crear páginas personalizadas creadas manualmente, se debe usar "render" del objeto "shortcuts" del módulo "django".


```python
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
```


Se debe crear el directorio *templates* dentro de la aplicación, dentro de este se debe crear un directorio con el nombre de la aplicación, *pages*, y es en este directorio en donde se guardan las planillas html.

```bash
(DirVenv) $ mkdir -p templates/pages/
(DirVenv) $ vim templates/pages/index.html
<html>
	<body>
		Hello World!
		Primera Página.
	</body>
</html>
```


Ahora, se puede ejecutar o arrancar el servidor.

```bash
(DirVenv) $ python manage.py runserver
```


## Enviando el código a Git

Para empezar a usar git se necesita iniciar git.
Se debe estar en el directorio principal del proyecto.

```bash
(DirVenv) $ git init
```

Agregamos los ficheros, confirmamos y enviamos.

```bash
(DirVenv) $ git add .
(DirVenv) $ git add commit -m "Primer comentario de app"
(DirVenv) $ git push
```

Es posible agregar otro sistema de versiones como "Bitbucket", en ese caso se debe crear una cuenta, crear un repositorio nuevo, y copiar su dirección.

En la terminal se debe usar.

```bash
(DirVenv) $ git remote add origin git@bitbucket.org:<USER>/hello-world.git
(DirVenv) $ git push -u origin master
```


Para revisar el estado se debe usar el comando:

```bash
(DirVenv) $ git status
```


Si todo resulta bien, se tendrá el código en un repositorio, en este caso en "Bitbucket", disponible para descargar, seguir, actualizar los cambios en los ficheros.



# 3 -- Aplicación Pages

Se construirá una aplicación "Pages" que tendrá una página principal y una sobre la página. Ahora se se utilizará planillas y "views" basados en clases para crear aplicaciones más complejas.

## Configuración inicial

* Crear un nuevo directorio para el código fuente.
* Iniciar un nuevo entorno virtual, e instalar Django.
* Crear un nuevo proyecto Django.
* Crear una aplicación nueva "pages".
* Actualizar "settings.py".


```bash
$ mkdir pages_projects
$ cd pages_projects
$ python -m venv ex3
$ source bin/activate
(ex3) $ pip install django
(ex3) $ django-admin startproject pages_project .
(ex3) $ python manage.py startapp pages
```


Actualizar "settings.py" del proyecto "pages_project".

'pages_project/settings.py'
```python
(ex3) $ vim pages_project/settings.py
[ ... ]
INSTALLED_APPS = [
	'pages', 		# nueva app
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

[ ... ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],			#  Agregar el directorio "templates" de la aplicación
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

[ ... ]
```


pages_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```


Crear fichero "urls.py" de la aplicación "pages".

pages/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
]
```


Crear una función "views" con el nombre "index" para manejar las peticiones/respuestas.

pages/views.py
```python
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

```



## Templates

Django utiliza planillas, que son ficheros HTML individuales que pueden ser servidos por una "view" para una página web especificada por una URL.

Siguiendo el patrón:

```
URL  -->  View  -->  Model  -->  Template
```


El orden de ubicación de las planillas o "templates" dentro de una aplicación Django.

```
└── pages
    └── templates
        └── pages
            └── home.html
```


El directorio "templates", "pages" se deben crear manualmente, "templates" es obligatorio" y "pages" debe tener el mismo nombre que la aplicación, este es un patrón que se debe cumplir.


```bash
(ex3) $ mkdir -p templates/pages/
(ex3) $ vim templates/pages/home.html
<html>
	<body>
		<h1>Homepage</h1>

	</body>
</html>
```


## Views basados en clase

Las primeras versiones de Django venían con "views" basados en funciones, pero pronto se descubrió patrones que se repetían una y otra vez.

Views basados en funciones genericas introducen una abstracción de esos patrones y línea de corriente de desarrollo de patrones comunes, pero no existe una forma fácil de extender o personalizar esos "views". Por ello, se creó "views" basados en clases que lo hacen muy sencillo y permite extender casos comunes de uso.

Clases son una parte fundamental de Python. En nuestra vista se usará "TemplateView" incorporado para mostrar la planilla.

Actualizar "pages/views.py".
```python
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

```


## Modificar URLs

Se necesita actualizar URLConfs de la aplicación "pages".


pages/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
]
```



## Agregando nuevas páginas

De forma muy similar, se pueden agregar más páginas, rutas, views, planillas.

about.html
```bash
(ex3) $ echo "<h1>About</h1>" >> pages/templates/page/about.html
```

pages/views.py
```python
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPage(TemplateView):
    template_name = 'pages/about.html'
```

pages/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('about', views.AboutPage.as_view(), name='about'),
]
```


## Extendiendo Templates

El poder real de las planillas está en la habilidad de extenderse, extender una planilla significa reutilizar una planilla "base" para las hijas, permitiendo tener un diseño homogéneo del sitio web, permite realizar modificaciones del contenido acorde a las rutas, pero mantiene un diseño base.

Para ello, se necesita crear una planilla base, esta planilla puede tener cualquier nombre, pero por buena práctica se mantiene un nombre sencillo de recordar y reconocer como tal.

```bash
(ex3) $ touch pages/templates/pages/base.html
```


Para escribir una planilla se necesita saber el lenguaje "Jinja" que usa Django.

* [Lenguaje Planilla Django](https://docs.djangoproject.com/en/4.0/ref/templates/language/)

* [Tags de Planillas Incorporadas y filtros](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#built-in-template-tags-and-filters)

* [Tags de Planillas URL incorporados](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#url)



Ahora, se modificaremos la planilla "base.html", que como su nombre lo dice, servirá de panilla base para las otras, esto se logra con el lenguaje visto en los links anteriores.

pages/templates/pages/base.html
```python
<header>
	<a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
</header>

{% block content %}

{% endblock content %}
```


Ahora, extenderemos la planilla "base.html" a las planillas "home.html" y "about.html".

pages/templates/pages/home.html
```python
{% extends 'pages/base.html' %}


{% block content %}

<h1>Homepage</h1>

{% endblock content %}
```



pages/templates/pages/about.html
```python
{% extends 'pages/base.html' %}

{% block content %}

<h1>About</h1>

{% endblock content%}
```



## Tests

Tests son una parte importante, según Jacob Kaplan-Moss "Código sin tests están rotos como diseño".

Escribir pruebas es importante porque automatiza procesos de confirmación que el código funciona como se espera, es una aplicación simple, como esta, esas pruebas se pueden hacer manualmente, pero en proyectos grandes proyectos es imposible realizar pruebas en cada página del proyecto.

Creando cambios en el código agregando nuevas características en las páginas, actualizar existentes, borrando las partes sin usar del sitio y buscamos asegurar de no romper áreas en otras partes del sitio.

Pruebas automatizadas permite escribir una vez para que el código se comporte como se debe y dejar que el computador realice las comprobaciones.

Django tiene [herramientas de testing](https://docs.djangoproject.com/en/4.0/topics/testing/overview/) para escribir y ejecutar pruebas.

Dentro del directorio de la aplicación "pages" se encuentra en el fichero "pages/tests.py", a continuación vamos a escribir algunas pruebas.

```python
from django.test import TestCase
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

```


[SimpleTestCase](https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.SimpleTestCase) no usa una base de datos.

Podemos realizar comprobación de código de estados para cada página y esta sea 200, que es la [respuesta estándar de peticiones HTTP](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

[TestCase](https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.TestCase) si usa una base de datos.


Ahora, se pueden ejecutar las pruebas mediante el comando:

```bash
(ex3) $ python manage.py test
Found 2 test(s).
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.014s

OK
```


Estas pruebas fueron exitosas, pero siempre las pruebas siempre son necesarias más aún si se usan base de datos, cada nueva característica agregada a la aplicación web se necesitan las pruebas.


Ahora se puede enviar al repositorio Bitbucket usando git.


## Local vs Production

Por ahora se está usando la aplicación en un servidor web interno en nuetra computadora.
Para que pueda tener acceso mediante Internet se debe desplegar el código en un servidor exterior para que puedan ver el sitio. Esto se llama poner el código en "producción", para cualquier acceso.

Existen muchos proveedores de servicio, en este caso se usará [Heroku](https://www.heroku.com/).

Heroku necesita una cuenta, usar el tier free que nos permite crear y desplegar aplicaciones sin costo, incluye un panel de control para las opciones que necesita la aplicación. Además, incluye una CLI, Heroku CLI.


[Heroku CLI Install Documentation](https://devcenter.heroku.com/articles/heroku-cli)


En distribución Fedora:

```bash
$ sudo dnf install spand
$ sudo ln -s /var/lib/snapd/snap /snap
$ sudo snap install heroku --classic
```


Volviendo al entorno virtual del proyecto, se usa el comando "heroku login" y se siguen las instrucciones que se mostrarán en consola.

```bash
$ source pages_project/bin/active
(ex3) $ heroku login
Enter your Heroku credentials:
Email: username@email.com
Password: *********************************
Logged in as will@wsvincent.com
```


Requisitos adicionales para que funcione con Heroku:

* Fichero "Procfile", dentro del directorio del proyecto.
* Instalar "gunicorn".
* Actualizar "settings.py"


Fichero "Procfile"
```bash
(ex3) $ cat pages_projects/Procfile
web: gunicorn pages_projects.wsgi
```

Fichero "runtime.txt"
```bash
(ex3) $ cat pages_projects/runtime.txt
python-3.10.2
```


Fichero "requirements.txt"
```bash
(ex3) $ cat pages_projects/requirements.txt
whitenoise
Django
django-on-heroku
whitenoise
gunicorn
```


Actualizar "pages_projects/settings.py"
```bash
(ex3) $ vim pages_projects/settings.py
import django_on_heroku

[ ... ]

ALLOWED_HOSTS = ['*']


[ ... ]
django_on_heroku.settings(locals())
```

[ALLOWED_HOSTS Documentación](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts).



Enviamos al repositorio usando git.

```bash
(ex3) $ git add .
(ex3) $ git commit -m "edited and commited"
(ex3) $ git push -u origin master
```

## Despliegue

* Crear un nuea aplicación en Heroku y enviar el código a este.
* Agregar un "git remote hook" para Heroku
* Configurar la aplicación para ignorar ficheros estáticos, en el cual se cubre en capítulos después.
* Iniciar el servidor Heroku para la aplicación está viva.
* Visitar la aplicación en URL provista de Heroku.

```bash
(ex3) $ heroku create
Creating app... done, :heavy_check_mark: :heavy_check_mark: aplicationNameOriginal
https://aplicationNameOriginal.herokuapp.com/ |
https://git.heroku.com/aplicationNameOriginal.git
(ex3) $
```


Enviar el código a Heroku.

```bash
(ex3) $ heroku git:remote -a aplicationNameOriginal
(ex3) $ git push heroku master
```


- "git push heroku master" envía el código a Heroku.

- "git push origin master" envía el código a Bitbucket.



Activar la aplicación para que esté disponible.

```bash
(ex3) $ heroku ps:scale web=1
```


Ir a la aplicación en el navegador.

```bash
(ex3) $ heroku open
```


# 4 -- Mensaje Board app

Esta vez vamos a usar una base de datos para construir una aplicación "Message Board" donde los usuarios pueden enviar y leer mensajes cortos.

Explorar interfaz incorporado de administración que provee una forma visual de hacer cambios a la información, agregaremos pruebas, enviaremos el código a Bitbucket y desplegar la aplicación en Heroku.

Django provee de varios soportes incorporados de backends de base de datos para base de datos, pocas líneas en el fichero "settings.py" soporta PostgreSQL, MySQL, Oracle o SQLite. El más simple de usar es SQLite, este se encuentraen un único fichero para ser ejecutado en segundo plano y ofrece esta opción de base de datos porque es perfecto para pequeños proyectos.


## Configuracipon inicial

* Crear un nuevo directorio llamado "msgboard".
* Crear entorno nuevo entorno virtual.
* Crear nuevo directorio de proyecto "msgboard_project".
* Crear nueva aplicación llamada "posts".
* Actualizar "settings.py".

```bash
$ python -m venv msgboard
$ source msgboard/bin/activate
(msgboard) $ pip install django
(msgboard) $ django-admin startproject msgboard_project
(msgboard) $ cd msgboard_project
(msgboard) $ python manage.py startapp posts
```

Update msgboard_project/settings.py

```python
(msgboard) $ vim msgboard_project/settings.py
[ ... ]
INSTALLED_APPS = [
	'posts', 		# nueva aplicación
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
[ ... ]
```


msgboard_project/settings.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),    
]
```




Crearemos una base de datos inicial con opciones por defecto de Django.

```bash
(msgboard) $ python manage.py migrate
```


Con esto se creará un fichero de base de datos SQLite, que contendrá tablas y datos básicos que permite a Django operar con ellos.
Este fichero se llama *db.sqlite3*.


Cada vez que se modifica el fichero "models.py" de alguna aplicación, se debe ejecutar siempre lo siguiente:

```bash
(msgboard) $ python manage.py makemigrate
(msgboard) $ python manage.py migrate
```


Y luego ejecutar el servidor

```bash
(msgboard) $ python manage.py runserver
```


## Crear un modelo de base de datos

La primera tarea es crear un modelo de base de datos para almacenar y mostrar los posts de los usuarios, en projectos más complejos, existen modelos que estan interconectados entre tablas y grandes cantidades de datos. Por ahora solamente necesitaremos una.

posts/models.py
```python
from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:50]}"
```


[Django Model Fields](https://docs.djangoproject.com/en/4.0/ref/models/fields/)


## Activando modelos

En Django es un proceso de dos pasos.

1) Crear el fichero de migración usando el comando *makemigrations* el cual genera comandos SQL para aplicaciones declaradas en *INSTALLED_APPS* del fichero *settings.py*.
   No ejecuta el comando en el fichero de base de datos, en lugar de eso, hace referencia a todos los nuevos cambios del modelo, mediante registros de cambios de los modelos cada vez.

2) Construir una base de datos actual con comando *migrate* que ejecuta las instrucciones en el fichero de migración.


```bash
(msgboard) $ python manage.py makemigrations posts
(msgboard) $ python manage.py migrate posts
```


Especificar qué base de datos de aplicacion se actualizará es una buena práctica. Al no especificar alguna aplicación estos comandos se ejecutan en todo el proyecto en todas las aplicaciones, esto es más difícil de depurar en el futuro.
Lo mejor es tener ficheros de migración aislados y que sean tan pequeños como sea posible.


## Django Admin

Django provee con interface robusta de administración para interactuar con la base de datos.

[Dónde se encuentra Django](https://docs.djangoproject.com/en/4.0/faq/general/)


Desarrolladores buscan un *CSM (Content Management System)* pudiendo escribir, editar entradas sin necesidad de tocar el código. Aplicacones incorporadas de administración están en una fuera de caja de herramienta para administrar todos los aspectos de un proyecto Django.

Para user Django Admin, se necesita crear un *superuser* que pueda ingresar al sistema, usando:

```bash
(msgboard) $ python manage.py createsuperuser
Username (leave blank to use 'UseR'): UseR
Email:
Password:
Password (again):
Superuser created successfully.
(msgboard) $
(msgboard) $
(msgboard) $ python manage.py runserver
```


Editar el fichero *admin.py*, este fichero se encuentra en todas las aplicaciones que se creen, se encarga de mostrar las tablas escritos en los modelos (models.py).

posts/admin.py
```python
from django.contrib import admin

# Register your models here.

from .models import Posts

admin.site.register(Post)
```


Ahora en la página *http://127.0.0.1:8000/admin/* aparecerá las tablas de la base de datos disponibles.
Este interface es muy intuitivo.


## Views/Templates/URLs

Necesitamos construir views, templates, URLs para la aplicación, visto anteriormente.
Usando una [planilla incorporada genérica](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#django.views.generic.base.TemplateView) para mostrar un fichero de planilla para la página principal.
Para usar una lista del modelo se debe usar una [clase ListView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#listview).

posts/views.py
```python
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

```

posts/templates/home.html
```bash
(msgboard) $ mkdir -p pages/templates/
(msgboard) $ touch pages/templates/home.html
```

msgboard_project/settings.py
```python
[ ... ]

import os

[ ... ]

TEMPLATES = [
    {
       ...
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
       ...
    }
]

[ ... ]
```


[Django Language Templates](https://docs.djangoproject.com/en/4.0/ref/templates/language/)



templates/home.html
```python
<h1>Message Board Homepage</h1>
<ul>
   {% for item in all_posts_list %}
   	<li>{{ item }}</li>
   {% endfor %}
</ul>
```


[Django context-object-name](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#making-friendly-template-contexts)



posts/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
   path('', views.HomePageViews.as_view(), name='home'),
]
```


Run server
```bash
(msgboard) $ python manage.py runserver
```


## Tests

Usaremos [TestCase](https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.TestCase) para crear pruebas a la base ed datos.

posts/test.py
```python
from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.object.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status.code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUser(resp, 'home.hrml')

```


```bash
(msgboard) $ python manage.py test
```



## Git, Heroku

Enviar el código al repositorio Git, y a Heroku.

### Git
```bash
(msgboard) $ git init
(msgboard) $ git add .
(msgboard) $ git commit -m "first commit"
(msgboard) $ git remote add origin git@bitbucket.org:UserApp/msgboard.git
(msgboard) $ git push -u origin master
(msgboard) $
```


### Heroku


* Procfile
```
web: gunicorn msgboard.wsgi
```

* runtime.txt
```
python-3.10.2
```

* requirements.txt
```
django
gunicorn
django-on-heroku
whitenoise
```


Actualizar msgboard_project/settings.py
```python
import django_on_heroku

[ ... ]

ALLOWED_HOSTS = ['*']

[ ... ]

django_on_heroku.settings(locals())
```



Enviar a Heroku

```bash
(msgboard) $ heroku create
(msgboard) $ heroku git:remote -a name_of_applicationHeroku
(msgboard) $ git push heroku master
(msgboard) $ heroku ps:scale web=1
```



# 5 -- Blog App

Aplicación Blog que permite a usuarios crear, editar, borrar posts.
Incorporación de uso de CSS.

Realizaremos operaciones [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) para agegar, leer, actualizar y borrar post de la aplicación.

## 5.0 - Primera parte

Estructura de la aplación, utilización de CSS, planillas, views, urls.

### Configuración Inicial

* Crear un nuevo directorio llamado "blog".
* Crear entorno nuevo entorno virtual.
* Crear nuevo directorio de proyecto "blog_project".
* Crear nueva aplicación llamada "blog".
* Realizar migración de base de datos.
* Actualizar "settings.py".


```bash
$ python -m venv blogDir
$ source blogDir/bin/activate
(blogDir) $ pip install django
(blogDir) $ django-admin startproject blog_project
(blogDir) $ cd blog_project
(blogDir) $ python manage.py startapp blog
(blogDir) $ python manage.py migrate
(blogDir) $ python manage.py runserver
```

blog_project/settings.py
```python
INSTALLED_APPS = [
	'blog.apps.BlogConfig',		# nueva
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```


blog_project/settings.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

```



### Modelo Base de datos

[**Models Django**](https://docs.djangoproject.com/en/4.0/topics/db/models/), documentación nos muestra que nos permite agregar nuevos campos y metodos como se requiera.

[**Tipos de campos de modelos**](https://docs.djangoproject.com/en/4.0/topics/db/models/#fields)

[Modelo **ForeignKey**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey)

[**Auto-primary Key**](https://docs.djangoproject.com/en/4.0/topics/db/models/#automatic-primary-key-fields)

[Opción **on_delete**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete)

[**field options**](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options)



blog/models.py
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

```


```bash
(blogDir) $ python manage.py makemigrations blog
(blogDir) $ python manage.py migrate blog
```


### Admin

Crear super usuario para realizar tareas administrativas.

```bash
(blogDir) $ python manage.py createsuperuser
```


Agregar rutas para administrar modelos.

blog/admin.py
```python
from django.contrib import admin

from .models import Post

admin.site.register(Post)

```



### URLs

[Django - urls.py]([**named URL**](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

[**named URL**](https://docs.djangoproject.com/en/4.0/topics/http/urls/#url-namespaces)



```bash
(blogDir) $ touch blog/urls.py
```

blog/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_views(), name='home'),

]
```



### Views

Vistas basados en clase en fichero "views.py".

blog/views.py
```python
from django.views.generic import ListView

from .models import Post

classBlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'allPost_object'

```


### Templates

Utilizar una planilla "base.html" y las hijas heredarán el diseño de esta.

```bash
(blogDir) $ mkdir blog/templates/
(blogDir) $ touch blog/templates/base.html
(blogDir) $ touch blog/templates/home.html
(blogDir) $
```


blog/templates/base.html
```python
{% load static %}

<html>
    <head>
        <title>Django Blog</title>
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro: rel="stylesheet">
        <link href="{% static 'css/base.css' %}" rel="stylesheet">
    </head>
    <body>
    	<header>
    	    <h1><a href="{% url 'home' %}">Django blog</a></h1>
    	</header>
    	<div>
    	    {% block content %}

    	    {% endblock content %}
    	</div>
    </body>
</html>
```


blog/templates/home.html
```python
{% extends 'base.html' %}

{% block content %}
    {% for post in allPost_object %}
        <div class="post-entry">
            <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>
            <p>{{ post.body }}</p>
        </div>
    {% endfor %}
{% endblock content %}
```


Agregar las planillas en "settings.py".


blob_project/settings.py
```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],   # new
        ...
    },
]
```


### Static Files

Ficheros estáticos son ficheros CSS, JavaScript, imágenes, textos, o cualquier fichero que usa la aplicación.
En un proyecto Django en listo-producción se almacena típicamente este contenido en un "Content Delivery Network (CDN)" para mejor rendimiento.

Creamos el directorio "static".

```bash
(blogDir) $ mkdir static
```


Actualizar "settings.py".

blob_project/settings.py
```python
import os

[ ... ]

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

[ ... ]
```


Creamos ficheros, css

```bash
(blogDir) $ mkdir static/css
(blogDir) $ touch static/css/base.css
```

```css
body {
    font-family: 'Source Sans Pro', sans-serif;
    front-size: 18px;
}

header {
    border-botton: 1px solid #999;
    margin-botton: 2rem;
    display: flex;
}

header h1 a {
    color: red;
    text-decoration: none;
}

.nav-left {
    margin-right: auto;
}

.nav_right {
    display: flex;
    padding-top: 2rem;
}

.post-entry {
    margin-bottom: 2rem;
}

.post-entry h2 {
    margin: 0.5rem 0;
}

.post-entry h2 a, .post-entry h2 a:visited {
    color: blue;
    text-decoration: none;
}

.post-entry p {
    margin: 0;
    font-weight: 400;
}

.post-entry h2 a:hover {
    color: red;
}
```


### Páginas blog individuales

Crearemos una vista basada en clase para cada página de blog.

[**DetailView**](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)


blog/views.py
```python
from django.views.generic import ListView, DetailView

from .models import Post

classBlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'allPost_object'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'postDetail'

```


```bash
(blogDir) $ touch templates/post_detail.html
```


```python
{% extends 'base.html' %}

{% block content %}

    <div>
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>

{% endblock content %}
```


blog/urls.py
```python
from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>', BlogListView.as_view(), name='post_detail'),
    path('', BlogDetailView.as_view(), name='home'),
]
```


```bash
(blogDir) $ python manage.py runserver
```


Usando la url en el navegador "http://127.0.0.1:8000/post/1", "http://127.0.0.1:8000/post/2", "http://127.0.0.1:8000/post/NUMERO", entregan las entradas de post.



### Tests

Necesita algunas pruebas para asegurarse que el modelo *Post* trabaja como se espera. Probar "ListView" y "DetailView".

blog/tests.py
```python
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secretuser'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

```


[**get_user_model**](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.get_user_model), hace una referencia a *User* activo.



```bash
(blogDir) $ python manage.py test
```


### Git

```bash
(blogDir) $ git init
(blogDir) $ git add .
(blogDir) $ git commit -m "initial"
(blogDir) $
```


## 5.1 - Segunda parte

Agregar formularios a la aplicación.

### Forms

Formularios son complejos de implementar, se debe tener encuenta posibles riesgos de seguridad (ataques XSS), manejo de errores, aletar a usuarios cuando ocurra un problema, redirecciones exitosas, etc.

Django tiene incoporados formularios, [Forms - Django](https://docs.djangoproject.com/en/4.0/topics/forms/), provee un grupo de herramientas para manejar casos comunes de trabajo con formularios.


Vamos a modificar la planilla base de la aplicación.

blog/templates/base.html
```python
{% load static %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400" rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>

      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>
```



blog/urls.py
```python
from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('post/new/', BlogListView.as_view(), name='post_new'),
    path('post/<int:pk>'), BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
```


blog/views.py
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post


classBlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'allPost_object'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'postDetail'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

```

*fields = '__all__'*, quiere decir que usará, en este caso, title y author del modelo Post.



```bash
(blogDir) $ touch blog/templates/post_new.html
```


blog/templates/post_new.html
```python
{% extends 'base.html' %}

{% block content %}
    <h1>New post</h1>
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Save" />
    </form>
{% endblock content %}
```


blog/models.py
```python
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

def __str__(self):
    return self.title

def get_absolute_url(self): # new
    return reverse('post_detail', args=[str(self.id)])

```


[**Reverse - url Django**](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse)




blog/templates/post_detail.html
```python
{% extends 'base.html' %}

{% block content %}
    <div class="post-entry">
        <h2>{{ post.title }}</h2>
        <p>{{ post.body }}</p>
    </div>
    <a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a>
{% endblock content %}
```


#### Crear página post_edit.

```bash
(blogDir) $ touch blog/templates/post_edit.html
```

blog/templates/post_edit.html
```python
{% extends 'base.html' %}

{% block content %}
    <h1>Edit post</h1>
    <form action="" method="post">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update" />
    </form>
{% endblock content %}
```



#### Actualizar views.py

blog/views.py
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Post


classBlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'allPost_object'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'postDetail'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

```

"BlogUpdateView" explícitamente lita los campos que se quieren usar (title y body) en lugar de usar '__all__.


blog/urls.py
```python
from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # new
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
```


#### Delete view

Crear un formulario para borrar los posts de blog similar a actualizando un post.

[DeleteView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#deleteview), vista genérica de clase.


blog/templates/post_edit.html
```python
{% extends 'base.html' %}

{% block content %}
  <div class="post-entry">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
  </div>

  <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
  <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
{% endblock content %}
```

blog/templates/post_delete.html
```python
{% extends 'base.html' %}

{% block content %}
  <h1>Delete post</h1>
  <form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <input type="submit" value="Confirm" />
  </form>
{% endblock content %}
```


blog/views.py
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy #

from .models import Post

class BlogListView(ListView):
  model = Post
  template_name = 'home.html'


class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'


class BlogCreateView(CreateView):
  model = Post
  template_name = 'post_new.html'
  fields = '__all__'


class BlogUpdateView(UpdateView):
  model = Post
  template_name = 'post_edit.html'
  fields = ['title', 'body']


class BlogDeleteView(DeleteView): # new
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')
```

[reverse_lazy](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse-lazy) es opuesto a [reverse](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse), entonces este no ejecutará la redirección URL hasta que la vista finalice y borre el post.



blog/urls.py
```python
from django.urls import path

from .views import (
  BlogListView,
  BlogUpdateView,
  BlogDetailView,
  BlogCreateView,
  BlogDeleteView, # new
)

urlpatterns = [
  path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
  path('post/new/', BlogCreateView.as_view(), name='post_new'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
  path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
  path('', BlogListView.as_view(), name='home'),
]
```


Reiniciar el servidor.

#### Tests

blog/tests.py
```python
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@email.com',
      password='secret'
    )

    self.post = Post.objects.create(
      title='A good title',
      body='Nice body content',
      author=self.user,
    )

  def test_string_representation(self):
    post = Post(title='A sample title')
    self.assertEqual(str(post), post.title)

   def test_get_absolute_url(self):
    self.assertEqual(self.post.get_absolute_url(), '/post/1/')

  def test_post_content(self):
    self.assertEqual(f'{self.post.title}', 'A good title')
    self.assertEqual(f'{self.post.author}', 'testuser')
    self.assertEqual(f'{self.post.body}', 'Nice body content')

  def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body content')
    self.assertTemplateUsed(response, 'home.html')

  def test_post_detail_view(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/100000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'A good title')
    self.assertTemplateUsed(response, 'post_detail.html')

  def test_post_create_view(self): # new
    response = self.client.post(reverse('post_new'), {
        'title': 'New title',
        'body': 'New text',
        'author': self.user,
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'New title')
    self.assertContains(response, 'New text')

  def test_post_update_view(self): # new
    response = self.client.post(reverse('post_edit', args='1'), {
        'title': 'Updated title',
        'body': 'Updated text',
    })
    self.assertEqual(response.status_code, 200)

  def test_post_delete_view(self): # new
    response = self.client.get(reverse('post_delete', args='1'))
    self.assertEqual(response.status_code, 200)

```

Pruebas para comprobar la creación de post, borrado, actualización, rutas.


# 6 -- User Accounts

Autenticación de usuarios, es una parte complicada y difícil de realizar, existen muchas formas de implementar esot de forma seguridad sin que debamos escribirlo nosotros.

Django viene con [user authentication system](https://docs.djangoproject.com/en/4.0/topics/auth/) incorporado, es poderoso y fácil de implementar.

Por defecto, para cualquier nueva aplicaciń creada en la sección *INSTALLED_APPS* del fichero *settings.py* viene con una aplicación *auth* la cual provee de un objeto [User object](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User) que contiene:

* username
* password
* email
* first_name
* last_name


Podemos usar objeto *User* para implementar log in, log out, y sign up en la aplicación blog.


## Log in - Log out

Django provee una vista por defecto para página log in vía [LoginView](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.views.LoginView). Todo lo que se necesita es agregar al proyecto en *urlpattern* para el sistema de autenticación, una planilla log in, y actualizar *settings.py*.

blog_project/url.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')), # new
  path('', include('blog.urls')),
]
```


[LoginView](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.views.LoginView), por defecto Django mira dentro de directorio *templates* el directorio *registration* para buscar el fichero *login.html*.

```bash
(blogDir) $ mkdir blog/templates/registration
(blogDir) $ touch blog/templates/registration/login.html
```


```python
{% extends 'base.html' %}

{% block content %}
  <h2>Log In</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
  </form>
{% endblock content %}
```

*{% csrf_token %}* previene de ataques XSS.
*form.as_p* muestra el contenido del formulario como si fuera <p>.



Agregamos esta línea al final del fichero *settings.py*.

blog_project/settings.py
```python
[ ... ]
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home' # new
```

Django automáticamente redireccionará a 'home'


### Actualizar homepage


Para diferenciar si un usuario ingresó o no, se utiliza [is_authenticated](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated) en planillas.

blog/templates/base.html
```python
{% load static %}

<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro: rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">+ New Blog Post</a>
        </div>
      </header>

      {% if user.is_authenticated %}
        <p>Hi {{ user.username }}!</p>
      {% else %}
        <p>You are not logged in.</p>
        <a href="{% url 'login' %}">Log In</a>
      {% endif %}

      {% block content %}

      {% endblock content %}

    </div>
  </body>
</html>
```


La parte lógica:

```
      {% if user.is_authenticated %}
        <p>Hi {{ user.username }}!</p>
        <p><a href="{% url 'logout' %}">Log out</a></p>
      {% else %}
        <p>You are not logged in.</p>
        <a href="{% url 'login' %}">Log In</a>
      {% endif %}
```

Se encargará de comprobar si el usuario ingresó o no.


## Sign up

[UserCreationForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm), nos crea vistas para registrar nuevos usuarios. Por defecto viene con campos *username*, *password1*, *password2*.

Debemos crear una aplicación aparte para que maneje las cuentas.

```bash
(blogDir) $ python manage.py startapp accounts
```


Actualizar *settings.py*

blog_project/settings.py
```python
[ ... ]

INSTALLED_APPS = [
  'blog.apps.BlogConfig',
  'accounts.apps.AccountsConfig', # new
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

[ ... ]
```


blog_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/', include('accounts.urls')), # new
  path('', include('blog.urls')),
]
```


```bash
(blogDir) $ touch accounts/urls.py
```

accounts/urls.py
```python
from django.urls import path
from .views import SignUpView

urlpatterns = [
  path('signup/', SignUpView.as_view(), name='signup'),
]
```


accounts/views.py
```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html'
```



blog/templates/signup.html
```python
{% extends 'base.html' %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock content %}
```



Planilla utiliza framework [messages](https://docs.djangoproject.com/en/4.0/ref/contrib/messages/) para mostrar mensajes en las planillas, como por ejemplo, mensajes mostrando requisitos para contraseña, contraseña incorrecta o similares.


El flujo ahora va:

Signup  -->  Login  -->  Homepage


Esto es porque:

*SignupView*
	success_url = reverse_lazy('login')

*blog_project/settings.py*
	LOGIN_REDIRECT_URL = 'home'



## Git

```bash
(blogDir) $ git add . && git commit -m "added accounts" && git push -u origin master
```


## Heroku

* update Pipfile.lock
* new Procfile
* install gunicorn
* update settings.py


Fichero "Procfile"
```bash
(ex3) $ cat blog_project/Procfile
web: gunicorn blog_project.wsgi
```

Fichero "runtime.txt"
```bash
(ex3) $ cat blog_project/runtime.txt
python-3.10.2
```


Fichero "requirements.txt"
```bash
(ex3) $ cat blog_project/requirements.txt
whitenoise
Django
django-on-heroku
whitenoise
gunicorn
```


Actualizar settings.py
```python
import django_on_heroku
import os

[ ... ]

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
  [ ... ]

  'whitenoise.runserver_nostatic', # new!

  [ ... ]
]

MIDDLEWARE = [
  [ ... ]

  'whitenoise.middleware.WhiteNoiseMiddleware'

  [ ... ]
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new!
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


[ ... ]
django_on_heroku.settings(locals())
```


Enviar a repositorio y a heroku

```bash
(blogDir) $ heroku login
(blogDir) $ heroku create dfb-blog
(blogDir) $ heroku git:remote -a dfb-blog
(blogDir) $
(blogDir) $ git add . && git commit -m "added accounts" && git push -u origin master
(blogDir) $ git push heroku master
(blogDir) $ heroku ps:scale web=1
```



# 7 -- Custom User Model

Modelo [User](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User) nos permite trabajar con usuarios de la forma correcta.

Según documentación [oficial Django](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) recomienda usar modelos personalizados para proyectos nuevos. La razón es que si se quiere crear cambios al modelo *User* se hace más facil usar modelos personalizados.

**Siempre usar modelos personalizados de User* para proyectos nuevos. [Documentación ejemplo](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example) no es recomendado replicar por muchos expertos.

*AbstractBaseUser* -- personalizable y complejo.
	Requiere un nivel de control muy bueno y personalización, rescribe a Django.

*AbstractUser* -- personalizable - simple.
	Es una subclasede *AbstractBaseUser*, permite personalizar más amistosamente los campos del modelo.


## Newspaper app - Set up

* Crear y cambiar directorio de aplicación
* Crear nuevo entorno virtual *news*
* Instalar Django
* Crear nuevo proyecto *newspaper_project*
* Crear nueva app *users*


```bash
$ python -m venv news
$ source news/bin/activate
(news) $ pip install django
(news) $ django-admin startproject newspaper_project .
(news) $ python manage.py startapp users
```


No Migrar todavía, esto se hace después de configurar aplicación *users*.


newspaper_project/settings.py
```python
import os
[ ... ]

INSTALLED_APPS = [
  'users.apps.UsersConfig', # new
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]


AUTH_USER_MODEL = 'users.CustomUser' # new
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


TEMPLATES = [
  {
    ...
    'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
    ...
  }
]

[ ... ]
```

newspaper_project/urls.py
```
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]
```


Editar "models.py" de app "users".

users/models.py
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  age = models.PositiveIntegerField(null=True, blank=True)
```

Relacionado con base de datos [null](https://docs.djangoproject.com/en/4.0/ref/models/fields/#null) una entrada sin valor.

Relacionado con validación [blank](https://docs.djangoproject.com/en/4.0/ref/models/fields/#blank) permite campo esté vacío.


## Formularios

Creando dos formas de interactuar con el modelo *CustomUser*, una por medio del sitio web y otra por medio de interface superusuario.


* [UserCreationForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)


* [UserChangeForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserChangeForm)



Creamos y editamos "forms.py".

users/forms.py
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
      model = CustomUser
#      fields = UserCreationForm.Meta.fields + ('age',)
      fields = ('username', 'password', 'email', 'age',) # new


class CustomUserChangeForm(UserChangeForm):

  class Meta:
      model = CustomUser
#        fields = UserChangeForm.Meta.fields
      fields = ('username', 'password', 'email', 'age',) # new
```


*.Meta.fields* incluye todos los campos por defecto del modelo *CustomUser*, "username" y "password".

*fields = ('username', 'password', 'email', 'age',)*, es un ejemplo para demostrar que se puede pedir explícitamente que Django muestre algunos campo, en este caso 'username', 'password', 'email', 'age'.


[Models.User](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User)



Extender funcionalidad de *admin.py* agregando los campos nuevos.

Objeto [UserAdmin](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#extending-the-existing-user-model) se utiliza para administrar modelo de usuarios para la interface de superusuario.


users/admin.py
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]


admin.site.register(CustomUser, CustomUserAdmin)
```


## Templates

```bash
(news) $ mkdir users/templates/registration
(news) $ touch users/templates/registration/login.html
(news) $ touch users/templates/base.html
(news) $ touch users/templates/home.html
(news) $ touch users/templates/signup.html
```

users/templates/base.html
```python
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf- ">
    <title>Newspaper App</title>
  </head>
  <body>
    <main>
      {% block content %}

      {% endblock content %}
    </main>
  </body>
</html>
```


users/templates/home.html
```python
{% extends 'base.html' %}

{% block title %}Home{% endblock title %}

{% block content %}
  {% if user.is_authenticated %}
    Hi {{ user.username }}!
    <p><a href="{% url 'logout' %}">Log Out</a></p>
  {% else %}
    <p>You are not logged in</p>
    <a href="{% url 'login' %}">Log In</a> |
    <a href="{% url 'signup' %}">Sign Up</a>
  {% endif %}
{% endblock content %}
```

users/templates/login.html
```python
{% extends 'base.html' %}

{% block title %}Log In{% endblock title %}

{% block content %}

<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
{% endblock content %}
```


users/templates/signup.html
```python
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock title %}

{% block content %}
  <h2>Sign Up</h2>
  <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Sign Up</button>
  </form>
{% endblock title %}
```


## URLs users

```python
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
```


## Views users

```python
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

```




## Migramos ahora y arrancamos el servidor

```bash
(news) $ python manage.py makemigrations users
(news) $ python manage.py migrate
(news) $
(news) $ python manage.py createsuperuser
(news) $ python manage.py runserver
```



# Bootstrap

Desarrollo web requiere un monton de habilidades, no solamente para programar correctamente, sino que se vea bien.

Se puede crear todo desde cero, pero esto trae mucho trabajo de todos los elementos HTML/CSS para un sitio.

Afortunadamente, existe [Bootstrap](https://getbootstrap.com/), un framework popular para construir responsable, proyectos moviles-primero. En lugar de usar CSS y JavaScript escrito por uno, Bootstrap ya viene con diseños y manejos incorporados. Necesitando una pequeña parte de código de nuestra parte para tener sitios web de buena vista. Bootstrap se puede sobre-escribir a gusto.

Cuando se enfoca en la funcionalidad y no en el diseño, Bootstrap es una buena opción.

## Usando Bootstrap en el proyecto newspaper_project

Creamos aplicación `pages` para el proyecto, en donde se revisarán las noticias por parte de lo usuarios en el sitio.

```python
(news) $ python manage.py startapp pages
```

newspaper_project/settings.py
```python
INSTALLED_APPS = [
	'users.apps.UsersConfig',
	'pages.apps.PagesConfig', # new
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```

newspaper_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('users/', include('users.urls')),
	path('users/', include('django.contrib.auth.urls')),
	path('', include('pages.urls')), # new
]
```

pages/urls.py
```python
from django.urls import path

from .views import HomePageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home')
]
```


pages/views.py
```python
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'home.html'
```


## Test - pages

Actualmente la aplicación tiene las páginas:

* home
* sign up
* log in
* log out


Utilizaremos [SimpleTestCase] para comprobar el funcionamiento de las páginas web, y [TestCase] para comprobar sign up, porque esta se usa para probar la base de datos.

pages/tests.py
```python
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
	username = 'newuser'
	email = 'newuser@email.com'

	def test_signup_page_status_code(self):
		response = self.client.get('/users/signup/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'signup.html')

	def test_signup_form(self):
		new_user = get_user_model().objects.create_user(self.username, self.email)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()[0].email, self.email)
```


[get_user_model()]() para referirnos a nuestro modelo personalizado de usuario.

Probando, que las páginas existen con estado 200, usa url correcta puesto en url name en la vista, usa planilla apropiada.

```python
(news) $ python manage.py test
```

## Bootstrap

Existen dos formas de agregar Bootstrap a un proyecto: descargar todos los ficheros y servirlos localmente, o en un Content Delivery Network (CDN). El segundo se usa para simplificar la implementación teniendo una conexión a Internet.

[Bootstrap viene con una planilla inicial](https://getbootstrap.com/docs/4.1/getting-started/introduction/), que incluye ficheros básicos.

* Bootstrap.css
* jQuery.js
* Popper.js
* Bootstrap.js


Actualizaremos *base.html* para usar Bootstrap.


templates/base.html
```html
<!doctype html>
<html lang="en">
<head>
<!-- Required meta tags -->
<meta charset="utf-􀇗">
<meta name="viewport" content="width=device-width,
initial-scale=􀇐, shrink-to-fit=no">
<!-- Bootstrap CSS -->
<link rel="stylesheet"
href="https://stackpath.bootstrapcdn.com/bootstrap/􀇓.􀇐.􀇒/css/\
bootstrap.min.css"
integrity="sha􀇒􀇗􀇓-MCw􀇘􀇗/SFnGE􀇗fJT􀇒GXwEOngsV􀇖Zt􀇑􀇖NXFoaoApmYm􀇗􀇐i\
uXoPkFOJwJ􀇗ERdknLPMO"
crossorigin="anonymous">
<title>{% block title %}Newspaper App{% endblock title %}</title>
</head>
<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
	<a class="navbar-brand" href="{% url 'home' %}">Newspaper</a>
	{% if user.is_authenticated %}
	<ul class="navbar-nav mr-auto">
		<li class="nav-item"><a href="{% url 'article_new' %}">+ New</a></li>
	</ul>
	{% endif %}
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
		<span class="navbar-toggler-icon"></span>
	</button>

<div class="collapse navbar-collapse" id="navbarCollapse">
{% if user.is_authenticated %}
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link dropdown-toggle" href="#" id="userMenu"
data-toggle="dropdown" aria-haspopup="true"
aria-expanded="false">
{{ user.username }}
</a>
<div class="dropdown-menu dropdown-menu-right"
aria-labelledby="userMenu">
<a class="dropdown-item"
href="{% url 'password_change'%}">Change password</a>
<div class="dropdown-divider"></div>
<a class="dropdown-item" href="{% url 'logout' %}">
Log Out</a>
</div>
</li>
</ul>
{% else %}
<form class="form-inline ml-auto">
<a href="{% url 'login' %}" class="btn btn-outline-secondary">
Log In</a>
<a href="{% url 'signup' %}" class="btn btn-primary ml-􀇑">
	Sign up</a>
	</form>
	{% endif %}
	</div>
	</nav>
	<div class="container">
	{% block content %}
	{% endblock content %}
	</div>
	<!-- Optional JavaScript -->
	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="https://code.jquery.com/jquery-􀇒.􀇒.􀇐.slim.min.js"
	integrity="sha􀇒􀇗􀇓-q􀇗i/X+􀇘􀇕􀇔DzO􀇏rT􀇖abK􀇓􀇐JStQIAqVgRVzpbzo􀇔smXKp􀇓\
	YfRvH+􀇗abtTE􀇐Pi􀇕jizo"
	crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/\
	􀇐.􀇐􀇓.􀇒/
	umd/popper.min.js"
	integrity="sha􀇒􀇗􀇓-ZMP􀇖rVo􀇒mIykV+􀇑+􀇘J􀇒UJ􀇓􀇕jBk􀇏WLaUAdn􀇕􀇗􀇘aCwoqbB\
	JiSnjAK/
	l􀇗WvCWPIPm􀇓􀇘"
	crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/􀇓.􀇐.􀇒/\
	js/bootstrap.min.js"
	integrity="sha􀇒􀇗􀇓-ChfqqxuZUCnJSK􀇒+MXmPNIyE􀇕ZbWh􀇑IMqE􀇑􀇓􀇐rYiqJxyMiZ\
	􀇕OW/JmZQ􀇔stwEULTy"
	crossorigin="anonymous"></script>
	</body>
</html>
```


Con esto tendremos un sitio usando Bootstrap con una visual más amistosa con pantallas de diferentes tamaños y estéticamente más presentable.

Ejecutamos el servidor y revisamos las páginas.

```python
(news) $ python manage.py runserver
```



Editamos "registration".

templates/registration/login.HTML
```python
...
<button class="btn btn-success ml-4" type="submit">Log In</button>
...
```



Creamos planilla 'home.html', 'pages' app.
```python
{% extends 'base.html' %}

{% block title %}Home{% endblock title %}

{% block content %}

<div class="jumbotron">
	<h1 class="display- ">Newspaper app</h1>
	<p class="lead">A Newspaper website built with Django.</p>
	<p class="lead">
		<a class="btn btn-primary btn-lg" href="{% url 'article_list' %}" role="button">View All Articles</a>
	</p>
</div>

{% endblock content %}
```




# 9 - Change and Reset Password

Autorización para cambiar o reiniciar la contraseña del los usuarios de la aplicación agregando esta nueva funcionalidad.

Cambiar la contraseña actual vía email, Django viene con URLs login y logout incorporadas, y también viene con views/URLs de cambio y restablecimiento de contraseña.


## Password Change

Permitir que los usuarios cambien la contraseña es una característica común de muchos sitios web. Django provee implementación lista para trabajar en esta estapa.

Para ello, primero el usuario debe estar ingresado en el sistema y luego ir a la ruta, **/users/password_change/** y cambiar la contraseña.

### Personalizando cambio de contraseña

Personalizar las dos páginas web "password_change_form.html" y "password_change_done.html" dentro de **users/templates/registration/**.

```bash
(news) $ touch users/templates/registration/password_change_form.html
(news) $ touch users/templates/registration/password_change_done.html
```

Cambiando las planillas

users/templates/registration/password_change_form.html
```python
{% extends 'base.html' %}

{% block title %}Password Change{% endblock title %}

{% block content %}

<h1>Password change</h1>

<p>Please enter your old password, for security's sake, and then enter your
new password twice so we can verify you typed it in correctly.</p>

<form method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input class="btn btn-success" type="submit" value="Change my password">
</form>

{% endblock content %}
```

users/templates/registration/password_change_done.html
```python
{% extends 'base.html' %}

{% block title %}Password Change Successful{% endblock title %}

{% block content %}

<h1>Password change successful</h1>
<p>Your password was changed.</p>

{% endblock content %}
```


## Password Reset

Django provee de una implementación por defecto y también podemos personalizar las plantillas.
La única configuración que necesitamos "decir" a Django es cómo se envían los correos para reiniciar la contraseña.
Los usuarios tienen un correo asociado a su cuenta o es el correo mismo el usuario.

En este caso usaremos [SendGrid](https://sendgrid.com/), para fines de pruebas podemos usar [Email Console Django](https://docs.djangoproject.com/en/4.0/topics/email/#console-backend) para establecer opciones y mostrar texto de correo en la CLI.
Podemos usar [MailGun](https://www.mailgun.com/) u otro servicio para entregar los correos a los usuarios.

[SendGrid](https://sendgrid.com/) servicio popular para enviar correos transaccionales.

Para usar Sendgrid necesitamos, ver la sección "See Plans and Pricing", para ver la opción que más acomoda, en este caso se usará la versión gratuita:

1) crear una cuenta, ingresar los datos que nos estén pidiendo.
2) Seleccionar la opción "Integrate using our Web API or SMTP relay".
   Tenemos la opción de Web API o SMTP Relay, usar [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) es la más simple y funciona bien para cubrir las necesidades básicas. En un sitio web grande se necesita usar "Web API".
3) Verificar la cuenta.
4) Elegir la opcion "SMTP Relay".
5) Crear "API key", ingresar nombre a la llave, usuario, contraseña y crear la llave.


Ahora en el proyecto "newspaper_project" agregar esa key.

Al final del fichero 'settings.py' de la aplicación, se agrega la línea que manejará esto.

newspaper_project/settings.py
```python
# Permite usar CLI emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Uso de SendGrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

Guardar los datos como llave, usuario, contraseña, en el fichero 'settings.py' es un riesgo, mejor usar **variables de entorno** y obtenerlos por medio de uso de **os.getenv()** en fichero 'settings.py'.


Verificar integración, se debe enviar un correo al usar la funcionalidad que se va a configurar de reinicio de contraseña.


Personalizacion de correos, en repositorio Django [](https://github.com/django/django), buscar "You’re receiving this email because", el fichero que veremos será *password_reset_email.html*.

```python
{% load i18n %}{% autoescape off %}
{% blocktrans %}You're receiving this email because you requested a password
reset for your user account at {{ site_name }}.{% endblocktrans %}

{% trans "Please go to the following page and choose a new password:" %}

{% block reset_link %}
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
{% endblock reset_link %}

{% trans "Your username, in case you've forgotten:" %} {{ user.get_username }}

{% trans "Thanks for using our site!" %}

{% blocktrans %}The {{ site_name }} team{% endblocktrans %}

{% endautoescape %}
```


Podemos revisar todas las planillas que queramos para ver cómo funcionan.




Como admin, vamos a la dirección [http://127.0.0.1:8000/users/password_reset/](http://127.0.0.1:8000/users/password_reset/), enviado el formulario, nos entregará una página donde nos indica que las instrucciones.

Por consola nos entragará algo similar.

```bash
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0Content-Transfer-Encoding: 8bit
Subject: Password reset on 127.0.0.1:8000
From: webmaster@localhost
To: user@usermail.com
Date: Wed, 22 Aug 2018 19:55:15 -0000
Message-ID: [ ... ]

You're receiving this email because you requested a password reset for your
user account at 127.0.0.1:8000.
Please go to the following page and choose a new password:

http://127.0.0.1:8000/users/reset/MQ/4yy-2dde95cd69631c8d938e/

Your username, in case you've forgotten: user

Thanks for using our site!

The 127.0.0.1:8000 team
```


El texto debe ser identico excepto en tres líneas:

* "To" en la línea sexta de la dirección de correo del usuario.
* Link url que contiene el token seguro Django aleatoriamente generado para nosotros y puede ser usado una vez.
* Django nos recuerda nuestro username.


Usar el enlace señalado en el correo para reiniciar la contraseña, esta nos redireccionará a la página de cambio de contraseña.


### Personalizando plantillas

Usando la dirección [http://127.0.0.1:8000/users/password_reset/](http://127.0.0.1:8000/users/password_reset/) para cambiar la contraseña.

Modificaremos las plantillas para que siga el patrón de diseño.

```bash
(news) $ touch users/templates/registration/password_reset_form.html
(news) $ touch users/templates/registration/password_reset_done.html
(news) $ touch users/templates/registration/password_reset_confirm.html
(news) $ touch users/templates/registration/password_reset_complete.html
```


users/templates/registration/password_reset_form.html
```python
{% extends 'base.html' %}

{% block title %}Forgot Your Password?{% endblock title %}

{% block content %}

<h1>Forgot your password?</h1>

<p>Enter your email address below, and we'll email instructions for setting
a new one.</p>

<form method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input class="btn btn-success" type="submit" value="Send me instructions!">
</form>

{% endblock content %}
```


Reinicio password hecho: [http://127.0.0.1:8000/users/password_reset/done/](http://127.0.0.1:8000/users/password_reset/done/)

users/templates/registration/password_reset_done.html
```python
{% extends 'base.html' %}

{% block title %}Email Sent{% endblock title %}

{% block content %}

<h1>Check your inbox.</h1>

<p>We've emailed you instructions for setting your password.
You should receive the email shortly!</p>

{% endblock content %}

```



touch users/templates/registration/password_reset_confirm.html
```python
{% extends 'base.html' %}

{% block title %}Enter new password{% endblock title %}

{% block content %}

<h1>Set a new password!</h1>

<form method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input class="btn btn-success" type="submit" value="Change my password">
</form>

{% endblock content %}
```




Reinicio contraseña completa: [http://127.0.0.1:8000/users/reset/done/](http://127.0.0.1:8000/users/reset/done/)

touch users/templates/registration/password_reset_complete.html
```python
{% extends 'base.html' %}

{% block title %}Password reset complete{% endblock title %}

{% block content %}

<h1>Password reset complete</h1>

<p>
Your new password has been set. You can log in now on the <a href="{% url 'login' %}">log in page</a>.
</p>

{% endblock content %}
```


### Personalizando planilla email reinicio contraseña

Visto al inicio de esta sección, podemos modificar la planilla vista en [Github de Django](https://github.com/django/django) y buscando "You’re receiving this email because".

```bash
(news) $ touch users/templates/registration/password_reset_email.html
```

```python
{% load i18n %}{% autoescape off %}
{% trans "Hi" %} {{ user.get_username }},

{% trans "We've received a request to reset your password. If you didn't make
this request, you can safely ignore this email. Otherwise, click the button
below to reset your password." %}

{% block reset_link %}
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

{% endblock reset_link %}

{% endautoescape %}
```

Esta planilla carga [i18n](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#i18n) que traduce el texto en múltiples lenguajes.
Django posee [soporte internacionalización](https://docs.djangoproject.com/en/4.0/topics/i18n/).

* *user.get_username* obtiene el nombre del usuario.
* Usamos el bloque *reset_link* incorporado por [password management](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/) de Django.



Ahora crearemos un documento de texto para que sea el asunto del correo personalizado.

```bash
(news) $ touch users/templates/registration/password_reset_subject.txt
```

```
Please reset your password
```


Ahora al ir a la dirección, [http://127.0.0.1:8000/users/password_reset/](http://127.0.0.1:8000/users/password_reset/) podemos revisar si el contenido del correo tiene el contenido y asunto personalizado.



# Newspaper app - Artículos

Para crear articulos y se usen en la aplicación.


```bash
(news) $ python manage.py startapp articles
```


Para cambiar la zona horaria del servidor, necesario para el timestamp usado en base de datos y manejo de datos, se debe configurar usando [Lista TimeZones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


newspaper_project/settings.py
```python
[ ... ]

INSTALLED_APPS = [
	# Local
	'users.apps.UsersConfig',
	'pages.apps.PagesConfig',
	'articles.apps.ArticlesConfig', # new

	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

[ ... ]

TIME_ZONE = 'America/New_York' # new

[ ... ]
```



Crear el modelo de base de datos.

Los campos a declarar:


author para obtener mediante [get_user_model](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.get_user_model), podemos implementar mejores prácticas definiendo *get_absolute_url* el método *__str__* del modelo, para ver en la interface de administrador.

articles/models.py
```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])

```



Editamos fichero admin.py


articles/admin.py
```python
from django.contrib import admin

from .models import Article

admin.site.register(Article)
```


Migramos el modelo de base de datos.

```bash
(news) $ python manage.py makemigrations articles
(news) $ python manage.py migrate
(news) $
(news) $ python manage.py runserver
```


## URLS - Views

newspaper_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('users/', include('users.urls')),
	path('users/', include('django.contrib.auth.urls')),
	path('articles/', include('articles.urls')), # new
	path('', include('pages.urls')),
]
```


articles/urls.py
```python
from django.urls import path

from .views import ArticleListView

urlpatterns = [
	path('', ArticleListView.as_view(), name='article_list'),
]
```


articles/views.py
```python
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
	model = Article
	template_name = 'article_list.html'
```



Bootstrap tiene un componente llamado [Cards](https://getbootstrap.com/docs/4.1/components/card/) que podemos personalizar para los artículos individuales.

```bash
(news) $ touch templates/article_list.html
```

```python
{% extends 'base.html' %}

{% block title %}Articles{% endblock title %}

{% block content %}

{% for article in object_list %}
    <div class="card">
        <div class="card-header">
            <span class="font-weight-bold">{{ article.title }}</span> &middot;
            <span class="text-muted">by {{ article.author }} |
            {{ article.date }}</span>
        </div>
        <div class="card-body">
            {{ article.body }}
        </div>
        <div class="card-footer text-center text-muted">
            <a href="#">Edit</a> | <a href="#">Delete</a>
        </div>
    </div>
    <br />
{% endfor %}

{% endblock content %}
```


Podemos crear una [custom template filter](https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/) para mostrar la fecha en segundos, minutos o días, esto puede ser mostrado usando lógica *if/else* y [opciones de fechas Django(https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#date).



### Edit/Delete - Funcionalidades CRUD.

articles/urls.py
```python
from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView, # new
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('', ArticleListView.as_view(), name='article_list'),
]
```



article/views.py
```python
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView # new
from django.urls import reverse_lazy # new

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

```


Planillas articles.

```bash
(news) $ touch templates/article_detail.html
(news) $ touch templates/article_edit.html
(news) $ touch templates/article_delete.html
```


articles/templates/article_detail.html
```python
{% extends 'base.html' %}

{% block content %}
<div class="article-entry">
    <h2>{{ object.title }}</h2>
    <p>by {{ object.author }} | {{ object.date }}</p>
    <p>{{ object.body }}</p>
</div>
<p>
    <a href="{% url 'article_edit' article.pk %}">Edit</a> | <a href="{% url 'article_delete' article.pk %}">Delete</a></p>

<p>
    Back to <a href="{% url 'article_list' %}">All Articles</a>.
</p>
{% endblock content %}
```


articles/templates/article_edit.html
```python
{% extends 'base.html' %}

{% block content %}

<h1>Edit</h1>

<form action="" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button class="btn btn-info ml-2" type="submit">Update</button>
</form>

{% endblock content %}
```



articles/templates/article_delete.html
```python
{% extends 'base.html' %}

{% block content %}

<h1>Delete</h1>

<form action="" method="post">
	{% csrf_token %}
    <p>Are you sure you want to delete "{{ article.title }}"?</p>
    <button class="btn btn-danger ml-2" type="submit">Confirm</button>
</form>

{% endblock content %}
```



articles/templates/article_list.html
```python

...
<div class="card-footer text-center text-muted">
	<a href="{% url 'article_edit' article.pk %}">Edit</a> | <a href="{% url 'article_delete' article.pk %}">Delete</a>
</div>
...

```



### Create Page

*CreateView* para crear artículos nuevo, está incoporado en Django.


articles/views.py
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body', 'author',)

```


articles/urls.py
```python
from django.urls import path

from .views import (
	ArticleListView,
	ArticleUpdateView,
	ArticleDetailView,
	ArticleDeleteView,
	ArticleCreateView, # new
)

urlpatterns = [
	path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
	path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
	path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
	path('new/', ArticleCreateView.as_view(), name='article_new'), # new
	path('', ArticleListView.as_view(), name='article_list'),
]
```


Planilla "article_new.html"

```bash
(news) $ touch templates/article_new.html
```


```python
{% extends 'base.html' %}

{% block content %}

<h1>New article</h1>

<form action="" method="post">
	{% csrf_token %}
	{{ form.as_p }}
	<button class="btn btn-success ml-2" type="submit">Save</button>
</form>

{% endblock content %}
```


# 10 -- Permisos y Autorización

Existen varios problemas en el proyecto *Newspaper*.

Para ver cualquier artículo debemos tener acceso autorizado a ciertas partes del sitio, esto es diferente a *autenticación*, el cual permite registrarse e ingresar a usuarios. Autorización restrige accesos.

Django tiene una funcionalidad incorporada para autorización.


## Mejorando *CreateView*

Validación de formulario enviado. Método *form_valid*.


articles/views.py
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateViews
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body') # new

	def form_valid(self, form): # new
		form.instance.author = self.request.user
		return super().form_valid(form)

```



[Stack Overflow](https://stackoverflow.com/) es un foro que permite tener ayuda de otros programadores, preguntas-respuestas de temas de tecnologías como Django o cualquier otro framework o lenguaje.


Al crear un nuevo artículo y guardarlo, dará error. Esto es porque no se ha dado "autorización" para guardar artículos.


## Mixins

Hay que establecer algunas autorizaciones para usuarios que se hayan identificado. Acá se pueden usar *mixins*, el cual es una serie multiples herencias que Django usa para evitar duplicar código y permite personalización.

Por ejemplo, el generico [ListView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) necesita retornar una planilla, al igual que [DetailView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#detailview) y otras views. Para evitar repetir código en cada view genérico, Django usa "mixins" conocidos como [TemplateResponseMixin](https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-simple/#templateresponsemixin).


*ListView* y *DetailView* usan mixins para mostrar la planilla apropiada.

Si se revisa [Github de Django](https://github.com/django/django) se pueden ver que usa mixins en cualquier lugar.

Para restringir acceso de views solamente para usuarios ingresados, Django tiene [LoginRequired mixin](https://docs.djangoproject.com/en/4.0/topics/auth/default/#the-loginrequired-mixin), que es poderoso y extremadamente consiso.


En *articles/views.py* importamos *LoginRequiredMixin* para la clase *ArticleCreateView*. Asegurarse que los mixins estén siempre al tope de las importaciones.

articles/views.py
```python
from django.contrib.auth.mixins import LoginRequiredMixin # new

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateViews
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):  # new
    model = Article
    template_name = 'article_list.html'
	login_url = 'login'  # new


class ArticleDetailView(LoginRequiredMixin, DetailView):  # new
    model = Article
    template_name = 'article_detail.html'
	login_url = 'login'  # new


class ArticleUpdateView(LoginRequiredMixin, UpdateView):  # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
	login_url = 'login'  # new


class ArticleDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
	login_url = 'login'  # new


class ArticleCreateView(LoginRequiredMixin, CreateView):  # new
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body',)
	login_url = 'login'  # new

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

```

*login_url = 'login'  # new* - en *ArticleCreateView* redirecciona automáticamente a la página de "login" para que el usuario no autorizado ingrese sus datos para entrar a la página.



### UpdateView and DeleteView

Hasta ahora cualquier usuario puede editar y borrar artículos, se necesita restringir ese acceso a autores de esos artículos.

La clase base [View](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#view) usado en Django tiene un método interno [dispath()](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch).


Importar *PermissionDenied*, agregar método *dispatch* a *ArticleUpdateView* y *ArticleDeleteView*.


articles/views.py
```python
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.core.exceptions import PermissionDenied  # new

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateViews
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
	login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
	login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)



class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body',)
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

```


Con esto, nos mostrará error 403 cuando intentemos usar una parte del sitio web sin autorización.

Para mostrar links "edit" y "delete" a usuarios autor del artículo se debe invocar [custom template tags](https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/) para identificar si el usuario es el autor.




# Newspaper app  -- Comentarios

Existen dos formas de agregar comentarios al sitio Newspaper.
El primero sería crear una aplicación dedicada *comments* y un enlace a los *articles*, pero esto es un punto de sobre-carga para nosotros.
Lo segundo podemos agregar un modelo adicional llamado *Comment* a nuestra app *articles* y enlazarlo a modelo *Article* por medio de foreign key.


## Model

Agregar otra tabla a la base de datos llamado *Comment*, este modelo tiene relaciones foreign key many-to-one para *Article*, un artículo puede tener muchos comentarios. Tradicionalmente el nombre del campo foreign key es simplemente el modelo para enlazarlo, entonces este campo se llamara *article*. Los otros dos campos serán *comment*, *author*.

articles/models.py
```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	commets = models.CharField(max_length=140)
	author = models.ForeighKey(get_user_model, on_delete=models.CASCADE

	)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('articles_list')
```

*get_absolute_url*, retorna página principal *articles/*.


```bash
(news) $ python manage.py makemigrations articles
(news) $ python manage.py migrate
```


## Admin

articles/admin.py
```python
from django.contrib import admin

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```


Django posee formas de mostrar las relaciones 'foreign key' de una forma amistosa.

* [TabularInline](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.TabularInline)
	Muestra las referencias entre los campos en una línea.
	Para mostrar mucha información, ocupa menos espacio.

* [StackedInline](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.StackedInline)
	Muestra las referencias entre los campos en líneas por individuales.


Usando StackedInline

articles/admin.py
```python
from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.StackedInline):
	model = Comment


class ArticleAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]



admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
```



## Template

Se debe actualizar planillas *article_list.html* y *article_details.html*, para cada modelo *Article* relacionado con modelo *Comment*.

- [Following relationships backward](https://docs.djangoproject.com/en/4.0/topics/db/queries/#following-relationships-backward)


Utilizando atributo *related_name* para el modelo, el cual permite explícitamente establecer el nombre de relacion reversa.

articles/models.py
```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
	article = models.ForeignKey(
		Article,
		on_delete=models.CASCADE,
		related_name='comments',
	)
	commets = models.CharField(max_length=140)
	author = models.ForeighKey(
		get_user_model,
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('articles_list')
```


```bash
(news) $ python manage.py makemigrations articles
(news) $ python manage.py migrate
(news) $ python manage.py runserver
```



Entender las consultas (queries) toma algo de tiempo y relaciones reversas es algo confuso. Una vez que se toma control de casos básicos de consultas y relaciones, se puede explorar como filtrar los *querysets* con detalle y retornar la información exácta que se quiere.

En el fichero *article_list.html* podemos agregar los comentarios a *card-footer*, mover los links "delete" y "edit" a *card-body*.
Para acceder a cada comentario llamando a *article.comments.all* el cual mira al modelo *article*, entonces los comentarios estan relacionados con el nombre del modelo *Comment*, y selecciona todos.



articles/template/article_list.html
```python
{% extends 'base.html' %}

{% block title %}Articles{% endblock title %}

{% block content %}

{% for article in object_list %}
    <div class="card">
        <div class="card-header">
            <span class="font-weight-bold">{{ article.title }}</span> &middot;
            <span class="text-muted">by {{ article.author }} |
            {{ article.date }}</span>
        </div>
        <div class="card-body">
            <p>{{ article.body }}</p>
			<a href="{% url 'article_edit' article.pk %}">Edit</a> |
			<a href="{% url 'article_delete' article.pk %}">Delete</a>
        </div>

        <div class='card-footer'>
        	{% for comment in article.comments.all %}
        		<p>
        			<span class='font-weight-bod'>
        				{{ comment.author }} &middot;
        			</span>
        			{{ comment }}
        		</p>
        	{% endfor %}
        </div>

    </div>
    <br />
{% endfor %}

{% endblock content %}
```







# Recursos Open Source

* [Documentación Oficial Django](https://www.djangoproject.com/)
* [Django Oficial Github](https://github.com/django/django)

* [Classy Class-Based Views](https://ccbv.co.uk/)


## Recursos del autor

* [wsvincent.com](https://wsvincent.com/), author de Django for Beginners.


* [Django, PostgreSQL, and Docker](https://wsvincent.com/django-docker-postgresql/)
* [Django Social Authentication](https://wsvincent.com/django-allauth-tutorial/)
* [Django Log In Mega-Tutorial](https://wsvincent.com/django-allauth-tutorial-custom-user-model/)
* [Official Django REST Framework Tutorial - A Beginner’s Guide](https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/)
* [Django Rest Framework Tutorial](https://wsvincent.com/django-rest-framework-tutorial/)
* [Django Rest Framework with React](https://wsvincent.com/django-rest-framework-react-tutorial/)



## Otros recursos

* [Repo awesome-django](https://github.com/wsvincent/awesome-django)
* [DjangoX](https://github.com/wsvincent/djangox)
* Django REST Framework
* [DRFX](https://github.com/wsvincent/drfx)
