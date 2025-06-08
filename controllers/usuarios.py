from db.conexion import conectar_bd  # asegúrate de que el path sea correcto

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

    
    def obtener_usuarios():
        try:
            conexion = conectar_bd()
            if conexion is None:
                return []

            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, usuario, rol FROM usuarios")  # Omitimos la clave por seguridad
            datos = cursor.fetchall()
            conexion.close()
            return datos
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
