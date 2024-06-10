-- Tabla autor
DROP TABLE IF EXISTS autor CASCADE;
CREATE TABLE autor (
  id_autor SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

-- Tabla libro
DROP TABLE IF EXISTS libro CASCADE;
CREATE TABLE libro (
  ISBN INT PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  genero VARCHAR(45) NOT NULL,
  anio INT NOT NULL,
  editorial VARCHAR(45) NOT NULL,
  precio DECIMAL(10, 2) NOT NULL,
  cantidad INT NOT NULL,
  disponibilidad VARCHAR(45) NOT NULL
);

-- Tabla autor_libro
DROP TABLE IF EXISTS autor_libro CASCADE;
CREATE TABLE autor_libro (
  id_autor INT NOT NULL,
  ISBN INT NOT NULL,
  CONSTRAINT fk_autor
    FOREIGN KEY(id_autor) 
    REFERENCES autor(id_autor),
  CONSTRAINT fk_libro
    FOREIGN KEY(ISBN) 
    REFERENCES libro(ISBN)
);

-- Tabla usuario
DROP TABLE IF EXISTS usuario CASCADE;
CREATE TABLE usuario (
  nombre_usuario VARCHAR(50) PRIMARY KEY,
  contrasena VARCHAR(50) NOT NULL,
  rol VARCHAR(45) NOT NULL
);

-- Tabla direccion
DROP TABLE IF EXISTS direccion CASCADE;
CREATE TABLE direccion (
  id_direccion SERIAL PRIMARY KEY,
  direccion VARCHAR(60) NOT NULL,
  ciudad VARCHAR(60) NOT NULL,
  municipio VARCHAR(60) NOT NULL,
  CP VARCHAR(10) NOT NULL
);

-- Tabla tarjeta
DROP TABLE IF EXISTS tarjeta CASCADE;
CREATE TABLE tarjeta (
  num_tarjeta VARCHAR(16) PRIMARY KEY,
  id_cliente INT NOT NULL,
  CVV VARCHAR(4) NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  banco VARCHAR(45) NOT NULL
);

-- Tabla cliente
DROP TABLE IF EXISTS cliente CASCADE;
CREATE TABLE cliente (
  id_cliente SERIAL PRIMARY KEY,
  nombre_usuario VARCHAR(50) NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  apellido_paterno VARCHAR(50) NOT NULL,
  apellido_materno VARCHAR(50) NOT NULL,
  id_direccion INT NOT NULL,
  correo VARCHAR(50) NOT NULL,
  telefono VARCHAR(15) NOT NULL,
  num_tarjeta VARCHAR(16) NOT NULL
);

-- Tabla empleado
DROP TABLE IF EXISTS empleado CASCADE;
CREATE TABLE empleado (
  id_empleado SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  nombre_usuario VARCHAR(50) NOT NULL,
  apellido_paterno VARCHAR(50) NOT NULL,
  apellido_materno VARCHAR(50) NOT NULL,
  CONSTRAINT fk_usuario_empleado
    FOREIGN KEY(nombre_usuario) 
    REFERENCES usuario(nombre_usuario)
);

-- Tabla favoritos
DROP TABLE IF EXISTS favoritos CASCADE;
CREATE TABLE favoritos (
  id_cliente INT NOT NULL,
  ISBN INT NOT NULL,
  CONSTRAINT fk_cliente_favoritos
    FOREIGN KEY(id_cliente) 
    REFERENCES cliente(id_cliente),
  CONSTRAINT fk_libro_favoritos
    FOREIGN KEY(ISBN) 
    REFERENCES libro(ISBN)
);

-- Tabla proveedor
DROP TABLE IF EXISTS proveedor CASCADE;
CREATE TABLE proveedor (
  id_proveedor SERIAL PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  tel_contacto VARCHAR(15) NOT NULL
);

-- Tabla pedido
DROP TABLE IF EXISTS pedido CASCADE;
CREATE TABLE pedido (
  id_proveedor INT NOT NULL,
  ISBN INT NOT NULL,
  fecha_pedido DATE NOT NULL,
  fecha_entrega DATE NOT NULL,
  cantidad_pedida INT NOT NULL,
  precio_total DECIMAL(10, 2) NOT NULL,
  CONSTRAINT fk_proveedor_pedido
    FOREIGN KEY(id_proveedor) 
    REFERENCES proveedor(id_proveedor),
  CONSTRAINT fk_libro_pedido
    FOREIGN KEY(ISBN) 
    REFERENCES libro(ISBN)
);

-- Tabla tipo_venta
DROP TABLE IF EXISTS tipo_venta CASCADE;
CREATE TABLE tipo_venta (
  id_tipo SERIAL PRIMARY KEY,
  nombre VARCHAR(45)
);

-- Tabla venta
DROP TABLE IF EXISTS venta CASCADE;
CREATE TABLE venta (
  id_venta SERIAL PRIMARY KEY,
  tipo_venta INT NOT NULL,
  fecha DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  metodo_pago VARCHAR(45) NOT NULL,
  metodo_entrega VARCHAR(45),
  CONSTRAINT fk_tipo_venta
    FOREIGN KEY(tipo_venta) 
    REFERENCES tipo_venta(id_tipo)
);

-- Tabla venta_libro
DROP TABLE IF EXISTS venta_libro CASCADE;
CREATE TABLE venta_libro (
  id_venta INT NOT NULL,
  ISBN INT NOT NULL,
  cantidad INT NOT NULL,
  CONSTRAINT fk_venta_libro
    FOREIGN KEY(id_venta) 
    REFERENCES venta(id_venta),
  CONSTRAINT fk_libro_venta
    FOREIGN KEY(ISBN) 
    REFERENCES libro(ISBN)
);

-- Añadir restricciones de claves foráneas después de crear las tablas
ALTER TABLE direccion
  ADD COLUMN id_cliente INT,
  ADD CONSTRAINT fk_cliente_direccion FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);

ALTER TABLE tarjeta
  ADD CONSTRAINT fk_cliente_tarjeta FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);
