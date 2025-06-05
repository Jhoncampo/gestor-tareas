from tkinter import Toplevel, ttk, messagebox
from controllers.auth import registrar_usuario

class registro_view(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registrarse")
        self.geometry("400x450+600+200")
        self.resizable(False, False)
        self.grab_set()
        self.crear_formulario()

    def crear_formulario(self):
        frm = ttk.LabelFrame(self, text="Formulario de Registro")
        frm.pack(padx=20, pady=20, fill="both", expand=True)

        ttk.Label(frm, text="Registrarme", font=("Arial", 16)).pack(pady=10)

        ttk.Label(frm, text="Nombre completo:").pack(anchor='w', padx=10)
        self.entry_nombre = ttk.Entry(frm, width=40, justify='center')
        self.entry_nombre.pack(pady=5)

        ttk.Label(frm, text="Nombre de usuario:").pack(anchor='w', padx=10)
        self.entry_usuario = ttk.Entry(frm, width=40, justify='center')
        self.entry_usuario.pack(pady=5)

        ttk.Label(frm, text="Contraseña:").pack(anchor='w', padx=10)
        self.entry_clave = ttk.Entry(frm, width=40, justify='center', show='*')
        self.entry_clave.pack(pady=5)

        ttk.Button(frm, text="Registrar usuario", command=self.guardar_usuario).pack(pady=15)

    def guardar_usuario(self):
        nombre = self.entry_nombre.get().strip()
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_clave.get().strip()

        if not nombre or not usuario or not clave:
            messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios.")
            return

        exito, mensaje = registrar_usuario(nombre, usuario, clave)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.destroy()
        else:
            messagebox.showerror("Error", mensaje)
