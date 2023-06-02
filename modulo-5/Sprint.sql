-- Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 5 de Bases de Datos.
-- Diagrame el modelo entidad relación.
-- Construya una base de datos. Asigne un usuario con todos los privilegios. Construya las tablas.
CREATE DATABASE sprint5;
-- create database laquesoporte;
CREATE USER 'user_sprint5'@'localhost' IDENTIFIED BY 'contraseña';
USE sprint5;

-- Cada usuario tiene información sobre: nombre, apellido, edad, correo electrónico y número de veces que ha utilizado la aplicación
CREATE TABLE usuarios (
id_usuario INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(30),
apellido VARCHAR(50),
edad INT,
correo_electronico VARCHAR(50),
conteo_usos INT DEFAULT 1 
);

-- Cada operario tiene información sobre: nombre, apellido, edad, correo electrónico y número de veces
-- que ha servido de soporte (por defecto es 1, pero al insertar los registros debe indicar un número -- manual).

CREATE TABLE operarios (
id_operario INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(30),
apellido VARCHAR(50),
edad INT,
correo_electronico VARCHAR(50),
conteo_soportes INT DEFAULT 1 -- no creo lógico setearlo en 1
);

CREATE TABLE tickets (
id_ticket INT PRIMARY KEY AUTO_INCREMENT,
id_operario INT,
id_usuario INT,
fecha TIMESTAMP DEFAULT NOW(),
evaluación BOOL DEFAULT '0', -- no todos responden
-- evaluación TINYINT DEFAULT NULL, -- default NULL en caso de que nadie responda
FOREIGN KEY (id_operario) REFERENCES operarios(id_operario) ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE encuesta (
id_encuesta INT PRIMARY KEY AUTO_INCREMENT,
id_operario INT, -- no es necesario pero creo que mejora legibilidad... se mantiene??
id_usuario INT, -- no es necesario pero creo que mejora legibilidad... se mantiene??
id_ticket INT,
evaluación TINYINT,
comentario 	VARCHAR(255),
FOREIGN KEY (id_operario) REFERENCES operarios(id_operario) ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (id_ticket) REFERENCES tickets(id_ticket) ON UPDATE CASCADE ON DELETE RESTRICT
);

/*Tu aplicación necesita una base de datos para sistematizar el funcionamiento del soporte ‘En qué puedo ayudarte’. El soporte lo realizan operarios.
Cada vez que un usuario utiliza el soporte ‘¿En qué puedo ayudarte?’ se le asigna un operario para mayudarlo con su problema.
Luego de esto, el usuario responde una encuesta donde califica al operario con una nota de 1 a 7, junto a un pequeño comentario sobre su atención.*/

-- Agregue 5 usuarios, 5 operadores y 10 operaciones de soporte. Los datos debe crearlos según su imaginación.

-- operarios:
INSERT INTO operarios (nombre, apellido, edad, correo_electronico, conteo_soportes)
VALUES 
    ('Juan', 'Perez', 28, 'juan.perez@example.com', 0),
    ('Maria', 'Rodriguez', 35, 'maria.rodriguez@example.com', 0),
    ('Carlos', 'Sanchez', 42, 'carlos.sanchez@example.com', 0),
    ('Laura', 'Gomez', 31, 'laura.gomez@example.com', 0),
    ('Roberto', 'Fernandez', 25, 'roberto.fernandez@example.com', 50000); -- Roberto es practicante
    
-- usuarios:
INSERT INTO usuarios (nombre, apellido, edad, correo_electronico, conteo_usos)
VALUES 
    ('Ana', 'Lopez', 32, 'ana.lopez@example.com', 0),
    ('Pedro', 'Garcia', 45, 'pedro.garcia@example.com', 0),
    ('María', 'Torres', 27, 'maria.torres@example.com', 0),
    ('Javier', 'Martinez', 39, 'javier.martinez@example.com', 0),
    ('Karen', 'McTicket', 55, 'sofia.ramirez@example.com', 50000);

-- Cada vez que se realiza un soporte, se reconoce quien es el operario, el cliente, la fecha y la evaluación que recibe el soporte.
-- se entiende por una instancia de soporte realizado como un insert a la tabla tickets. cumpliendo con lo solicitado, el valor default de tickets/soportes es 1, pero con un ingreso de valor inicial manual.

Delimiter //
CREATE TRIGGER before_insert_tickets
BEFORE INSERT ON tickets
FOR EACH ROW
BEGIN
    DECLARE operario INT;
    DECLARE usuario INT;
    DECLARE ticket INT;
    
    SET operario = NEW.id_operario;
    SET usuario = NEW.id_usuario;
    SET ticket = NEW.id_ticket;
    
    IF NOT EXISTS (SELECT 1 FROM operarios WHERE id_operario = operario) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No existe el operario indicado';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM usuarios WHERE id_usuario = usuario) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No existe el usuario indicado';
    END IF;
    
   
    
END //
Delimiter ; -- recordatorio, para crear el trigger debo ejecutar desde la comilla de esta línea.

-- creamos una transaccion que permita simular eventos de soporte con valores semirandom.
-- el rango es de 1 a 6 para dar espacio a que fallen algunas consultas (tenemos 5 usuarios y operadores)
-- se asume que esta transacción es para los casos en que el usuario sí realizará una evaluación, ocupando una transacción distinta para el caso en que no.

-- caso con evaluacion
start transaction;
	-- setup variables representando un evento de soporte
    SET @operario = FLOOR(1 + RAND() * 5); 
    SET @usuario = FLOOR(1 + RAND() * 5); -- arbitrarios
	SET @conteo_soportes = (select conteo_soportes from operarios where id_operario = @operario); -- recupero los respectivos contadores
	SET @conteo_usos = (select conteo_usos from usuarios where id_usuario = @usuario);
    SET @evaluacion = FLOOR(1 + RAND() * 7);

	insert into tickets(id_operario, id_usuario, evaluación)
	values(@operario, @usuario, @evaluacion);
    
    SET @ticket = (select id_ticket from tickets where id_usuario = @usuario and id_operario = @operario order by id_ticket limit 1);
    -- no estoy seguro si es asc o desc (asc por defecto)
    insert into encuesta(id_operario, id_usuario, id_ticket, evaluación, comentario)
    values (@operario, @usuario, @ticket, @evaluacion, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.');

	update operarios set conteo_soportes = conteo_soportes + 1 where id_operario = @operario;
	update usuarios set conteo_usos = conteo_usos + 1 where id_usuario = @usuario;
commit;

-- caso sin evaluacion
start transaction;
	-- setup variables representando un evento de soporte
    SET @operario = FLOOR(1 + RAND() * 5); 
    SET @usuario = FLOOR(1 + RAND() * 5); -- arbitrarios
	SET @conteo_soportes = (select conteo_soportes from operarios where id_operario = @operario); -- recupero los respectivos contadores
	SET @conteo_usos = (select conteo_usos from usuarios where id_usuario = @usuario);

	update operarios set conteo_soportes = conteo_soportes + 1 where id_operario = @operario;
	update usuarios set conteo_usos = conteo_usos + 1 where id_usuario = @usuario;
commit;

-- Seleccione las 3 operaciones con mejor evaluación.

select * from tickets order by evaluación desc limit 3;

-- Seleccione las 3 operaciones con menos evaluación.

select * from tickets order by evaluación  limit 3;

-- Seleccione al operario que más soportes ha realizado.

select * from operarios order by conteo_soportes desc limit 1;

-- Seleccione al cliente que menos veces ha utilizado la aplicación.

select * from usuarios order by conteo_usos limit 1;

-- Agregue 10 años a los tres primeros usuarios registrados.

update usuarios set edad = edad + 10 order by id_usuario limit 3;

-- Renombre todas las columnas ‘correo electrónico’. El nuevo nombre debe ser email.

alter table usuarios rename column `correo_electronico` to email;
alter table operarios rename column `correo_electronico` to email;

-- Seleccione solo los operarios mayores de 20 años.

select * from operarios where edad > 20 order by edad ;