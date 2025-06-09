def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    coordenadas_x = int((pantalla_ancho / 2) - (ancho / 2))
    coordenadas_y = int((pantalla_alto / 2) - (alto / 2))
    ventana.geometry(f"{ancho}x{alto}+{coordenadas_x}+{coordenadas_y}")
