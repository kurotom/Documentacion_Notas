1. Obtener los datos completos de los empleados.

```
SELECT * FROM empleados;
```

2. Obtener los datos completos de los departamentos.

```
SELECT * FROM departamentos;
```

3. Obtener los datos de los empleados con cargo ‘Secretaria’.

```
SELECT * FROM empleados WHERE cargoE = 'Secretaria';
```

4. Obtener el nombre y salario de los empleados.

```
SELECT nomEmp, salEmp FROM empleados;
```

5. Obtener los datos de los empleados vendedores, ordenado por nombre.

```
SELECT * FROM empleados WHERE cargoE = '
```

6. Listar el nombre de los departamentos.

```
SELECT nombreDpto FROM departamentos;
```

7. Obtener el nombre y cargo de todos los empleados, ordenado por salario.

```
mysql> SELECT nomEmp, cargoE from empleados ORDER BY salEmp ASC;

```

8. Listar los salarios y comisiones de los empleados del departamento 2000, ordenado por comisión.

```
mysql> SELECT salEmp, comisionE from empleados WHERE codDepto = 2000 ORDER BY comisionE ASC;
```

9. Listar todas las comisiones.

```
SELECT comisionE FROM empleados;
```

10. Obtener el valor total a pagar que resulta de sumar a los empleados del departamento 3000 una bonificación de 500.000, en orden alfabético del empleado

```
SELECT SUM(salEmp + 500000) FROM empleados WHERE codDepto = 3000 ORDER BY nomEmp ASC;
```

11. Obtener la lista de los empleados que ganan una comisión superior a su sueldo.

```
mysql> SELECT nomEmp FROM empleados WHERE comisionE > salEmp;
```

12. Listar los empleados cuya comisión es menor o igual que el 30% de su sueldo.

```
mysql> SELECT nomEmp FROM empleados WHERE comisionE <= ((salEmp * 30) / 100);
```

13. Elabore un listado donde para cada fila, figure ‘Nombre’ y ‘Cargo’ antes del valor respectivo para cada empleado.

```
mysql> SELECT nomEmp AS 'Nombre', cargoE AS 'Cargo' FROM empleados;
```

14. Hallar el salario y la comisión de aquellos empleados cuyo número de documento de identidad es superior al ‘19.709.802’.

```
mysql> SELECT salEmp, comisionE FROM empleados WHERE nDIEmp > '19.709.802';
```

15. Muestra los empleados cuyo nombre empiece entre las letras J y Z (rango).
Liste estos empleados y su cargo por orden alfabético.

```
mysql> SELECT nomEmp, cargoE FROM empleados WHERE nomEmp REGEXP '^[J-Z]'
ORDER BY nomEmp ASC;
```

16. Listar el salario, la comisión, el salario total (salario + comisión), documento de identidad del empleado y nombre, de aquellos empleados que tienen comisión superior a 1.000.000, ordenar el informe por el número del documento de identidad.

```
mysql> SELECT salEmp AS 'Salario', comisionE AS 'Comisión', salEmp + comisionE AS 'Total', nDIEmp AS 'ID_empleado', nomEmp AS 'Nombre'  FROM empleados WHERE comisionE > '1.000.000' ORDER BY nDIEmp ASC;
```

17. Obtener un listado similar al anterior, pero de aquellos empleados que NO tienen comisión

```
mysql> SELECT salEmp AS 'Salario', comisionE AS 'Comisión', salEmp + comisionE AS 'Total', nDIEmp AS 'ID_empleado', nomEmp AS 'Nombre'  FROM empleados WHERE comisionE = 0 ORDER BY nDIEmp ASC;
```

18. Hallar los empleados cuyo nombre no contiene la cadena «MA»

```
mysql> SELECT nomEmp FROM empleados WHERE nomEmp NOT LIKE '%MA%';
```

19. Obtener los nombres de los departamentos que no sean “Ventas” ni “Investigación” NI ‘MANTENIMIENTO’.

```
mysql> SELECT nombreDpto from departamentos WHERE nombreDpto != 'VENTAS' AND nombreDpto != 'INVESTIGACIÓN' AND nombreDpto != 'MANTENIMIENTO';
```

20. Obtener el nombre y el departamento de los empleados con cargo ‘Secretaria’ o ‘Vendedor’, que no trabajan en el departamento de “PRODUCCION”, cuyo salario es superior a $1.000.000, ordenados por fecha de incorporación.

