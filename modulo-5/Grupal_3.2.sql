-- Como parte de este ejercicio se necesita crear una base de datos MySQL, que dé respuesta
-- a las necesidades que serán planteadas en experiencias posteriores.
-- Cada usuario de la aplicación Te Lo Vendo requiere de un crédito denominado TLV Coins. 
-- Este crédito funciona exclusivamente en la aplicación, y permite comprar productos y 
-- transferir dinero a otros usuarios.


    

-- Información adicional:
	
-- Si algún usuario no tiene la cantidad suficiente de TLV Coins, la transacción debe deshacerse.
-- no hablan de qué debe hacer la tercera tabla, creo. Esta debería ser la tabla de transacciones, que guarde con un ID cada una, el usuario que entrega, el que recibe, el monto y el timestamp default now()

-- DESARROLLO

CREATE DATABASE 532g;

-- Debe crear un usuario para realizar este ejercicio.
CREATE USER 'user_532g'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON 532g TO 'user_532g'@'localhost';

USE 532g;

-- Debe crear una base de datos que contenga tres tablas:
-- Tabla usuario que referencie a sus datos transaccionales
CREATE TABLE usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT, #incremental entero representando id unico
  nombre VARCHAR(50), #string largo
  apellido VARCHAR(50)  #string largo
);

INSERT INTO usuarios VALUES
(1, 'Juan', 'González'),
(2, 'María', 'Rodríguez'),
(3, 'Perico', 'Los Palotes'),
(4, 'John', 'Doe');

-- Tabla cuentas: Tiene dos columnas, la primera ‘Cuenta’ contiene la cuenta del 
-- usuario y la segunda columna ‘Saldo’ indica el saldo de cada usuario. Cree cuatro 
-- usuarios registrados en esta tabla. 
CREATE TABLE cuentas (
   id_usuario int,
   saldo FLOAT,
   FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
   UNIQUE KEY (id_usuario)
);

CREATE TABLE transacciones (
  id_transaccion INT PRIMARY KEY AUTO_INCREMENT, #
  id_usuario_origen INT, 
  id_usuario_destino INT,
  monto FLOAT,
  fecha_hora_transaccion DATETIME DEFAULT CURRENT_TIMESTAMP, 
  FOREIGN KEY (id_usuario_origen) REFERENCES usuarios(id_usuario),
  FOREIGN KEY (id_usuario_destino) REFERENCES usuarios(id_usuario) 
);

-- Algunos aspectos a considerar:
-- Los Usuario no pueden tener un saldo negativo.
-- Cada usuario puede traspasar TLV Coins a otros usuarios.

DELIMITER //
-- Se crea un trigger que se activa ANTES de un intento de INSERT a la tabla transacciones, que revisa toda la
-- lógica y además actualiza los saldos en la tabla 'cuentas'

CREATE TRIGGER before_insert_transacciones -- nombre de trigger
BEFORE INSERT ON transacciones -- antes de insertar en transacciones
FOR EACH ROW -- para cada fila:
BEGIN
    DECLARE saldo_origen INT; -- declara las variables para poder ser usadas en la función
    DECLARE saldo_destino INT;

    -- Verificar si monto > cuentas.saldo donde id_usuario = id_usuario_origen
    SELECT saldo INTO saldo_origen
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_origen;
	-- Si el usuario origen no tiene suficiente saldo, tira error.
    IF NEW.monto > saldo_origen THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Monto mayor que el saldo de la cuenta origen.';
    END IF;

    -- Verificar si monto <= 0, para no intentar hacer movimientos con montos negativos
    IF NEW.monto <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Monto debe ser mayor que 0.';
    END IF;

    -- Verificar si id_usuario_origen existe en la tabla 'cuentas'. 
    
    SELECT COUNT(*) INTO @count_origen
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_origen;

    IF @count_origen = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El id_usuario_origen no existe en la tabla cuentas.';
    END IF;

    -- Verificar si id_usuario_destino existe en la tabla 'cuentas'. Si no existe, se crea.
    SELECT COUNT(*) INTO @count_destino
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_destino;

    IF @count_destino = 0 THEN
        -- Insertar usuario en tabla 'cuentas' con saldo = 0
        INSERT INTO cuentas (id_usuario, saldo) VALUES (NEW.id_usuario_destino, 0);
    END IF;

    -- Actualizar saldos en tabla 'cuentas' para id_usuario_origen y id_usuario_destino
    UPDATE cuentas
    SET saldo = saldo + NEW.monto
    WHERE id_usuario = NEW.id_usuario_destino;

    UPDATE cuentas
    SET saldo = saldo - NEW.monto
    WHERE id_usuario = NEW.id_usuario_origen;
END; -- marca final de la función
//

DELIMITER ;

-- ● Transfiera 200 TLV Coins desde un usuario A un usuario B.
-- ● Transfiera 150 TLV Coins desde un usuario B un usuario C.
-- ● Transfiera 500 TLV Coins desde un usuario C un usuario D.
-- ● Transfiera 200 TLV Coins desde un usuario D un usuario A.

-- En cada transacción, manualmente debe verificar que la cuenta tenga saldo suficiente.
-- Verificar que la cuenta de destino exista.
-- Actualizar la cuenta de origen.
-- Actualizar la cuenta de destino.
-- Verificar que se haya actualizado la cuenta de origen.
-- Verificar que se haya modificado la cuenta de destino.
-- Deshaga la transacción que realiza el usuario A al usuario usuario B.
-- Deshaga la transacción que realiza el usuario B al usuario usuario C.
-- Realice un commit de la transacción que realiza el usuario C al usuario usuario D.
-- Realice un commit de la transacción que realiza el usuario D al usuario usuario A.
-- Todo se tiene que ejecutar de forma transaccional.
-- 

-- darle saldo inicial de 500 a cuenta 1 y 3

INSERT INTO cuentas VALUES (
1, 500);

INSERT INTO cuentas VALUES (
3, 500);


-- Evitando que pasen a saldo negativo, además verificar que de cuenta origen y destino DEBEN existir

-- Para revisar saldos y transacciones previas:
SELECT * FROM cuentas;
SELECT * FROM transacciones;
 
-- ● Transfiera 200 TLV Coins desde un usuario A un usuario B.
START TRANSACTION;
INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
1,
2,
200
);

-- ● Transfiera 150 TLV Coins desde un usuario B un usuario C.

INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
2,
3,
150
);
-- PARA REVISAR ANTES DE ROLLBACK
SELECT * FROM cuentas;
SELECT * FROM transacciones;
ROLLBACK;
-- PARA REVISAR DESPUÉS DE ROLLBACK
SELECT * FROM cuentas;
SELECT * FROM transacciones;

-- ● Transfiera 500 TLV Coins desde un usuario C un usuario D.

START TRANSACTION;

INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
3,
4,
500
);
-- ● Transfiera 200 TLV Coins desde un usuario D un usuario A.

INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
3,
1,
200
);

COMMIT;
-- Verificar que las transacciones se realizaron en las cuentas origen y destino 

SELECT * FROM cuentas;
SELECT * FROM transacciones;

















