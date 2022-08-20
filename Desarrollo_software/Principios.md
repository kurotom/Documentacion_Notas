# Principios de diseño y desarrollo

* DRY - Don't Repeat Yourself.

Promueve la reducción de la duplicación, debido a que esta aumenta la dificultad en los cambios y evolución posterior, perjudicando la claridad y crea espacios para inconsistencias.


* GRASP - object-oriented design General Responsibility Assignment Software Patterns.

Serie de buenas prácticas de diseño de software:
* Experto
La responsabilidad de la creación de un objeto o implementación debe caer en la clase que conoce toda la información necesaria.

* Creador
No ayuda a identificar quién debe ser responsable de la creación (o instaciación) de nuevos objetos o clases.
La nueva instancia deberá ser creada por la clase que:
  - Tiene la información necesaria para realizar la creación del objeto, o
  - Usa directamente las instancias creadas del objeto, o
  - Almacena o maneja varias instancias de la clase
  - Contiene o agrega la clase.

* Controlador
Sirve como intermediario entre determinada interfaz y el algoritmo que la implementa, de tal forma que recibe los datos del usuario y es la que los envía a distintas clases según el método llamado.

* Alta cohesión y bajo acoplamiento
Mayor grado de cohesión con un menor grado de acoplamiento. De esta forma se tiene menor dependencia y se especifican los propósitos de cada objeto en el sistema.

Alta cohesión.
  - Cohesión Coincidente: El módulo realiza múltiples tareas, sin ninguna relación entre ellas.
  - Cohesión Lógica: El módulo realiza múltiples tareas relacionadas, pero, en tiempo de ejecución, sólo una de ellas será llevada a cabo.
  - Cohesión Temporal: Las tareas llevadas a cabo por un módulo tienen, como única relación "que deben ser ejecutadas al mismo tiempo".
  - Cohesión de Procedimiento: La única relación que guardan las tareas de un módulo es que corresponden a una secuencia de pasos propia del “producto”.
  - Cohesión de Comunicación: Las tareas corresponden a una secuencia de pasos propia del “producto” y todas afectan a los mismos datos.
  - Cohesión de Información: Las tareas llevadas a cabo por un módulo tienen su propio punto de arranque, su codificación independiente y trabajan sobre los mismos datos. El ejemplo típico: OBJETOS
  - Cohesión Funcional: Cuando el módulo ejecuta una y sólo una tarea, teniendo un único objetivo a cumplir, se dice que tiene Cohesividad Funcional.

Bajo acoplamiento
  - Acoplamiento de Contenido: Cuando un módulo referencia directamente el contenido de otro módulo. (En lenguajes de alto nivel es muy raro)
  - Acoplamiento Común: Cuando dos módulos acceden (y afectan) a un mismo valor global.
  - Acoplamiento de Control: Cuando un módulo le envía a otro un elemento de control que determina la lógica de ejecución del mismo.

* Polimorfismo
Siempre que se tenga que llevar a cabo una responsabilidad que dependa del tipo, se tiene que hacer uso del polimorfismo.

* Fabricación pura
Se da en las clases que no representan un ente u objeto real del dominio del problema, sino que se ha creado intencionadamente para disminuir el acoplamiento, aumentar la cohesión y/o potenciar la reutilización del código.

* Indirección
El patrón de indirección nos aporta bajar el acoplamiento entre dos clases asignando la responsabilidad de la mediación entre ellos a un tercer elemento (clase) intermedio.

* Variaciones Protegidas
Es el principio fundamental de protegerse del cambio, de tal forma que todo lo que preveamos en un análisis previo que es susceptible de modificaciones, lo envolvamos en una interfaz, utilizando el polimorfismo para crear varias implementaciones y posibilitar implementaciones futuras, de manera que quede lo menos ligado posible a nuestro sistema, de forma que cuando se produzca la variación, nos repercuta lo mínimo. Forma parte de los patrones Grasp avanzados.


* KISS - Keep It Simple Stupid,1960 Kelly Johnson.

La mayoría de sistemas funcionan mejor si se mantienen simples que si se hacen complejos, la simplicidad debe ser mantenida como clave de diseño.

* YAGNI - You Aren't Gonna Need It.

No vas a necesitarlo, consiste en que no se debe agregar nunca una funcionalidad excepto cuando sea necesaria.
Evita:
* Perder tiempo
* Evitar depuraciones, documentacion, y soporte, adicionales.
* Impone límites que afectan al futuro.
* Hasta que no está definido para qué se necesita es imposible saber qué debe hacer (funcionalidades nuevas no funcionen correctamente).
* Evita derivar en código inflado.
* Características pueden pasar por alto, si no se utiliza junto con un VCS (Version control system).
* Las nuevas funcionalidades pueden generar efecto "bola de nieve", consumiendo recurso y tiempo, sin beneficios.
