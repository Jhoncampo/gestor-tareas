from tkinter import NSEW, NS
from tkinter import ttk
from ttkbootstrap import Frame, Label

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
        btn_tareas = ttk.Button(self.frame_left, text='Tareas', width=20)
        btn_tareas.grid(row=0, column=0, padx=10, pady=10)

        btn_usuarios = ttk.Button(self.frame_center, text='Usuarios', width=20, command=self.ventana_lista_usuarios)
        btn_usuarios.grid(row=1, column=0, padx=10, pady=10)

        btn_productos = ttk.Button(self.frame_right, text='Productos', width=20)
        btn_productos.grid(row=2, column=0, padx=10, pady=10)

        btn_ventas = ttk.Button(self.frame_left, text='Ventas', width=20)
        btn_ventas.grid(row=3, column=0, padx=10, pady=10)

        btn_clientes = ttk.Button(self.frame_left, text='Clientes', width=20)
        btn_clientes.grid(row=4, column=0, padx=10, pady=10)

        btn_compras = ttk.Button(self.frame_left, text='Compras', width=20)
        btn_compras.grid(row=5, column=0, padx=10, pady=10)

        btn_reportes = ttk.Button(self.frame_left, text='Reportes', width=20)
        btn_reportes.grid(row=6, column=0, padx=10, pady=10)

        btn_backup = ttk.Button(self.frame_left, text='Backup', width=20)
        btn_backup.grid(row=7, column=0, padx=10, pady=10)

        btn_restauradb = ttk.Button(self.frame_left, text='Restaurar DB', width=20)
        btn_restauradb.grid(row=8, column=0, padx=10, pady=10)

        # Etiquetas explicativas en panel central y derecho
        lbl_center = ttk.Label(self.frame_center, text='Aquí pondremos las ventanas que creemos')
        lbl_center.grid(row=0, column=0, padx=10, pady=10)

        lbl_right = ttk.Label(self.frame_right, text='Aquí pondremos las búsquedas para la venta')
        lbl_right.grid(row=0, column=0, padx=10, pady=10)


    def ventana_lista_usuarios(self):
        print("Mostrando lista de usuarios... (Aún no implementado)")
