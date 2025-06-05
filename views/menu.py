from tkinter import NSEW, NS
from tkinter import ttk
from ttkbootstrap import Frame, Label

class menu_view:
    def __init__(self, master):
        self.master = master
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.ventana_menu()

    def ventana_menu(self):
        # Panel lateral donde van los botones
        self.frame_left = ttk.Frame(self.master, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)

        # Panel central donde va el contenido
        self.frame_center = ttk.Frame(self.master)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)

        # Botón Tareas
        btn_tareas = ttk.Button(self.frame_left, text='Tareas', width=20)
        btn_tareas.grid(row=0, column=0, padx=10, pady=10)

        # Botón Usuarios
        btn_usuarios = ttk.Button(self.frame_left, text='Usuarios', width=20, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=1, column=0, padx=10, pady=10)

    def ventana_lista_usuarios(self):
        print("Mostrando lista de usuarios... (Aún no implementado)")
