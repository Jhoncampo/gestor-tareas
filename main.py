from views.login import login_view
import ttkbootstrap as tb

def main(): #flujo principal del programa.
    app = tb.Window(themename="superhero") #aplicamos un tema de color moderno
    app.title("Gestor de Tareas 2025") #titulo de la ventana
    app.state("zoomed") #se abre en pantalla maximizada automaticamente

    # 🔧 Hacer que la celda 0,0 del grid se expanda
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    login_view(app) #llama a ua funcion ya llamada y le pasa  la ventana como argumento

    app.mainloop() #Inicia el bucle principal de la interfaz gráfica (GUI) en una aplicación hecha con Tkinter o ttkbootstrap.


if __name__ == "__main__": #Indica el punto de entrada principal del programa en Python.
    main() #Llama a la función main() para ejecutar el bloque principal del programa.
