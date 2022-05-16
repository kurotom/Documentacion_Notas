# Addons Heroku

Son componentes, servicios o piezas de infraestructura que se mantienen completamente para ti, ya sea por un proveedor externo o por Heroku.

[Lista de addons](https://devcenter.heroku.com/categories/add-on-documentation)

Componentes como almacenamiento de información, monitoreo, análisis, procesamiento de información, y más. Todo esto existe para que los desarrolladores se enfoquen en las lógicas de sus aplicaciones, y no agreguen complejidad adicional para mantener los servicios en correcto estando en un ambiente de producción.

Los Addons pueden ser instalados por medio del dashboard Heroku o por CLI, no todos son gratis, revisar bien la información.

Cada elemento addon tiene instrucciones para que se puedan agregar a la aplicación.

Por ejemplo, agregar Postgress a la aplicación Heroku, después de finalizar la instalación, se debe configurar la variable de entorno *DATABASE_URL* que es la dirección de la base de datos.


## Instalación CLI

Se puede instalar mediante el uso del comando *heroku addons:create SERVICE*, que aprovisionará el complemento con su proveedor, le dará al complemento un nombre global y le dará un alias predeterminado en su aplicación, y establecerá cualquier variable de configuración que proporcione el complemento usando nombres basados en ese alias.

Por ejemplo:

```
heroku addons:create heroku-postgresql:<PLAN_NAME>
```

Donde *PLAN_NAME* es el nombre del plan seleccionado según lo revisado en la documentación de heroku-postgress.


Luego se debe establecer la variable con nombre *DATABASE_URL*, listo todo, ahora se tiene una base de datos, vacía, asignada a la aplicación.

[Documentación Heroku Postgresql](https://devcenter.heroku.com/articles/heroku-postgresql).


## Usando dashboard Heroku

Dentro del panel de control de la aplicación en Heroku, se dirige a la pestaña **Resources**, luego a **Find more add-ons**, busca el add-on que quiera, luego presione el botón **Install**, seleccione el plan que va a usar, seleccione la aplicación a la cuál se le agregará el addon, finalmente **Submit Order Form**.

Con eso se tendrá el addon agregado a la aplicación.
