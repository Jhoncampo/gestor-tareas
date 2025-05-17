# Base de datos

## Creamos base de datos

```sql
CREATE DATABASE gestor_tareas; # Creamos la db

USE gestor_tareas; # Usamos la db

# Creamos la tabal usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    clave VARCHAR(10) NOT NULL,
    rol ENUM('admin', 'usuario') NOT NULL DEFAULT 'usuario'
);

# Creamos la tabal tareas y la referenciamos con la tabla usuarios
CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    descripcion TEXT,
    fecha_inicio TIMESTAMP DEFAULT NOW(),
    fecha_vencimiento DATETIME,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

