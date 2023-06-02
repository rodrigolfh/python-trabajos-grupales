-- Manipulación de datos - Consultas SQL.
-- D. Identifique cual es el salario mínimo entre vendedores.
select * from empleados where sueldo = (select min(sueldo) from empleados);
-- E. Identifique cual es el salario máximo entre vendedores.
select * from empleados where sueldo = (select max(sueldo) from empleados);
-- F. Súmele el salario mínimo identificado al salario de todos los vendedores.
UPDATE empleados
JOIN (SELECT MIN(sueldo) AS min_sueldo FROM empleados) AS subquery
SET sueldo = sueldo + subquery.min_sueldo
limit 99;
-- o en su lugar usar SET SQL_SAFE_UPDATES = 0 y luego SET SQL_SAFE_UPDATES = 1 en lugar de establecer un limit(?)
-- G. Elimine el producto más caro del inventario.
DELETE FROM productos ORDER BY precio DESC LIMIT 1;
-- H. Cree una tabla que contenga solo los clientes que han pagado más que el promedio.
CREATE TABLE usuarios_premium AS SELECT * FROM usuarios WHERE total_comprado > (SELECT AVG(total_comprado) FROM usuarios);
-- I. Actualice los datos de tres productos.
UPDATE productos
SET precio = precio + (precio*0.1)
limit 3;
-- J. Actualice los datos de tres vendedores.
UPDATE empleados
SET comision = comision + (comision*0.05)
limit 3;
-- K. Actualice los datos de 1 cliente.
UPDATE usuarios
SET saldo = saldo - (saldo*0.05)
limit 1;
-- L. Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
select nombre, apellido from empleados where sueldo > (select avg(sueldo) from empleados)  limit 1;
-- M. Indique cuál es el cliente con mayor gasto.
select * from usuarios where total_comprado = (select max(total_comprado) from usuarios) limit 1;