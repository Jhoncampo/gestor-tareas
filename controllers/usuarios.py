from db.conexion import conectar_bd  # asegúrate de que el path sea correcto
from utils.session import obtener_usuario

class UsuariosController:
    def guardar_usuario(self, datos):
        conexion = conectar_bd()
        if not conexion:
            return False  # si no se conectó, salimos

        try:
            cursor = conexion.cursor()
            # Aquí no incluimos el ID porque es autoincremental
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
            cursor.execute("SELECT id, nombre, usuario, rol FROM usuarios")  # Omitimos la clave por seguridad
            datos = cursor.fetchall() #recupera todas las filas y nos devuelve en tuplas
            #nos guarda en la variable datos todas las filas
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
            return cursor.rowcount > 0 #"Devuelve True si una o más filas fueron afectadas por la consulta SQL, y False si no."
        except:
            return False #"Si ocurre cualquier error, devuelve False.
        finally:
            conexion.close()

