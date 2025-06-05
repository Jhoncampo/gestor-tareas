# 📋 Gestor de Tareas en Python (Tkinter + MySQL)

Aplicación de escritorio desarrollada en **Python** con interfaz gráfica usando **Tkinter** y estilos modernos con **ttkbootstrap**, que permite la gestión de tareas para uno o varios usuarios, con control de roles, historial y alertas.

---

## 🚀 Funcionalidades clave

### 🗂 Gestión de tareas
- ✅ Crear, editar, eliminar tareas
- ✅ Filtrar por estado: Pendiente, En progreso, Completado
- ✅ Establecer prioridad: Alta, Media, Baja
- ✅ Asignación de responsables
- ✅ Notas y archivos adjuntos
- ✅ Comentarios e historial de cambios
- ✅ Búsqueda por palabra clave o fecha

### ⏰ Automatización
- ✅ Alertas para tareas próximas a vencer
- ✅ Tareas recurrentes (diarias, semanales, mensuales)
- ✅ Progreso por tarea y usuario

### 🔐 Gestión de usuarios y seguridad
- ✅ Crear, editar, eliminar usuarios
- ✅ Roles: Administrador / Usuario común
- ✅ Validación de contraseñas
- ✅ Recuperación por pregunta secreta
- ✅ Historial de acceso y acciones

### 📊 Interfaz visual y usabilidad
- ✅ Modo claro / oscuro (ttkbootstrap)
- ✅ Dashboard con:
  - Número de tareas por estado
  - Gráfico circular por prioridad
  - Línea temporal de tareas completadas
- ✅ Animaciones al cambiar de vista
- ✅ Cabecera con usuario actual, fecha/hora
- ✅ Panel lateral de tareas urgentes
- ✅ Barra de progreso por proyecto

### 💾 Base de datos y extras
- ✅ Separación de tareas por proyectos
- ✅ Historial de cambios por tarea
- ✅ Exportar a CSV / PDF
- ✅ Backup y restauración automática
- ✅ Soporte multi-idioma (experimental)

---

## 🧩 Tecnologías utilizadas

- 🐍 Python 3.10+
- 🖼 Tkinter + ttkbootstrap
- 🐬 MySQL (conector `mysql-connector-python`)
- 📦 pyinstaller (para crear ejecutable)
- 📧 smtplib (notificaciones por correo - opcional)

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

