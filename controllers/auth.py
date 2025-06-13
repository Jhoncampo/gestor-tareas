from db.conexion import conectar_bd #importando la función conectar_bd

def login(usuario, clave): #def es para declarar o llamar la funcion login
    conexion = conectar_bd() #crea una conexion con la base de datos
    if not conexion:  #se usa para ejecutar una condicion del código solo si es falta o no existe.
        return None  # termina y devuelve el valor especial none: ningun valor o ausencia de valor
    try: #Intenta ejecutar el  de código sin errores.
        cursor = conexion.cursor() #Crea un cursor, que es el objeto que permite ejecutar consultas SQL sobre la conexión.
        # %s es un marcador de valor seguro, que evita inyecciones SQL..
        cursor.execute("SELECT id, nombre, usuario FROM usuarios WHERE usuario = %s AND clave = %s", (usuario, clave)) #Ejecuta una consulta SQL que busca un usuario con el nombre de usuario y contraseña proporcionados
        fila = cursor.fetchone() #Recupera el primer resultado encontrado (si existe).

        if fila: #Si se encontró una fila (es decir, el usuario existe y la contraseña es correcta):Devuelve un diccionario con el id, nombre y usuario.
            return {
                'id': fila[0],
                'nombre': fila[1],
                'usuario': fila[2]
            }
        return None
    finally:
        conexion.close() #Se ejecuta siempre, haya o no errores. Cierra la conexión a la base de datos para liberar recursos.


def registrar_usuario(nombre, usuario, clave):
    conexion = conectar_bd() #creando una conexión a la base de datos
    if not conexion: #Si no hay conexión" o "si la variable conexion es None, False o está vacía", entonces ejecuta el bloque siguiente.

        return False, "Error de conexión"
    try: 
        cursor = conexion.cursor() #Crea un cursor, que es el objeto que permite ejecutar consultas SQL sobre la conexión.
        cursor.execute("INSERT INTO usuarios (nombre, usuario, clave) VALUES (%s, %s, %s)", (nombre, usuario, clave))
        conexion.commit() #se usa para guardar de forma permanente los cambios hechos en la base de datos durante una transacción.
        return True, "Usuario registrado correctamente" #si es verdadero muestra el mensaje y se devuelve
    except Exception as e: #Si ocurre cualquier error (excepción), captúralo y guárdalo en la variable e
        return False, str(e) #False: indica que ocurrió un error o que la operación falló y str devuelve el mensaje de error como texto, para saber qué salió mal.

    finally:
        conexion.close() #Pase lo que pase —con o sin error—, siempre cerrar la conexión a la base de datos."
