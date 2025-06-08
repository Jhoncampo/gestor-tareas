from db.conexion import conectar_bd

def login(usuario, clave):
    conexion = conectar_bd()
    if not conexion:
        return None
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, usuario FROM usuarios WHERE usuario = %s AND clave = %s", (usuario, clave))
        fila = cursor.fetchone()
        if fila:
            return {
                'id': fila[0],
                'nombre': fila[1],
                'usuario': fila[2]
            }
        return None
    finally:
        conexion.close()


def registrar_usuario(nombre, usuario, clave):
    conexion = conectar_bd()
    if not conexion:
        return False, "Error de conexión"
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, usuario, clave) VALUES (%s, %s, %s)", (nombre, usuario, clave))
        conexion.commit()
        return True, "Usuario registrado correctamente"
    except Exception as e:
        return False, str(e)
    finally:
        conexion.close()
