import tkinter as tk
from tkinter import ttk

class MiPrograma:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Programa")

        self.botones_frame = ttk.Frame(root)
        self.botones_frame.pack(padx=20, pady=20)

        self.configuration_button = ttk.Button(self.botones_frame, text="Ver configuración", style="TButton", command=self.mostrar_configuracion)
        self.configuration_button.pack()

    def mostrar_configuracion(self):
        # Crear una ventana emergente (Toplevel)
        ventana_emergente = tk.Toplevel(self.root)
        ventana_emergente.title("Configuración")

        # Agregar contenido a la ventana emergente
        etiqueta = ttk.Label(ventana_emergente, text="Aquí va la información de configuración")
        etiqueta.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiPrograma(root)
    root.mainloop()
