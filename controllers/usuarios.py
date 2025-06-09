from db.conexion import conectar_bd 
from utils.session import obtener_usuario

class UsuariosController:
    def guardar_usuario(self, datos):
        conexion = conectar_bd()
        if not conexion:
            return False 

        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios (nombre, usuario, clave, rol) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, datos)
            conexion.commit()
            return True
        except Exception as e:
            print("Error al guardar usuario:", e)
            return False
        finally:
            conexion.close()

    
    def obtener_usuarios(self):
        try:
            conexion = conectar_bd()
            if conexion is None:
                return []

            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, usuario, rol FROM usuarios")  
            datos = cursor.fetchall()
            conexion.close()
            return datos
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
    def obtener_usuario_actual(self):
          return obtener_usuario()

    def actualizar_perfil_usuario(self, datos):
        conexion = conectar_bd()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE usuarios SET nombre = %s, clave = %s WHERE id = %s",
                datos
            )
            conexion.commit()
            return cursor.rowcount > 0
        except:
            return False
        finally:
            conexion.close()

