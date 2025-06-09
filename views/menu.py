from tkinter import NSEW, NS
from tkinter import ttk
from ttkbootstrap import Frame, Label
from views.lista_usuarios import view_lista_usuarios
from views.lista_tareas import view_lista_tareas
from views.perfil import view_perfil_usuario
from utils.session import cerrar_sesion


class menu_view(Frame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.master = master
        self.usuario = usuario
        


        self.ventana_menu()

    def ventana_menu(self):
        self.frame_left = Frame(self.master, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)

        self.frame_center = Frame(self.master)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)

        self.frame_right = Frame(self.master, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        btn_tareas = ttk.Button(self.frame_left, text='Tareas', width=20, command=self.ventana_lista_tareas)
        btn_tareas.grid(row=0, column=0, padx=10, pady=10)

        # btn_usuarios = ttk.Button(self.frame_left, text='Usuarios', width=20, command=self.ventana_lista_usuarios)
        # btn_usuarios.grid(row=1, column=0, padx=10, pady=10)
        
        btn_perfil = ttk.Button(self.frame_left, text='Perfil', width=20, command=self.ventana_perfil_usuario)
        btn_perfil.grid(row=2, column=0, padx=10, pady=10)
        btn_salir = ttk.Button(self.frame_left, text='Cerrar sesión', width=20, command=self.cerrar_sesion)
        btn_salir.grid(row=3, column=0, padx=10, pady=10)


    def ventana_perfil_usuario(self):
        for widget in self.frame_center.winfo_children():
            widget.destroy()
        view_perfil_usuario(self.frame_center) 


    def ventana_lista_usuarios(self):
        for widget in self.frame_center.winfo_children():
            widget.destroy()

        view_lista_usuarios(self.frame_center)
    def cerrar_sesion(self):
        from views.login import login_view 

        from utils.session import cerrar_sesion
        cerrar_sesion()

        for widget in self.master.winfo_children():
            widget.destroy()

        login_view(self.master)



    def ventana_lista_tareas(self):
        from utils.session import obtener_usuario
        usuario = obtener_usuario()

        for widget in self.frame_center.winfo_children():
            widget.destroy()

        view_lista_tareas(self.frame_center, usuario['id'])