```
mysql> SELECT nomEmp, nombreDpto FROM empleados JOIN departamentos WHERE empleados.codDepto = departamentos.codDepto AND nombreDpto = 'VENTAS' OR nombreDpto = 'SECRETARIA' AND nombreDpto != 'PRODUCCIÓN' AND salEmp > '1.000.000' ORDER BY fecIncorporacion ASC;
```

21. Obtener información de los empleados cuyo nombre tiene exactamente 11 caracteres

```
mysql> SELECT nomEmp AS 'Nombre - (length 11)' FROM empleados WHERE LENGTH(nomEmp) = 11;
```

22. Obtener información de los empleados cuyo nombre tiene al menos 11 caracteres.

```
mysql> SELECT nomEmp AS 'Nombre - <= 11' FROM empleados WHERE LENGTH(nomEmp) <= 11;
```

23. Listar los datos de los empleados cuyo nombre inicia por la letra ‘M’, su salario es mayor a $800.000 o reciben comisión y trabajan para el departamento de ‘VENTAS’.

```
mysql> SELECT DISTINCT nomEmp, nombreDpto, salEmp, comisionE   FROM empleados JOIN departamentos WHERE (salEmp > '800.000' OR comisionE > 0) AND nomEmp REGEXP '^M' AND nombreDpto = 'VENTAS';
```

24. Obtener los nombres, salarios y comisiones de los empleados que reciben un salario situado entre la mitad de la comisión la propia comisión.

```
mysql> SELECT nomEmp, salEmp, comisionE FROM empleados WHERE salEmp >= (comisionE / 2);
```

25. Mostrar el salario más alto de la empresa.

```
mysql> SELECT * FROM empleados WHERE salEmp ORDER BY salEmp DESC LIMIT 1;
```

26. Mostrar cada una de las comisiones y el número de empleados que las reciben. Solo si tiene comisión.

```
mysql> SELECT comisionE, COUNT(*) FROM empleados GROUP BY comisionE HAVING comisionE > 0;
```

27. Mostrar el nombre del último empleado de la lista por orden alfabético.

```
mysql> SELECT * FROM empleados ORDER BY nomEmp DESC LIMIT 1;
```

28. Hallar el salario más alto, el más bajo y la diferencia entre ellos.

```
mysql> SELECT MAX(salEmp) AS 'MAX', MIN(salEmp) AS 'MIN', MAX(salEmp) - MIN(salEmp) AS 'RESTO' FROM empleados;
```

29. Mostrar el número de empleados de sexo femenino y de sexo masculino, por departamento.

```
mysql> SELECT codDepto, sexEmp, COUNT(*) FROM empleados GROUP BY codDepto, sexEmp;
```

30. Hallar el salario promedio por departamento.

```
mysql> SELECT codDepto, AVG(salEmp) FROM empleados GROUP BY codDepto;
```

31. Mostrar la lista de los empleados cuyo salario es mayor o igual que el promedio de la empresa. Ordenarlo por departamento.

```
mysql> SELECT nDIEmp, nomEmp, salEmp FROM empleados WHERE salEmp >= (SELEC
T AVG(salEmp) from empleados);
```

32. Hallar los departamentos que tienen más de tres empleados. Mostrar el número de empleados de esos departamentos.

```
mysql> SELECT departamentos.codDepto, empleados.codDepto, COUNT(*) as 'CANT' FROM departamentos, empleados WHERE departamentos.codDepto = empleados.codDepto GROUP BY departamentos.codDepto HAVING CANT >= 3;
```

33. Mostrar el código y nombre de cada jefe, junto al número de empleados que dirige. Solo los que tengan mas de dos empleados (2 incluido).

```
```

34. Hallar los departamentos que no tienen empleados

```
mysql> SELECT d.codDepto, d.nombreDpto, COUNT(*) AS 'D' FROM departamentos d, empleados e WHERE d.codDepto = e.codDepto GROUP BY d.codDepto HAVING D = 0;
```

35. Mostrar el nombre del departamento cuya suma de salarios sea la más alta, indicando el valor de la suma.

```
mysql> SELECT d.nombreDpto, sum(e.salEmp) FROM departamentos d, empleados
e WHERE d.codDepto = e.codDepto GROUP BY d.nombreDpto ORDER BY SUM(e.salEmp) DESC LIMIT 1;
```

