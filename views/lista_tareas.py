from tkinter import LabelFrame, Label, Toplevel, NSEW, W, messagebox, StringVar, ttk
from datetime import datetime
from ttkbootstrap.widgets import DateEntry
import ttkbootstrap as tb
from controllers.tareas import TareasController
from utils.frame_center import centrar_ventana

class view_lista_tareas(tb.Frame):
    def __init__(self, master, usuario_id):
        super().__init__(master)
        self.master = master
        self.usuario_id = usuario_id  

        self.controller = TareasController()
        self.grid(row=0, column=0, sticky=NSEW) 

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

        self.lblframe_busqueda_tareas=LabelFrame(self.frame_lista_tareas)
        self.lblframe_busqueda_tareas.grid(row=1,column=0, padx=10, pady=10,sticky=NSEW)

        self.txt_busqueda_tarea = ttk.Entry(self.lblframe_busqueda_tareas, width=96)
        self.txt_busqueda_tarea.grid(row=0, column=0, padx=5, pady=5)
        self.txt_busqueda_tarea.bind('<KeyRelease>', self.buscar_tareas)


        # Tabla (labelframe del treeview)
        self.lblframe_tree_listatareas = ttk.LabelFrame(self.frame_lista_tareas)
        self.lblframe_tree_listatareas.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        columnas = ("id","titulo", "descripcion", "fecha_inicio", "fecha_vencimiento")
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

        # Scrollbar vertical para el treeview de tareas
        tree_scroll_listatareas = ttk.Scrollbar(self.lblframe_tree_listatareas, orient="vertical", command=self.tree_listatareas.yview)
        tree_scroll_listatareas.grid(row=0, column=1, sticky="ns")

        # Enlazar el scrollbar con el treeview
        self.tree_listatareas.configure(yscrollcommand=tree_scroll_listatareas.set)

        self.refrescar_tareas()

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


        Label(self.form, text="Fecha vencimiento").grid(row=2, column=0, padx=10, pady=10)

        self.date_fecha = DateEntry(self.form, width=20, bootstyle="primary")
        self.date_fecha.grid(row=2, column=1, padx=(10, 0), pady=10, sticky="w")

        Label(self.form, text="Hora").grid(row=3, column=0, padx=10, pady=10)

        horas = [f"{h:02d}:{m:02d}" for h in range(0, 24) for m in (0, 30)] 
        self.combo_hora = ttk.Combobox(self.form, values=horas, width=18)
        self.combo_hora.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.combo_hora.set("08:00") 


        if datos:
            self.txt_titulo.insert(0, datos[1])
            self.txt_descripcion.insert(0, datos[2])

            fecha_str, hora_str = datos[4].split(" ")
            self.date_fecha.entry.delete(0, 'end')
            self.date_fecha.entry.insert(0, fecha_str)

            self.combo_hora.set(hora_str)

            self.tarea_id = datos[0]
            
        btn_guardar = ttk.Button(self.form, text="Guardar", style="success", command=comando)
        btn_guardar.grid(row=3, column=1, pady=20)


    def refrescar_tareas(self):
        for row in self.tree_listatareas.get_children():
            self.tree_listatareas.delete(row)

        tareas = self.controller.obtener_tareas_por_usuario(self.usuario_id)
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

    
    def guardar_tarea(self):
        try:
            titulo = self.txt_titulo.get()
            descripcion = self.txt_descripcion.get()
            fecha_str = f"{self.date_fecha.entry.get().replace('/', '-')} {self.combo_hora.get()}"


            fecha_dt = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
            fecha_formateada = fecha_dt.strftime("%Y-%m-%d %H:%M:%S")

            datos = (
                titulo,
                descripcion,
                fecha_formateada,
                self.usuario_id 
            )

            if self.controller.guardar_tarea(datos):
                messagebox.showinfo("Éxito", "Tarea guardada")
                self.form.destroy()
                self.refrescar_tareas()
            else:
                messagebox.showerror("Error", "No se pudo guardar la tarea")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la tarea: {e}")


    def actualizar_tarea(self):
        try:
            fecha_str = f"{self.date_fecha.entry.get()} {self.combo_hora.get()}"
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            fecha_formateada = fecha_dt.strftime("%Y-%m-%d %H:%M:%S")

            datos = (
                self.txt_titulo.get(),
                self.txt_descripcion.get(),
                fecha_formateada,
                self.tarea_id
            )

            if self.controller.actualizar_tarea(datos):
                messagebox.showinfo("Éxito", "Tarea actualizada")
                self.form.destroy()
                self.refrescar_tareas()
            else:
                messagebox.showerror("Error", "No se pudo actualizar")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la tarea: {e}")

        fecha_dt = datetime.strptime(fecha_str, "%d-%m-%Y %H:%M:%S")
        fecha_formateada = fecha_dt.strftime("%Y-%m-%d %H:%M:%S")
        datos = (
            self.txt_titulo.get(),
            self.txt_descripcion.get(),
            fecha_formateada,
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

    def buscar_tareas(self, event=None):
        texto = self.txt_busqueda_tarea.get().lower()

        for row in self.tree_listatareas.get_children():
            self.tree_listatareas.delete(row)

        tareas = self.controller.obtener_tareas_por_usuario(self.usuario_id)

        tareas_filtradas = [
            tarea for tarea in tareas
            if texto in tarea[0].lower() or texto in tarea[1].lower()
        ]

        for tarea in tareas_filtradas:
            self.tree_listatareas.insert("", "end", values=tarea)

