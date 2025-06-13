# utils/session.py

usuario_actual = None #se inicializa una variable " " con el valor de none que seia vacio

def establecer_usuario(usuario_dict): #Define una función que recibe como parámetro un diccionario con los datos del usuario
    global usuario_actual #Le dice a Python que quieres usar la variable que esta afuera de la funcion
    usuario_actual = usuario_dict #guarda los datos del usuario en la variable global para poder acceder a esta funcion desde cualquier prograda

def obtener_usuario():
    return usuario_actual #Devuelve el usuario que ha iniciado sesión actualmente.

def cerrar_sesion(): # Está diseñada para cerrar la sesión del usuario
    """Limpia la sesión actual""" #es un docstring, un comentario interno que explica qué hace la función.
    global _usuario_actual # indica que vas a modificar la variable global 
    _usuario_actual = None #borra la sesión asignando None