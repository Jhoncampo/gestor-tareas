from tkinter import ttk, messagebox
from ttkbootstrap import Window
from views.registro import registro_view
from views.menu import menu_view
import ttkbootstrap as tb
from controllers.auth import login
from utils.session import establecer_usuario
from utils.session import obtener_usuario

class login_view(tb.Frame):  
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.ventana_login()

    def ventana_login(self):
        self.frame_login = ttk.Frame(self, padding=30)
        self.frame_login.pack(expand=True)

        lbl_titulo = ttk.Label(self.frame_login, text='Inicio de Sesión', font=('Segoe UI', 20, 'bold'))
        lbl_titulo.pack(pady=(0, 25))

        self.txt_usuario = ttk.Entry(self.frame_login, width=30, justify='center')
        self.txt_usuario.pack(pady=10)

        self.txt_clave = ttk.Entry(self.frame_login, width=30, justify='center', show='*')
        self.txt_clave.pack(pady=10)

        btn_ingresar = ttk.Button(self.frame_login, text='Ingresar', width=30, bootstyle="success", command=self.ingresar)
        btn_ingresar.pack(pady=(20, 10))

        btn_registrar = ttk.Button(
            self.frame_login, 
            text='¿No tienes cuenta? Regístrate', 
            width=30, 
            bootstyle="link", 
            command=self.ventana_registro
        )
        btn_registrar.pack()

    def ingresar(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()
        resultado = login(usuario, clave)

        if resultado:
            establecer_usuario(resultado)  
            self.frame_login.pack_forget()
            self.ventana_menu(resultado)
        else:
            messagebox.showerror("Acceso", "Usuario o clave incorrectos")

    def ventana_menu(self, usuario):
        menu_view(self, usuario) 

    def ventana_registro(self):
        registro_view(self)
