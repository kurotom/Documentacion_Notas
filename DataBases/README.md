# SQL

> Lenguaje de consulta estructurada, es un lenguaje de dominio específico, diseñado para administrar, y recuperar información de sistemas de gestion de base de datos relacionales. [SQL - Wikipedia](https://es.wikipedia.org/wiki/SQL)

<br>

## Páginas de información.

* [**1keydata**](https://www.1keydata.com/es/sql/)

* [**mysqltutorial**](https://www.mysqltutorial.org/mysql-basics/)

* [**guru99**](https://www.guru99.com/sql.html)

<br>

# Contenido


* [Básico](basico)
    * [SELECT](#select)
    * [NULL, NOT NULL](#valoresnull)
    * [Funciones NULL](#funcionesnull)
    * [DISTINCT](#distinct)
    * [WHERE](#where)
    * [AND OR](#and-or)
    * [IN](#in)
    * [BETWEEN](#between)
    * [LIKE](#like)
    * [ORDER BY](#ordeby)
    * [GROUP BY](#groupby)
    * [HAVING](#having)
    * [ALIAS](#alias)
    * [JOIN](#join)
    * [ON](#on)
    * [CONCAT](#concat)
    * [SUBSTR](#substr)
    * [TRIM](#trim)
    * [LIMIT](#limit)
    * [TABLA](#tablas)
        * [CREATE](#create)
        * [AS](#as)
        * [Restricciones](#restricciones)
        * [CREATE VIEW](#view)
        * [INDEX](#index)
        * [ALTER](#alter)
        * [DROP](#drop)
        * [TRUNCATE](#truncate)
        * [INSERT](#insert)
        * [UPDATE](#update)
        * [DELETE](#delete)
        * [RENAME](#rename)


* [SQL Avanzado](#avanzado)
    * [UNION](#union)
    * [UNION ALL](#unionall)
    * [INTERSECT](#intersect)
    * [MINUS](#minus)
    * [EXISTS](#exists)
    * [CASE](#case)
    * [Anidadas](#anidadas)


* [Funciones](#funciones)
    * [AVG](#avg)
    * [COUNT](#count)
    * [FIRST](#first)
    * [LAST](#last)
    * [MAX](#max)
    * [MIN](#min)
    * [SUM](#sum)
    * [UCASE](#ucase)
    * [LCASE](#lcase)
    * [MID](#mid)
    * [LENGTH](#length)
    * [ROUND](#round)
    * [FORMAT](#format)
    * [FLOOR](#floor)
    * [CEIL](#ceil)
    * [CEILING](#ceiling)
    * [DIV](#div)




* [Resumen](#resumen)

<br>

<a name="basico"></a>
# SQL Básico

<a name="select"></a>
### SELECT

Usado para realizar consultas a tablas.

#### Sintáxis

```sql
SELECT * FROM nombre_tabla;

SELECT name, age, skills, city FROM date_personal;
```

<br>

<a name="valoresnull"></a>
### NULL, NOT NULL

Representa valores desconocidos. Estos no se pueden operar con operadores aritméticos, solamente se puede usar **IS**, **IS NOT**.

#### Sintáxis

```sql
SELECT * FROM personas WHERE apellido2 IS NULL;

SELECT name FROM personas WHERE name IS NOT NULL;
```

<br>

<a name="funcionesnull"></a>
### Funciones NULL

Si se quiere cambiar un **NULL** por algún valor, se debe usar **IFNULL**, **COALESCE**.

#### Sintáxis

```sql
SELECT producto, preciounidad * (unidadesstock + IFNULL(unidadespedido, 0) FROM productos 
```

O usar:

```sql
SELECT producto, preciounidad * (unidadesstock + COALESCE(unidadespedido, 0) FROM productos 
```

En esta caso se cambio el valor NULL por 0.

<br>

<a name="distinct"></a>
### DISTINCT

Devuelve los valores únicos de una consulta a una tabla.

#### Sintáxis

```sql
SELECT DISTINCT columna_nombre FROM nombre_tabla;
```

#### Ejemplo

```sql
SELECT DISTINCT nombre FROM personal;
```

<br>

<a name="where"></a>
### WHERE

Condicionante de consulta.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla WHERE "condicion";
```

#### Ejemplo

```sql
SELECT nombre, skills FROM personal WHERE name = 'Bob';
```

<br>

<a name="and-or"></a>
### AND - OR

Clausula usada con `WHERE`.
"Pipe" para condicionante `WHERE`, usado para realizar múltiples condicionales en una consulta.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla WHERE "condición" AND "condición";

SELECT columna_nombre FROM nombre_tabla WHERE "condición" OR "condición";
```

Operador de Comparación  :  =, >, <, >=, <=

Operador Distinto: <>

#### Ejemplo

```sql
SELECT name, age FROM personal WHERE name = 'Bob' AND (age > 20 AND age < 30);
```

<br>

<a name="in"></a>
### IN

Clausula usada con `WHERE`.
Similar a la sintaxis `WHERE columna_nombre = "valor"`, pero para múltiples valores.
Se usa para múltiples valores.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla WHERE columna_nombre IN ("valor1", "valor2", ...);
```

#### Ejemplo

```sql
SELECT * FROM personal WHERE name IN ('Bob', 'Katy');
```

<br>

<a name="between"></a>
### BETWEEN

Clausula usada con `WHERE`.
Permite selección entre un rango de valores.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla WHERE columna_nombre BETWEEN "valor1" AND "valor2";
```

#### Ejemplo

```sql
SELECT * FROM personal WHERE skills BETWEEN 1 AND 3;
```

<br>

<a name="like"></a>
### LIKE

Clausula usada con `WHERE`.
Busca un patrón en la consulta realizada.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla WHERE columna_nombre LIKE patrón;
```

#### Uso de WILDCARDS

%  :  sustituye a cero o más caracteres
_  :  sustituye a 1 carácter cualquiera
[lista]  :  sustituye a cualquier carácter de la lista
[^lista] o [!lista]  :  sustituye a cualquier carácter excepto los caracteres de la lista

Donde, patrón:
    * 'C_A' - todas las coincidencias que comienzan con "C" y terminan con "A", ejemplo: "casa".
    * 'CEB%' - todas las coincidencias que comienzan con "CEB", ejemplo: "cebolla".
    * '%AN' - todas las coincidencias que terminan en "AN", ejemplo: "pan".
    * '%as%' - todas las coincidencias que contienen "as", ejemplo: "casa", "brasas".

#### Ejemplo

```sql
SELECT * FROM personal WHERE name LIKE %%;
```

<br>

<a name="ordeby"></a>
### ORDER BY

Ordena el resultado de la consulta, ascendente o descendente.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla ORDER_BY columna_nombre [ASC, DESC];

SELECT columna_nombre FROM nombre_tabla WHERE condición ORDER BY columna_nombre [ASC, DESC];

SELECT columna_nombre FROM nombre_tabla WHERE condición ORDER BY columna_nombre1 [ASC, DESC] columna_nombre2 [ASC, DESC];
```

#### Ejemplo

```sql
SELECT name, age FROM personal ORDER BY age DESC name ASC;
```

<br>

<a name="groupby"></a>
### GROUP BY

Agrupa por columna la consulta realizada.

#### Sintáxis

```sql
SELECT 'columna_nombre1', SUM('columna_nombre2') FROM nombre_tabla GROUP BY 'nueva_Columna';
```

#### Ejemplo

```sql
SELECT store_name SUM(Sales) FROM Store_info GROUP BY store_name;
```

<br>

<a name="having"></a>
### HAVING

Se usa en reemplazo de `WHERE` porque este no se puede usar con funciones agregadas.
Puede o no incluir `GROUP BY`.

#### Sintáxis

```sql
SELECT columna_nombre FROM nombre_tabla HAVING (condicion de función aritmética);
```

#### Ejemplo

```sql
SELECT Store_Name, SUM(Sales) FROM Store_Information GROUP BY Store_Name HAVING SUM(Sales) > 1500;
```

<br>

<a name="alias"></a>
### Alias

Se pueden usar Alias de columna o Alias de tabla, existen para ayudar en la organización del resultado.

#### Sintáxis

```sql
SELECT "alias_tabla"."columna_nombre" "alias_columna" FROM "nombre_tabla" "alias_tabla";
```

#### Ejemplo

```sql
SELECT A1.store_name store,SUM(A1.sales) "Total Sales" FROM store_information A1 GROUP BY A1.store_name;
```

<br>

<a name="join"></a>
### JOIN

Se usa para unir dos o más tablas basado en una columna relacionada entre ellas.
Se puede usar cualquier condicionante anterior, por ejemplo `WHERE`.

#### Sintáxis

```sql
SELECT columna_nombre1 FROM nombre_tabla1 INNER JOIN nombre_tabla2 ON nombre_tabla1.columna_nombre = nombre_tabla2.columna_nombre;

SELECT columna_nombre FROM nombre_tabla1 LEFT JOIN nombre_tabla2 ON nombre_tabla1.columna_nombre = nombre_tabla2.columna_nombre;

SELECT columna_nombre FROM nombre_tabla1 RIGHT JOIN nombre_tabla2 ON nombre_tabla1.columna_nombre = nombre_tabla2.columna_nombre;

SELECT columna_nombre FROM nombre_tabla1 FULL JOIN nombre_tabla2 ON nombre_tabla1.columna_nombre = nombre_tabla2.columna_nombre;
```

* INNER JOIN  :  retorna registro que coincidan en ambas tablas.
* LEFT JOIN  :  retorna registros desde la tabla izquierda y los registros coinciden desde la tabla derecha.
* RIGHT JOIN  :  retorna los registros desde la tabla derecha, y los registros coincidentes desde la tabla izquierda.
* FULL JOIN  :  retorna los registros cuando coincidan entre ambas tablas (izquierda y derecha).

<br>

<a name="concat"></a>
### ON

*ON*, al usar con *JOIN*, para coincidir con las mismas columnas, por ejemplo, ForeignKeys entre tablas.

```sql
SELECT ForeignTableDemo.Id, ForeignTableDemo.Name, PrimaryTableDemo.Address from ForeignTableDemo JOIN PrimaryTableDemo ON ForeignTableDemo.FK = PrimaryTableDemo.FK;
```


<br>

<a name="concat"></a>
### CONCAT

Concatenar los resultados de varios campos diferentes.

  * MySQL: CONCAT()

#### Sintáxis

```sql
CONCAT (cadena1, cadena2, cadena3, ..)
```

#### Ejemplo

MySQL:

```sql
SELECT CONCAT (region_name, store_name) FROM geography WHERE store_name = 'Boston';
```


<br>

<a name="substr"></a>
### SUBSTR

La función de subcadena SQL se utiliza para tomar una parte de los datos.

#### Sintáxis

```sql
SUBSTR (str, pos)

SUBSTR (str, pos, len)
```

#### Ejemplo

```sql
SELECT SUBSTR (store_name, 3) FROM geography WHERE store_name = 'Los Angeles';

SELECT SUBSTR (Store_Name, 2, 4) FROM Geography WHERE Store_Name = 'San Diego';
```

<br>

<a name="trim"></a>
### TRIM

Eliminar un prefijo o sufijo determinado de una cadena.

* MySQL: TRIM(), RTRIM(), LTRIM()

#### Sintáxis

```sql
SELECT TRIM(' sample ');

SELECT LTRIM(' sample ');

SELECT RTRIM(' sample ');
```

<br>

<a name="limit"></a>
### LIMIT

Especifica el número de filas a mostrar.

#### Sintáxis

```sql
SELECT * FROM personas LIMIT 2;
```

<br>

<a name="tablas"></a>
# Manipulación de Tablas

<a name="create"></a>
## Create Table

Creación de tablas que almacenan información.

#### Sintáxis

```sql
CREATE TABLE nombre_tabla (
  columna_nombre1 datatype,
  columna_nombre2 datatype,
  columna_nombreX datatype,
);
```

datatype:

* CHAR(size)  :  cualquier dato de largo 'size', 0-255
* VARCHAR(size)  : variable de largo 'size', 0-65535
* TEXT(size)  :  string largo, 65535
* INT(size)  :  numero entero negativo o positivo
* FLOAT(size)  :  numero punto flotante
* DATE  :  YYYY-MM-DD
* DATETIME  :  YYYY-MM-DD hh:mm:ss
* TIMESTAMP  :  timestamp Unix
* TIME  :  HH:MM:SS
* YEAR  :  YYYY
* NOW  :  fecha actual


#### Ejemplo

```sql
CREATE TABLE personal (
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  edad INT(100),
  nacimiento DATE
);
```

<a name='as'></a>
## CREATE TABLE **AS**

Crear una tabla desde otra tabla existente, copiando los datos contenidos en esta última.

### Sintáxis

Crear una tabla desde otra tabla.
```sql
CREATE TABLE new_table AS (SELECT * FROM old_table);
```

Crear tabla desde otra tabla usando algunas columnas.
```sql
CREATE TABLE new_table AS (SELECT column_1, column2, column_N FROM old_table);
```

Crear tabla desde otras tablas.
```sql
CREATE TABLE new_table AS (SELECT column_1, column2, column_N FROM old_table_1, old_table_2, old_table_N);
```



<br>

<a name="restricciones"></a>
### Restricciones o Constraint

Las restricciones se deben ingresar cuando se crea una tabla, luego se puede cambiar usando `ALTER TABLE`.

* NOT NULL  :  valor no nulo, por defecto se aceptan valores NULL.
* UNIQUE  :  valor único, no se repiten.
* CHECK  :  valores de una columna cumplan condiciones.
* PRIMARY KEY  :  identificar el campo de llave identificador único.
* FOREIGN KEY  :  valor numérico que apunta a otro campo PRIMARY KEY de otra tabla.
* DEFAULT  :  establece un valor por defecto en una columna, se puede usar en CREATE TABLE o ALTER TABLE.

* AUTO INCREMENT  :  permite generar un número único cuando insertamos un nuevo registro en la tabla.

#### Sintáxis

```sql
CREATE TABLE Customer (
  SID integer NOT NULL,
  Last_Name varchar (30) NOT NULL,
  First_Name varchar(30)
);


CREATE TABLE Customer (
  SID integer NOT NULL,
  Last_Name varchar (30) NOT NULL,
  First_Name varchar(30)
);


CREATE TABLE Customer (
  SID integer CHECK (SID > 0),
  Last_Name varchar (30),
  First_Name varchar(30)
);
```

MySQL
```sql
CREATE TABLE Customer (
  SID integer,
  Last_Name varchar(30),
  First_Name varchar(30),
  PRIMARY KEY (SID)
);
```

MySQL
```sql
CREATE TABLE ORDERS (
  Order_ID integer,
  Order_Date date,
  Customer_SID integer,
  Amount double,
  PRIMARY KEY (Order_ID),
  FOREIGN KEY (Customer_SID) REFERENCES CUSTOMER (SID)
);
```


<a name="view"></a>
### CREATE VIEW

Tablas virtuales, se construyen a partir de una tabla existente, no almacena datos físicamente, algo así como un enlace simbólico a una tabla.

#### Sintáxis

```sql
CREATE VIEW "nombre_tabla_virtual" AS instrucciones_sql;
```

#### Ejemplo

```sql
CREATE VIEW nombre_tabla_virtual AS SELECT name, age, city FROM persons;
```

<br>

<a name="index"></a>
### CREATE INDEX

Los índices ayudan a obtener datos de tables de forma más rápida, pudiendo cubrir una o más de una columna.
Es recomendable crear índices en tablas.

#### Sintáxis

```sql
CREATE INDEX índice_nombre ON nombre_tabla (columna_nombre);
```

El uso del prefijo `IDX_` para "índice_nombre" es una práctica recomendada, o el uso de cualquier prefijo que identifique un índice.

#### Ejemplo

```sql
CREATE INDEX índice_personas ON personal (name, skills);
```

<br>

<a name="alter"></a>
### ALTER table

Altera o modifica una tabla, agregando, eliminando, cambiando nombre de columna o el tipo de datos.

* ADD  :  agrega una columna, ` ADD "columna_2" "tipo_de_datos"`.
* DROP  :  elimina una columna, ` DROP "columna_2"`.
* CHANGE  :  cambia el nombre de columna, ` CHANGE "antiguo_nombre" "nuevo_nombre" "tipo_de_datos"`.
* MODIFY  :  cambia el tipo de datos de una columna, ` MODIFY "columna_2" "nuevo_tipo_dato"`.

#### Sintáxis

```sql
ALTER TABLE nombre_tabla ADD columna_X varchar(50);

ALTER TABLE nombre_tabla ADD PRIMARY KEY (columna);

ALTER TABLE nombre_tabla DROP columna_X;

ALTER TABLE nombre_tabla CHANGE columna_X columna_Y varchar(50);

ALTER TABLE nombre_tabla MODIFY columna_Y int(20);
```

<br>

<a name='rename'></a>
### RENAME

Cambia el nombre de una tabla o de columna.

#### Sintáxis

```sql
ALTER TABLE nombre_tabla RENAME nuevo_nombre;
ALTER TABLE nombre_tabla RENAME COLUMN viejo_nombre TO nuevo_nombre;
```

<br>

<a name="drop"></a>
### DROP TABLE

Elimina una tabla completa, todos los datos que contiene se pierden.

### Sintáxis

```sql
DROP TABLE "nombre_tabla";
```

<br>

<a name="truncate"></a>
### TRUNCATE TABLE;

Elimina parte de los datos de una tabla, NO la tabla completa a diferenia de DROP.

#### Sintáxis

```sql
TRUNCATE TABLE "nombre_tabla";
```

<br>

<a name="insert"></a>
### INSERT INTO

Inserta información en una tabla especificada.
Se puede usar cláusulas `WHERE`, `GROUP BY`, `HAVING`, también `JOIN` y `ALIAS`.

#### Sintáxis

```sql
INSERT INTO "nombre_tabla" (
  "columna_1",
  "columna_2",
  "columna_X",
) VALUES (
  'data1',
  'data2',
  'dataX'
);
```

<br>

<a name="update"></a>
### UPDATE

Actualiza valor de un item dentro columna en una tabla.

#### Sintáxis

```sql
UPDATE "nombre_tabla" SET "columna_nombre1" = "nuevo Valor1", "columna_nombre2" = "nuevo Valor2" WHERE "condición";
```

#### Ejemplo

```sql
UPDATE personal SET age = 30 WHERE nombre = 'Vito' AND apellido = "Corleone";
```

<br>

<a name="delete"></a>
### DELETE FROM

Para borrar un registro de una tabla.

#### Sintáxis

```sql
DELETE FROM "nombre_tabla" WHERE "condición";
```

#### Ejemplo

```sql
DELETE FROM personal WHERE nombre = 'Fredo' and apellido = 'Corleone';
```

<br>

<a name="avanzado"></a>
# SQL Avanzado

Palabras claves:

* UNION  :  selecciona unos valores, combina los resultados de dos consultas juntas.

* UNION ALL  :  selecciona todos los valores, combina los resultados de dos consultas juntas.

* INTERSECT  :  opera en dos instrucciones SQL, actúa como operador `AND`, es decir si el valor existe entre ambas instrucciones.

* MINUS  :  toma todos los resultados de la primera instrucción SQL y luego sustrae aquellos que se encuentran presentes en la segunda instrucción SQL.

* EXISTS  :  verifica si la consulta interna arroja alguna fila.

* CASE  :  se utiliza para brindar un tipo de lógica "si entonces otro".

* Consultas Anidadas  :  instrucciones SQL dentro de otra, al usar `WHERE` o `HAVING`.

<a name="union"></a>
## UNION

```sql
[Instrucción SQL 1] UNION [Instrucción SQL 2];
```

## Ejemplo

```sql
SELECT Txn_Date FROM Store_Information UNION SELECT Txn_Date FROM Internet_Sales;
```

<a name="unionall"></a>
## UNION ALL

```sql
[Instrucción SQL 1] UNION ALL [Instrucción SQL 2];
```

## Ejemplo

```sql
SELECT Txn_Date FROM Store_Information UNION ALL SELECT Txn_Date FROM Internet_Sales;
```

<a name="intersect"></a>
## INTERSECT

```sql
[Instrucción SQL 1] INTERSECT [Instrucción SQL 2];
```

## Ejemplo

```sql
SELECT Txn_Date FROM Store_Information INTERSECT SELECT Txn_Date FROM Internet_Sales;
```

<a name="minus"></a>
## MINUS

```sql
[Instrucción SQL 1] MINUS [Instrucción SQL 2];
```

## Ejemplo

```sql
SELECT Txn_Date FROM Store_Information MINUS SELECT Txn_Date FROM Internet_Sales;
```

<a name="exists"></a>
## EXISTS

```sql
SELECT "nombre1_columna" FROM "nombre1_tabla" WHERE EXISTS (
  SELECT * FROM "nombre2_tabla" WHERE "Condición"
);
```

## Ejemplo

```sql
SELECT SUM(Sales) FROM Store_Information WHERE EXISTS (
  SELECT * FROM Geography WHERE region_name = 'West'
);
```

<a name="case"></a>
## CASE

```sql
SELECT CASE ("nombre_columna")
  WHEN "condición1" THEN "resultado1"
  WHEN "condición2" THEN "resultado2"
  ...
  [ELSE "resultadoN"]
  END
FROM "nombre_tabla";
```

"condición" puede ser un valor estático o una expresión. `ELSE` es opcional.

## Ejemplo

```sql
SELECT Store_Name, CASE Store_Name
  WHEN 'Los Angeles' THEN Sales * 2
  WHEN 'San Diego' THEN Sales * 1.5
  ELSE Sales
  END
"Nuevas Ventas",
Txn_Date
FROM Store_Information;
```

<a name="anidadas"></a>
## Consultas Anidadas

```sql
SELECT "nombre1_columna" FROM "nombre1_tabla" WHERE "nombre2_columna" [Operador de Comparación]
(SELECT "nombre3_columna"
FROM "nombre2_tabla"
WHERE "Condición");
```

Operador de Comparación  :  =, >, <, >=, <=

Operador Distinto: <>

Fuera de paréntesis son consultas externas, dentro del paréntesis son consultas internas.

## Ejemplo

```sql
SELECT SUM(Sales) FROM Store_Information WHERE Store_Name IN (
  SELECT Store_Name FROM Geography WHERE Region_Name = 'West'
);
```

<br>



<a name="funciones"></a>
# Funciones

Permite realizar cálculos matemáticos, como, mínimo, máximo, contar, promedio.

* AVG
* COUNT
* MAX
* MIN
* SUM

### Sintáxis

```sql
SELECT nombre_función('columna_nombre') FROM nombre_tabla;
```
<a name="avg"></a>
### AVG

```sql
SELECT AVG(age) FROM personal;
```

<a name="count"></a>
### COUNT

```sql
SELECT COUNT(name) FROM personal;

SELECT COUNT(DISTINCT name) FROM personal;
```

<br>

<a name="first"></a>
### FIRST

Devuelve el primer valor de la columna seleccionada.

#### Sintáxis

```sql
SELECT FIRST(precio) FROM pedidos;
```

<br>

<a name="last"></a>
### LAST

Devuelve el último valor de la columna seleccionada.

#### Sintáxis

```sql
SELECT LAST(precio) FROM pedidos;
```

<br>

<a name="max"></a>
### MAX

Retorna el número mayor de la columna seleccionada.

#### Sintáxis

```sql
SELECT MAX(precio) FROM pedidos;
```

<br>

<a name="min"></a>
### MIN

Retorna el número menor de la columna seleccionada.

#### Sintáxis

```sql
SELECT MIN(precio) FROM pedidos;
```

<br>

<a name="sum"></a>
### SUM

Retorna una suma de los valores de la columna seleccionada, deben ser de tipo número.

#### Sintáxis

```sql
SELECT sum(precio) FROM pedidos;
```

<br>

<a name="ucase"></a>
### UCASE

Convierte string en mayúscula, campo tipo string.

#### Sintáxis

```sql
SELECT UCASE(nombre) FROM pedidos;
```

<br>

<a name="lcase"></a>
### LCASE

Convierte string en minuscula, capo tipo string.

#### Sintáxis

```sql
SELECT LCASE(nombre) FROM pedidos;
```

<br>

<a name="mid"></a>
### MID

Extrae carácteres de un campo de texto, es decir, corta el string.
Recibe tres parámetros: el campo, INT_inicio, INT_final.

#### Sintáxis

```sql
 SELECT MID(cliente,1,3) FROM pedidos;
```

<br>

<a name="length"></a>
### LENGTH

Calcula la longitud del string del campo seleccionado,  tipo texto.

#### Sintáxis

```sql
SELECT LENGTH(cliente) AS cliente FROM pedidos;
```

<br>

<a name="round"></a>
### ROUND

Redondea el valor del campo numérico en decimales especificados.
Recibe dos parámetros: campo, int_cantidad_decimales.

#### Sintáxis

```sql
SELECT ROUND(precio,0) AS r_precio FROM pedidos;
```

<br>

<a name="format"></a>
### FORMAT

Usado para dar formato en el campo seleccionado.
Se le entrega dos parámetros: columna, formato.

#### Sintáxis

```sql
SELECT producto, precio, FORMAT(NOW(), ‘YYYY-MM-DD’) AS fecha FROM productos;
```

<br>

<a name="floor"></a>
### FLOOR

Retorna el valor entero más grande que será igual o menor que el de un número de entrada dado.

#### Sintáxis

```sql
SELECT FLOOR(numero);
```

<br>


<a name="ceil"></a>
### CEIL

Retorna el valor entero más pequeño que es mayor o igual que un número.

#### Sintáxis

```sql
SELECT CEIL(numero);
```

<br>

<a name="ceiling"></a>
### CEILING

La función devuelve el valor entero más pequeño que es mayor o igual que un número. Nota: Esta función es igual a la función CEIL().

#### Sintáxis

```sql
SELECT CEILING(numero);
```

<br>

<a name="div"></a>
### DIV

Se utiliza para la división de enteros (x se divide por y). Se devuelve un valor entero.

#### Sintáxis

```sql
SELECT 8 DIV 3;
```

<br>





<br>

---

<br>

<a name="resumen"></a>
# Resumen Sintáxis SQL

Select
```sql
SELECT "nom de colonne" FROM "nombre_tabla";
```

Distinct
```sql
SELECT DISTINCT "nombre_columna"
FROM "nombre_tabla";
```

Where
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
WHERE "condition";
```

And/Or
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
WHERE "condición simple"
{[AND|OR] "condición simple"}+;
```

In
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
WHERE "nombre_columna" IN ('valor1', 'valor2', ...);
```

Between
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
WHERE "nombre_columna" BETWEEN 'valor1' AND 'valor2';
```

Like
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
WHERE "nombre_columna" LIKE {patrón};
```

Order By
```sql
SELECT "nombre_columna"
FROM "nombre_tabla"
[WHERE "condición"]
ORDER BY "nombre_columna" [ASC, DESC];
```

Count
```sql
SELECT COUNT("nombre_columna")
FROM "nombre_tabla";
```

Group By
```sql
SELECT "nombre_columna 1", SUM("nombre_columna 2")
FROM "nombre_tabla"
GROUP BY "nombre_columna 1";
```

Having
```sql
SELECT "nombre_columna 1", SUM("nombre_columna 2")
FROM "nombre_tabla"
GROUP BY "nombre_columna 1"
HAVING (condición de función aritmética);
```

Create Table
```sql
CREATE TABLE "nombre_tabla"
("columna 1" "tipo_de_datos_para_columna_1",
"columna 2" "tipo_de_datos_para_columna_2",
... );
```

Drop Table
```sql
DROP TABLE "nombre_tabla";
```

Truncate Table
```sql
TRUNCATE TABLE "nombre_tabla";
```

Insert Into
```sql
INSERT INTO "nombre_tabla" ("colonne 1", "colonne 2", ...)
VALUES ("valor 1", "valor 2", ...);
```

Update
```sql
UPDATE "nombre_tabla"
SET "colonne 1" = [nuevo valor]
WHERE "condición";
```

Delete From
```sql
DELETE FROM "nombre_tabla"
WHERE "condición";
```
