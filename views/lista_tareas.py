from tkinter import ttk
from tkinter import NS, NSEW, W
import ttkbootstrap as tb

def mostrar_lista_tareas(self):
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