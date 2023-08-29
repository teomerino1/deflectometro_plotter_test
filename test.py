import tkinter as tk

root = tk.Tk()
root.title("Cambiar Color del Frame")

# Crear el Frame
config_frame = tk.Frame(root, text="Hola",relief="groove")
config_frame.pack(padx=20, pady=20)

# Cambiar el color de fondo del Frame
config_frame["bg"] = "blue"

root.mainloop()
