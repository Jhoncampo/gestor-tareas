import mysql.connector #importa el modulo que nos permite conectarnos a MySQL y ejecutar consultas.
from mysql.connector import Error #Importa solo la clase Error, que se usa para capturar errores específicos del conector MySQL

def conectar_bd(): #define una funcion llamada conectar_bd la cual nos establece conecxion con la base de datos
    try: #Intenta ejecutar el bloque de código sin errores.
        conexion = mysql.connector.connect(   #Aquí se crea la conexión a MySQL con los datos:
            host='localhost',     #el servidor está en nuestro computador.   
            user='root',       #nombre de usuario de MySQL.
            password='Jhon3126114451', #clave del usuario de la base de datos
            database='gestor_tareas' #nombre de la base de datos a usar
        )
        if conexion.is_connected(): #Si la conexión con la base de datos está activa, entonces
            print("Conexión exitosa a la base de datos") #imprima el mensaje escrito
            return conexion #que la función está devolviendo el objeto de conexión a la base de datos,
    except Error as e: #se usa para capturar errores específicos relacionados con MySQL cuando se intenta conectar a la base de datos 
        print(f"Error al conectar a la base de datos: {e}") #es una impresión formateada en Python que muestra el mensaje de error cuando falla la conexión a la base de datos.
        return None
