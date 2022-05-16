# Database fuera de Heroku

Para poder usar una base de datos externa a la que asigna Heroku, ésta se debe eliminar de la aplicación, el "addon" que se agrega automáticamente es la base de datos Postgresq.

Cuando desplegué una aplicación con base de datos externa a Heroku me generaba problemas, la tuve que eliminar y todo funcionaba como debería.

## ¿Cómo eliminar?

En el dashboard Heroku, dirigirse a la seccion **Resources**, en la parte **Add-ons** aparecerán todas las que están agregadas a la aplicación, presionar el botón que contiene una flecha hacia arriba y abajo, seleccionar **Delete Add-on**, ingresar la frase que se encuetra demarcada y presionar **Remove add-on**.

Y listo ahora la aplicación esta libre y si la configuración de la aplicación está correcta, funcionará con la base de datos externa.
