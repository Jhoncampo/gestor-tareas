# utils/session.py

usuario_actual = None

def establecer_usuario(usuario_dict):
    global usuario_actual
    usuario_actual = usuario_dict

def obtener_usuario():
    return usuario_actual

def cerrar_sesion():
    """Limpia la sesión actual"""
    global _usuario_actual
    _usuario_actual = None