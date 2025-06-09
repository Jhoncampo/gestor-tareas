from db.conexion import conectar_bd

class TareasController:
    def obtener_tareas_por_usuario(self, usuario_id):
        conexion = conectar_bd()
        if not conexion:
            return []
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, titulo, descripcion, fecha_inicio, fecha_vencimiento FROM tareas WHERE usuario_id = %s", (usuario_id,))
            return cursor.fetchall()
        finally:
            conexion.close()

    def guardar_tarea(self, datos):
        conexion = conectar_bd()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO tareas (titulo, descripcion, fecha_vencimiento, usuario_id) VALUES (%s, %s, %s, %s)",
                datos
            )
            conexion.commit()
            return True
        except:
            return False
        finally:
            conexion.close()

    def eliminar_tarea(self, tarea_id):
        conexion = conectar_bd()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM tareas WHERE id = %s", (tarea_id,))
            conexion.commit()
            return True
        finally:
            conexion.close()

    def actualizar_tarea(self, datos):
        conexion = conectar_bd()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE tareas SET titulo = %s, descripcion = %s, fecha_vencimiento = %s WHERE id = %s",
                datos
            )
            conexion.commit()
            return True
        finally:
            conexion.close()
