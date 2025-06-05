from tkinter import Toplevel, ttk, messagebox
from datetime import datetime

class TareasView(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Lista de tareas")
        self.geometry("700x400+300+200")
        self.resizable(False, False)
        self.grab_set()
        self.configurar_interfaz()

    def configurar_interfaz(self):
        ttk.Label(self, text='Lista de tareas', font=('Arial', 18)).pack(pady=10)

        tabla_frame = ttk.Frame(self)
        tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

        columnas = ("id", "titulo", "vencimiento", "estado")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, anchor="center")

        self.tabla.pack(fill="both", expand=True)

        ttk.Button(self, text="Agregar tarea", command=self.agregar_tarea).pack(pady=10)

        # Datos de ejemplo
        self.tareas = []
        self.cargar_tareas_demo()

    def cargar_tareas_demo(self):
        self.tareas = [
            {"id": 1, "titulo": "Tarea 1", "vencimiento": "2025-06-10", "estado": "pendiente"},
            {"id": 2, "titulo": "Tarea 2", "vencimiento": "2025-06-15", "estado": "completada"},
        ]
        for tarea in self.tareas:
            self.tabla.insert("", "end", values=(tarea["id"], tarea["titulo"], tarea["vencimiento"], tarea["estado"]))

    def agregar_tarea(self):
        # Esta función es de ejemplo; luego puedes abrir un formulario real
        nueva_tarea = {
            "id": len(self.tareas) + 1,
            "titulo": f"Tarea {len(self.tareas) + 1}",
            "vencimiento": datetime.now().strftime("%Y-%m-%d"),
            "estado": "pendiente"
        }
        self.tareas.append(nueva_tarea)
        self.tabla.insert("", "end", values=(nueva_tarea["id"], nueva_tarea["titulo"], nueva_tarea["vencimiento"], nueva_tarea["estado"]))
        messagebox.showinfo("Tarea agregada", "Tarea añadida correctamente.")
