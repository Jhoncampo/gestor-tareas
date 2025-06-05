from views.login import login_view
import ttkbootstrap as tb

def main():
    app = tb.Window(themename="superhero")
    app.title("Gestor de Tareas 2025")
    app.state("zoomed")

    login_view(app) 

    app.mainloop()

if __name__ == "__main__":
    main()

