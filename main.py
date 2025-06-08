from views.login import login_view
import ttkbootstrap as tb

def main():
    app = tb.Window(themename="superhero")
    app.title("Gestor de Tareas 2025")
    app.state("zoomed")

    # 🔧 Hacer que la celda 0,0 del grid se expanda
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    login_view(app)

    app.mainloop()


if __name__ == "__main__":
    main()
