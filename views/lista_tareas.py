from tkinter import LabelFrame, Label, Toplevel, NSEW, W, messagebox
from tkinter import ttk
import ttkbootstrap as tb
from controllers.tareas import TareasController
from utils.frame_center import centrar_ventana

class view_lista_tareas(tb.Frame):
    def __init__(self, master, usuario_id):
        super().__init__(master)
        self.master = master
        self.usuario_id = usuario_id  # ✅ GUARDA el id del usuario

        print("usuario_id recibido:", usuario_id)

        self.controller = TareasController()
        self.grid(row=0, column=0, sticky=NSEW)  # Estaba en column=1 (⬅️ posiblemente error)

        self.mostrar_lista_tareas()

    def mostrar_lista_tareas(self):
        self.frame_lista_tareas = ttk.Frame(self)
        self.frame_lista_tareas.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        # Botonera (labelframe de acciones)
        self.lblframe_botones_listatareas = ttk.Labelframe(self.frame_lista_tareas)
        self.lblframe_botones_listatareas.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        btn_nueva_tarea = tb.Button(
            self.lblframe_botones_listatareas,
            text='Nueva tarea',
            width=18,
            style='success',
            command=self.ventana_nueva_tarea
        )
        btn_nueva_tarea.grid(row=0, column=0, padx=5, pady=5)

        btn_editar_tarea = tb.Button(
            self.lblframe_botones_listatareas,
            text='Editar tarea',
            width=18,
            style='warning',
            command=self.ventana_editar_tarea
        )
        btn_editar_tarea.grid(row=0, column=1, padx=5, pady=5)

        btn_eliminar_tarea = tb.Button(
            self.lblframe_botones_listatareas,
            text='Eliminar tarea',
            width=18,
            style='danger',
            command=self.eliminar_tarea
        )
        btn_eliminar_tarea.grid(row=0, column=2, padx=5, pady=5)

        # Tabla (labelframe del treeview)
        self.lblframe_tree_listatareas = ttk.LabelFrame(self.frame_lista_tareas)
        self.lblframe_tree_listatareas.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id", "titulo", "descripcion", "fecha_inicio", "fecha_vencimiento")
        self.tree_listatareas = tb.Treeview(
            self.lblframe_tree_listatareas,
            columns=columnas,
            show="headings",
            height=17,
            style='dark'
        )
        self.tree_listatareas.grid(row=0, column=0)

        for col in columnas:
            self.tree_listatareas.heading(col, text=col.capitalize(), anchor=W)

        self.refrescar_tareas()


    def refrescar_tareas(self):
        for row in self.tree_listatareas.get_children():
            self.tree_listatareas.delete(row)

        tareas = self.controller.obtener_tareas_por_usuario(self.usuario_id)  # ✅ ahora dinámico
        for tarea in tareas:
            self.tree_listatareas.insert("", "end", values=tarea)

    def ventana_nueva_tarea(self):
        self.ventana_formulario("Nueva tarea", self.guardar_tarea)

    def ventana_editar_tarea(self):
        seleccion = self.tree_listatareas.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea para editar.")
            return
        valores = self.tree_listatareas.item(seleccion[0], "values")
        self.ventana_formulario("Editar tarea", self.actualizar_tarea, valores)

    def ventana_formulario(self, titulo, comando, datos=None):
        self.form = Toplevel(self.master)
        self.form.title(titulo)
        centrar_ventana(self.form, 600, 300)
        self.form.grab_set()

        Label(self.form, text="Título").grid(row=0, column=0, padx=10, pady=10)
        self.txt_titulo = ttk.Entry(self.form, width=40)
        self.txt_titulo.grid(row=0, column=1, padx=10, pady=10)

        Label(self.form, text="Descripción").grid(row=1, column=0, padx=10, pady=10)
        self.txt_descripcion = ttk.Entry(self.form, width=40)
        self.txt_descripcion.grid(row=1, column=1, padx=10, pady=10)

        Label(self.form, text="Fecha vencimiento (YYYY-MM-DD HH:MM)").grid(row=2, column=0, padx=10, pady=10)
        self.txt_fecha = ttk.Entry(self.form, width=40)
        self.txt_fecha.grid(row=2, column=1, padx=10, pady=10)

        if datos:
            self.txt_titulo.insert(0, datos[1])
            self.txt_descripcion.insert(0, datos[2])
            self.txt_fecha.insert(0, datos[4])
            self.tarea_id = datos[0]

        btn_guardar = ttk.Button(self.form, text="Guardar", style="success", command=comando)
        btn_guardar.grid(row=3, column=1, pady=20)

    def guardar_tarea(self):
        datos = (
            self.txt_titulo.get(),
            self.txt_descripcion.get(),
            self.txt_fecha.get(),
            self.usuario_id  # ✅
        )
        if self.controller.guardar_tarea(datos):
            messagebox.showinfo("Éxito", "Tarea guardada")
            self.form.destroy()
            self.refrescar_tareas()
        else:
            messagebox.showerror("Error", "No se pudo guardar la tarea")

    def actualizar_tarea(self):
        datos = (
            self.txt_titulo.get(),
            self.txt_descripcion.get(),
            self.txt_fecha.get(),
            self.tarea_id
        )
        if self.controller.actualizar_tarea(datos):
            messagebox.showinfo("Éxito", "Tarea actualizada")
            self.form.destroy()
            self.refrescar_tareas()
        else:
            messagebox.showerror("Error", "No se pudo actualizar")

    def eliminar_tarea(self):
        seleccion = self.tree_listatareas.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona una tarea", "Debes seleccionar una tarea para eliminar.")
            return
        tarea_id = self.tree_listatareas.item(seleccion[0], "values")[0]
        if messagebox.askyesno("Eliminar", "¿Seguro que quieres eliminar esta tarea?"):
            if self.controller.eliminar_tarea(tarea_id):
                messagebox.showinfo("Éxito", "Tarea eliminada")
                self.refrescar_tareas()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")
