-- G. Seleccione los vendedores que tienen un salario superior al promedio.
SELECT * FROM empleados WHERE sueldo > (SELECT AVG(sueldo) AS Promedio_Sueldo FROM empleados);

-- H. Seleccione los productos más caros que el promedio.
SELECT * FROM productos WHERE precio > (SELECT AVG(precio) AS Promedio_Precio FROM productos);

-- I. Seleccione los clientes que han pagado más que el promedio.
SELECT * FROM usuarios WHERE total_comprado > (SELECT AVG(total_comprado) FROM usuarios);

-- J. Indique cuántos vendedores tienen un salario inferior al promedio.
SELECT * FROM empleados WHERE sueldo < (SELECT AVG(sueldo) FROM empleados);

-- K. Indique cuántos productos son más baratos que el promedio.
SELECT * FROM productos WHERE precio < (SELECT AVG(precio) FROM productos);

-- L. Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio.
SELECT nombre, apellido FROM empleados WHERE sueldo > (SELECT AVG(sueldo) FROM empleados);

-- M. Indique cuál es el producto más barato y el producto más caro del inventario.
SELECT MAX(precio) AS producto_mas_caro, MIN(precio) AS producto_mas_barato FROM productos;

-- N. Indique cual es el costo de comprar uno de cada producto en el inventario.
SELECT SUM(precio) FROM productos;

-- O. Identifique la comuna que tiene más clientes registrados.
-- (como no teníamos la columna 'comuna', se agrega)
ALTER TABLE usuarios
ADD comuna VARCHAR(30);
UPDATE usuarios
SET comuna = CASE
    WHEN nombre = 'Valentina' THEN 'Santiago'
    WHEN nombre = 'Ricardo' THEN 'Valparaíso'
    WHEN nombre = 'Pedro' THEN 'Concepción'
    WHEN nombre = 'Juan' THEN 'Viña del Mar'
    WHEN nombre = 'Diego' THEN 'Santiago'
    WHEN nombre = 'Luis' THEN 'Antofagasta'
    WHEN nombre = 'Camila' THEN 'Valdivia'
    WHEN nombre = 'Andrea' THEN 'La Serena'
    WHEN nombre = 'Ignacio' THEN 'Arica'
    WHEN nombre = 'Isabella' THEN 'Rancagua'
    END;

SELECT comuna, COUNT(comuna) AS conteo_comuna 
FROM usuarios
GROUP BY comuna 
ORDER BY conteo_comuna DESC
LIMIT 1;

-- P. Identifique los productos que tienen más de 5 unidades en stock.
-- (no teníamos stock ahora se agrega)

ALTER TABLE productos
ADD stock INT;

UPDATE productos
SET stock = CASE
    WHEN sku = '001' THEN 300
    WHEN sku = '002' THEN 250
    WHEN sku = '003' THEN 200
    WHEN sku = '004' THEN 150
    WHEN sku = '005' THEN 100
    WHEN sku = '006' THEN 50
    WHEN sku = '007' THEN 25
    WHEN sku = '008' THEN 10
    WHEN sku = '009' THEN 5
    WHEN sku = '000' THEN 0
END;

SELECT * FROM productos WHERE stock > 5;

