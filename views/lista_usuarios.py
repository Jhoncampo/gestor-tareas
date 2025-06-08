
from tkinter import Frame, LabelFrame, Label, NSEW, NS, messagebox, Toplevel, W, Entry
from tkinter import ttk
import ttkbootstrap as tb  # type: ignore
from utils.frame_center import centrar_ventana
from controllers.usuarios import UsuariosController


class view_lista_usuarios(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky=NSEW)  # o .pack()
        self.mostrar_lista_usuarios()
        self.controller = UsuariosController()

    

    def mostrar_lista_usuarios(self):
        self.frame_lista_usuarios=ttk.Frame(self)
        self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2, sticky=NSEW)

        self.lblframe_botones_listausuarios=ttk.Labelframe(self.frame_lista_usuarios)
        self.lblframe_botones_listausuarios.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_usuario = tb.Button(
            self.lblframe_botones_listausuarios,
            text='Nuevo usuario',
            width=18,
            style='success',
            command=self.ventana_nuevo_usuario  # ⬅️ ahora llama bien al método
        )

        btn_nuevo_usuario.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_usuario=tb.Button(self.lblframe_botones_listausuarios, text='Modificar usuario', width=18, style='warning')
        btn_modificar_usuario.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_usuario=tb.Button(self.lblframe_botones_listausuarios, text='Eliminar usuario', width=18, style='danger')
        btn_eliminar_usuario.grid(row=0,column=2,padx=5,pady=5)

        self.lblframe_tree_listatareas=ttk.LabelFrame(self.frame_lista_usuarios)
        self.lblframe_tree_listatareas.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        columnas=("id","nombre", "usuario", "clave", "rol")
        self.tree_lista_tareas=tb.Treeview(self.lblframe_tree_listatareas, columns=columnas, height=17, show='headings', style='dark')
        self.tree_lista_tareas.grid(row=0,column=0)

        self.tree_lista_tareas.heading("id", text="ID", anchor=W)
        self.tree_lista_tareas.heading("nombre", text="Nombre", anchor=W)
        self.tree_lista_tareas.heading("usuario", text="Usuario", anchor=W)
        self.tree_lista_tareas.heading("clave", text="Clave", anchor=W)
        self.tree_lista_tareas.heading("rol", text="Rol", anchor=W)

        self.mostrar_usuarios()

    def ventana_nuevo_usuario(self):

        self.frame_nuevo_usuario=Toplevel(self.master) # window above the user list
        self.frame_nuevo_usuario.title("Nuevo usuario") #Title of the window
        self.center(380,400) # size of the window
        self.frame_nuevo_usuario.resizable(0,0) # we do not want to resize the window
        self.frame_nuevo_usuario.grab_set() # so that it does not allow any other accion until the window is closed

        lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
        lblframe_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        
        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Nombre")
        lbl_nombre_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)
        self.txt_nombre_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_nombre_nuevo_usuario.grid(row=0,column=1,padx=10,pady=10)
        
        lbl_nombre_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Usuario")
        lbl_nombre_nuevo_usuario.grid(row=1,column=0,padx=10,pady=10)
        self.txt_user_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_user_nuevo_usuario.grid(row=1,column=1,padx=10,pady=10)

        lbl_clave_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Clave")
        lbl_clave_nuevo_usuario.grid(row=2,column=0,padx=10,pady=10)
        self.txt_clave_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
        self.txt_clave_nuevo_usuario.grid(row=2,column=1,padx=10,pady=10)

        lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Rol")
        lbl_rol_nuevo_usuario.grid(row=3,column=0,padx=10,pady=10)
        self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario, width=38, values=("admin", "usuario",), state="readonly")
        self.txt_rol_nuevo_usuario.grid(row=3,column=1,padx=10,pady=10)
        self.txt_rol_nuevo_usuario.current(0) # set the default value to "Administrador"

        btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario, text="Guardar", width=38,style='success', command=self.guardar_usuario_desde_vista)
        btn_guardar_nuevo_usuario.grid(row=4,column=1,padx=10,pady=10)


    def guardar_usuario_desde_vista(self):
        if self.txt_user_nuevo_usuario.get() == "" or \
        self.txt_nombre_nuevo_usuario.get() == "" or \
        self.txt_clave_nuevo_usuario.get() == "" or \
        self.txt_rol_nuevo_usuario.get() == "":
            messagebox.showwarning("Guardando usuarios", "Rellene todos los campos")
            return

        datos = (
            self.txt_user_nuevo_usuario.get(),
            self.txt_nombre_nuevo_usuario.get(),
            self.txt_clave_nuevo_usuario.get(),
            self.txt_rol_nuevo_usuario.get()
        )

        resultado = self.controller.guardar_usuario(datos)

        if resultado:
            messagebox.showinfo("Guardando usuarios", "Usuario guardado correctamente")
            self.frame_nuevo_usuario.destroy()
            self.mostrar_usuarios()
        else:
            messagebox.showerror("Guardando usuarios", "Error al guardar el usuario")

    def mostrar_usuarios(self):
        try:
            # Limpiar el Treeview
            registros = self.tree_lista_usuarios.get_children()
            for item in registros:
                self.tree_lista_usuarios.delete(item)

            # Obtener datos desde el controlador
            usuarios = self.controller.obtener_usuarios()

            for row in usuarios:
                self.tree_lista_usuarios.insert("", 0, text=row[0], values=row)

        except Exception as e:
            print(f"Error al mostrar usuarios: {e}")

    def center(self, ancho, alto):
        centrar_ventana(self.frame_nuevo_usuario, ancho, alto)
