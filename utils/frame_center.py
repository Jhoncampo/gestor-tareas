# utils/frame_center.py

def centrar_ventana(ventana, ancho, alto): #Sirve para centrar una ventana de Tkinter en la pantalla.
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()  #Calcula el tamaño total de la pantalla del usuario (en píxeles).
    coordenadas_x = int((pantalla_ancho / 2) - (ancho / 2))
    coordenadas_y = int((pantalla_alto / 2) - (alto / 2)) #Se calcula el punto (x, y) donde la ventana debe empezar para quedar centrada.
    ventana.geometry(f"{ancho}x{alto}+{coordenadas_x}+{coordenadas_y}") #Establecer el tamaño de la ventana (ancho x alto) y posicionarla en la pantalla
