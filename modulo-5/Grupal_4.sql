-- Parte 1: Crear entorno de trabajo
-- - Crear una base de datos
create database 54grupal;
use 54grupal;

-- - Crear un usuario con todos los privilegios para trabajar con la base de datos recién creada.
CREATE USER 'user54grupal'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON 54grupal TO 'user54grupal'@'localhost';

-- Parte 2: Crear dos tablas.
-- - La primera almacena a los usuarios de la aplicación (id_usuario, nombre, apellido, contraseña,
-- zona horaria (por defecto UTC-3), género y teléfono de contacto).

CREATE TABLE usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50), #varchar por dar espacio a las particularidades que puede tener un nombre
  apellido VARCHAR(50), #varchar por dar espacio a las particularidades que puede tener un apellido
  contraseña VARCHAR(20), #varchar por dar espacio a las particularidades que puede tener un pass
  zona_horaria VARCHAR(10) DEFAULT 'UTC-3', #varchar para almacenar strings con simbolos como guion
  género CHAR(1), #deberia ser suficiente para indicar Masculino, femenino u otro
  teléfono VARCHAR(20) #string para almacenar un numero telefónico con simbolos
);

-- - La segunda tabla almacena información relacionada a la fecha-hora de ingreso de los usuarios
-- a la plataforma (id_ingreso, id_usuario y la fecha-hora de ingreso (por defecto la fecha-hora actual)).
CREATE TABLE ingresos (
  id_ingreso INT PRIMARY KEY AUTO_INCREMENT, #almacenará solo numeros enteros ascendentes
  id_usuario INT, #igualmente, solo numeros enteros
  fecha_hora_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP, -- almacena la fecha y hra de ingreso, además de asignarle un now() como value por defecto
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
-- Parte 3: Modificación de la tabla
-- - Modifique el UTC por defecto.Desde UTC-3 a UTC-2.
ALTER TABLE usuarios
CHANGE COLUMN zona_horaria
zona_horaria VARCHAR(10) NULL DEFAULT 'UTC-2' ;

-- Parte 4: Creación de registros.
-- - Para cada tabla crea 8 registros.
INSERT INTO usuarios (nombre, apellido, contraseña, zona_horaria, género, teléfono)
VALUES
  ('Juan', 'González', 'password1', 'UTC-2', '1', '912345678'),
  ('Pedro', 'Soto', 'password2', 'UTC-2', '1', '912345679'),
  ('María', 'López', 'password3', 'UTC-2', '2', '912345680'),
  ('Alejandra', 'Martínez', 'password4', 'UTC-2', '2', '912345681'),
  ('Diego', 'Silva', 'password5', 'UTC-2', '1', '912345682'),
  ('Fernanda', 'Torres', 'password6', 'UTC-2', '2', '912345683'),
  ('Andrés', 'Ramírez', 'password7', 'UTC-2', '1', '912345684'),
  ('Carolina', 'García', 'password8', 'UTC-2', '2', '912345685');

INSERT INTO ingresos (id_usuario)
VALUES
  (1),
  (2),
  (3),
  (4),
  (5),
  (6),
  (7),
  (8);

-- Parte 5: Justifique cada tipo de dato utilizado. ¿Es el óptimo en cada caso?
-- Se justificó como comentario al final de cada línea en los queries correspondientes.

-- Parte 6: Creen una nueva tabla llamada Contactos (id_contacto, id_usuario, numero de telefono,
-- correo electronico).

CREATE TABLE contactos (
  id_contacto INT PRIMARY KEY AUTO_INCREMENT, #almacenará solo numeros enteros ascendentes
  id_usuario INT, #igualmente, solo numeros enteros, una llave foránea
  fono INT, -- número de teléfono, un entero
  mail VARCHAR(55),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Parte 7: Modifique la columna teléfono de contacto, para crear un vínculo entre la tabla Usuarios y la
-- tabla Contactos.

ALTER TABLE contactos
ADD INDEX idx_fono (fono); -- para poder hacer el paso siguiente, Mysql exige un indexado.

ALTER TABLE usuarios
ADD COLUMN fono INT,
ADD FOREIGN KEY (fono) REFERENCES contactos(fono) ON UPDATE CASCADE;
