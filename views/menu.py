from tkinter import NSEW, NS
from tkinter import ttk
from ttkbootstrap import Frame, Label
from views.lista_usuarios import view_lista_usuarios
from views.lista_tareas import mostrar_lista_tareas

class menu_view:
    def __init__(self, master):
        self.master = master

        self.ventana_menu()

    def ventana_menu(self):
        # Panel izquierdo
        self.frame_left = Frame(self.master, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)

        # Panel central
        self.frame_center = Frame(self.master)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)

        # Panel derecho
        self.frame_right = Frame(self.master, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        # Botones del menú lateral
        btn_tareas = ttk.Button(self.frame_left, text='Tareas', width=20, command=self.ventana_lista_tareas)
        btn_tareas.grid(row=0, column=0, padx=10, pady=10)

        btn_usuarios = ttk.Button(self.frame_left, text='Usuarios', width=20, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=1, column=0, padx=10, pady=10)

    def ventana_lista_usuarios(self):
        # Limpia el frame central antes de insertar la nueva vista
        for widget in self.frame_center.winfo_children():
            widget.destroy()

        # Carga la vista de usuarios dentro del frame central
        view_lista_usuarios(self.frame_center)


    def ventana_lista_tareas(self):
        mostrar_lista_tareas(self)

