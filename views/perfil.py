
from tkinter import Frame, LabelFrame, Label, NSEW, NS, messagebox, Toplevel, W, Entry
from tkinter import ttk
import ttkbootstrap as tb  # type: ignore
from utils.frame_center import centrar_ventana
from controllers.usuarios import UsuariosController


class view_perfil_usuario(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky=NSEW)  
        self.controller = UsuariosController()

        self.usuario_actual = self.controller.obtener_usuario_actual() 
        if not self.usuario_actual:
            messagebox.showerror("Error", "No se pudo cargar el perfil del usuario.")
            return

        self.mostrar_formulario_perfil()
        self.mostrar_formulario_perfil()

    def mostrar_formulario_perfil(self):
        lblframe_perfil = LabelFrame(self, text="Mi perfil")
        lblframe_perfil.grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)

        Label(lblframe_perfil, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        self.txt_nombre = ttk.Entry(lblframe_perfil, width=40)
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.txt_nombre.insert(0, self.usuario_actual['nombre'])

        Label(lblframe_perfil, text="Usuario").grid(row=1, column=0, padx=10, pady=10)
        self.txt_usuario = ttk.Entry(lblframe_perfil, width=40)
        self.txt_usuario.grid(row=1, column=1, padx=10, pady=10)
        self.txt_usuario.insert(0, self.usuario_actual['usuario'])
        self.txt_usuario.config(state='disabled')

        Label(lblframe_perfil, text="Nueva clave").grid(row=2, column=0, padx=10, pady=10)
        self.txt_clave = ttk.Entry(lblframe_perfil, width=40, show="*")
        self.txt_clave.grid(row=2, column=1, padx=10, pady=10)

        btn_guardar = ttk.Button(lblframe_perfil, text="Guardar cambios", style='success.TButton', command=self.guardar_cambios)
        btn_guardar.grid(row=3, column=1, pady=15)

    def guardar_cambios(self):
        nombre = self.txt_nombre.get().strip()
        clave = self.txt_clave.get().strip()

        if not nombre or not clave:
            messagebox.showwarning("Validación", "Todos los campos deben estar completos.")
            return

        datos = (nombre, clave, self.usuario_actual['id'])
        actualizado = self.controller.actualizar_perfil_usuario(datos)

        if actualizado:
            messagebox.showinfo("Éxito", "Perfil actualizado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el perfil.")