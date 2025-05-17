# Hacemos las importaciones
from tkinter import ttk
from tkinter import NS, NSEW, W
import ttkbootstrap as tb

# La clase principal que hereda de ttkbootstrap una versión mejorada
class Ventana(tb.Window):
    # Aquí creamos el constructor
    def __init__(self): 
        super().__init__()
        self.ventana_login() # Llamamos a la función que muestra la interfaz login

    def ventana_login(self):
        # Agrupamos todo el login
        self.frame_login=ttk.Frame(self)
        self.frame_login.pack()

        # Le colocamos el titulo al frame
        self.lblframe_login=ttk.LabelFrame(self.frame_login, text='Ingreso')
        self.lblframe_login.pack(padx=10, pady=10)

        # Colocamos titulo principal
        lbltitulo=ttk.Label(self.lblframe_login, text='Inicio de sesión', font=('Arial',22))
        lbltitulo.pack(padx=10,pady=35)
        # Campo de entrada del usuario
        self.txt_usuario=ttk.Entry(self.lblframe_login, width=40, justify='center')
        self.txt_usuario.pack(padx=10, pady=10)

        # Campo de entrada de la clave en este caso la tenemos oculta con "*"
        self.txt_clave=ttk.Entry(self.lblframe_login, width=40, justify='center')
        self.txt_clave.pack(padx=10, pady=10)
        self.txt_clave.configure(show='*')

        # Boton para ingresar al menú
        btn_acceso=ttk.Button(self.lblframe_login, text='Ingresar', width=38, command=self.ingresar)
        btn_acceso.pack(padx=10, pady=10)

    # Función que se encarga de validar el ingreso del usuario (Aún en proceso)
    def ingresar(self):
        self.frame_login.pack_forget()
        self.ventana_menu()
        
    # Vista de la ventana de menú
    def ventana_menu(self):
        # Panel lateral donde van los botones
        self.frame_left=ttk.Frame(self, width=200)
        self.frame_left.grid(row=0,column=0,sticky=NS)
        # Panel central donde va las tablas
        self.frame_center=ttk.Frame(self, width=200)
        self.frame_center.grid(row=0,column=1,sticky=NSEW)

        # Boton tareas que muestra la vista de tareas
        btn_tareas=ttk.Button(self.frame_left, text='Tareas', width=20, command=self.ventana_lista_tareas)
        btn_tareas.grid(row=0,column=0,padx=10,pady=10)
        
        # Boton tareas que muestra la vista de usurios
        btn_usuarios=ttk.Button(self.frame_left, text='Usuarios', width=20, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=1,column=0,padx=10,pady=10)
        

    # Ventana para la vista tareas, incluye información de vista, modificación, eliminación y agregar
    def ventana_lista_tareas(self):
        self.frame_lista_tareas=ttk.Frame(self.frame_center)
        self.frame_lista_tareas.grid(row=0,column=0,columnspan=2, sticky=NSEW)

        self.lblframe_botones_listatareas=ttk.Labelframe(self.frame_lista_tareas)
        self.lblframe_botones_listatareas.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        # Botones básicos para las tareas
        btn_nueva_tarea=tb.Button(self.lblframe_botones_listatareas, text='Nueva tarea', width=18, style='success')
        btn_nueva_tarea.grid(row=0,column=0,padx=5,pady=5)
        btn_modificar_tarea=tb.Button(self.lblframe_botones_listatareas, text='Modificar tarea', width=18, style='warning')
        btn_modificar_tarea.grid(row=0,column=1,padx=5,pady=5)
        btn_eliminar_tarea=tb.Button(self.lblframe_botones_listatareas, text='Eliminar tarea', width=18, style='danger')
        btn_eliminar_tarea.grid(row=0,column=2,padx=5,pady=5)

        # Crea el marco donde va la tabal
        self.lblframe_tree_listatareas=ttk.LabelFrame(self.frame_lista_tareas)
        self.lblframe_tree_listatareas.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW)

        # Las columnas que tendra la tabla
        columnas=("id","titulo", "descripcion", "fecha_inicio", "fecha_vencimiento")
        # widget donde se montrará la informaición de la tabla
        self.tree_lista_tareas=tb.Treeview(self.lblframe_tree_listatareas, columns=columnas, height=17, show='headings', style='dark')
        self.tree_lista_tareas.grid(row=0,column=0)

        # Definimos los encabezados de la tabla
        self.tree_lista_tareas.heading("id", text="ID", anchor=W)
        self.tree_lista_tareas.heading("titulo", text="Titulo", anchor=W)
        self.tree_lista_tareas.heading("descripcion", text="Descripción", anchor=W)
        self.tree_lista_tareas.heading("fecha_inicio", text="Fecha inicio", anchor=W)
        self.tree_lista_tareas.heading("fecha_vencimiento", text="Fecha final", anchor=W)


    # Ventana para la vista usuarios, incluye información de vista, modificación, eliminación y agregar
    # Lo mismo que la vista de tareas
    def ventana_lista_usuarios(self):
        self.frame_lista_usuarios=ttk.Frame(self.frame_center)
        self.frame_lista_usuarios.grid(row=0,column=0,columnspan=2, sticky=NSEW)

        self.lblframe_botones_listausuarios=ttk.Labelframe(self.frame_lista_usuarios)
        self.lblframe_botones_listausuarios.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

        btn_nuevo_usuario=tb.Button(self.lblframe_botones_listausuarios, text='Nuevo usuario', width=18, style='success')
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
            


# Punto de entrada de nuestra aplicación
def main():
    app=Ventana()
    app.title("Gestor tareas")
    app.state("zoomed") # Iniciamos la pantalla maximizada
    tb.Style("superhero")
    app.mainloop()

# Validamos que el archivo se este ejecutando directamente
if __name__=="__main__":
    main()

