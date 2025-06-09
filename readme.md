# 📋 Gestor de Tareas en Python (Tkinter + MySQL)

Aplicación de escritorio desarrollada en **Python** con interfaz gráfica usando **Tkinter** y estilos modernos con **ttkbootstrap**, que permite la gestión de tareas para uno o varios usuarios, con control de roles, historial y alertas.
---


## 📁 Estructura del proyecto



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


## 🧩 Tecnologías utilizadas

- 🐍 Python 3.10+
- 🖼 Tkinter + ttkbootstrap
- 🐬 MySQL (conector `mysql-connector-python`)
- 📦 pyinstaller (para crear ejecutable)
- 📧 smtplib (notificaciones por correo - opcional)

---