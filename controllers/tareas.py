from db.conexion import conectar_bd #imprtamos la funcion conectar_bd de la base de datos

class TareasController: #Controla las acciones sobre tareas 
    def obtener_tareas_por_usuario(self, usuario_id): #que sirve para obtener todas las tareas asociadas a un usuario específico, identificado por su usuario_id
        conexion = conectar_bd()
        if not conexion: #Verifica si la conexión a la base de datos falló.
            return [] # Devuelve una lista vacía desde una función.
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, titulo, descripcion, fecha_inicio, fecha_vencimiento FROM tareas WHERE usuario_id = %s order by fecha_vencimiento asc", (usuario_id,))
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
