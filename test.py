import tkinter as tk

root = tk.Tk()

config_frame = tk.Frame(root)
config_frame.grid()

# Configurar el número de filas y columnas
config_frame.grid_rowconfigure(0, weight=1)
config_frame.grid_rowconfigure(1, weight=1)
config_frame.grid_rowconfigure(2, weight=1)
config_frame.grid_rowconfigure(3, weight=1)
# config_frame.grid_rowconfigure(4, weight=1)
config_frame.grid_columnconfigure(0, weight=1)
config_frame.grid_columnconfigure(1, weight=1)
config_frame.grid_columnconfigure(2, weight=1)
config_frame.grid_columnconfigure(3, weight=1)
# config_frame.grid_columnconfigure(4, weight=1)


# Crear elementos y colocarlos en filas y columnas específicas
elemento1 = tk.Label(config_frame, text="Elemento 1")
elemento1.grid(row=0, column=0)

elemento2 = tk.Label(config_frame, text="Elemento 2")
elemento2.grid(row=0, column=1)

elemento3 = tk.Label(config_frame, text="Elemento 3")
elemento3.grid(row=0, column=2)

elemento4 = tk.Label(config_frame, text="Elemento 4")
elemento4.grid(row=0, column=3)

elemento5 = tk.Label(config_frame, text="Elemento 5")
elemento5.grid(row=1, column=0)

elemento6 = tk.Label(config_frame, text="Elemento 6")
elemento6.grid(row=1, column=1)

elemento7 = tk.Label(config_frame, text="Elemento 7")
elemento7.grid(row=1, column=2)

elemento8 = tk.Label(config_frame, text="Elemento 8")
elemento8.grid(row=1, column=3)

elemento9 = tk.Label(config_frame, text="Elemento 9")
elemento9.grid(row=2, column=0)

elemento10 = tk.Label(config_frame, text="Elemento 10")
elemento10.grid(row=2, column=1)

elemento11 = tk.Label(config_frame, text="Elemento 11")
elemento11.grid(row=2, column=2)

elemento12 = tk.Label(config_frame, text="Elemento 12")
elemento12.grid(row=2, column=3)

root.mainloop()

