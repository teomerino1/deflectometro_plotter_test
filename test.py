import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cambiar Color de Frames")

        # Crear el primer Frame (config_frame)
        config_frame = tk.Frame(self.root)
        config_frame.pack()

        # Crear el segundo Frame (parameters_frame)
        parameters_frame = tk.Frame(config_frame, relief="groove")
        parameters_frame.pack()

        # Cambiar el color de fondo del segundo Frame
        parameters_frame.configure(bg="blue")

        # Crear el tercer Frame (reportes_frame)
        reportes_frame = tk.Frame(config_frame, relief="solid")
        reportes_frame.pack()

        # Cambiar el color de fondo del tercer Frame
        reportes_frame.configure(bg="green")

        # Crear el cuarto Frame (botones_frame)
        botones_frame = tk.Frame(config_frame, relief="ridge")
        botones_frame.pack()

        # Cambiar el color de fondo del cuarto Frame
        botones_frame.configure(bg="red")

        # Crear el quinto Frame (info_infas_frame)
        info_infas_frame = tk.Frame(config_frame, relief="ridge")
        info_infas_frame.pack()

        # Cambiar el color de fondo del quinto Frame
        info_infas_frame.configure(bg="yellow")

        # Crear el sexto Frame (imagenes_frame)
        imagenes_frame = tk.Frame(config_frame, relief="ridge")
        imagenes_frame.pack()

        # Cambiar el color de fondo del sexto Frame
        imagenes_frame.configure(bg="purple")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
