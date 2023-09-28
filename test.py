class TuClase:
    def __init__(self):
        self.contador_graficos = 0
        self.current_dataset = 0  # Variable para realizar un seguimiento del conjunto de datos actual

    def create_arrays(self):
        self.contador_graficos += 1
        new_defl_r_data = f"self.defl_r_data_{self.contador_graficos}"
        setattr(self, new_defl_r_data, [])
        new_defl_l_data = f"self.defl_l_data_{self.contador_graficos}"
        setattr(self, new_defl_l_data, [])
        new_indexes = f"self.indexes_{self.contador_graficos}"
        setattr(self, new_indexes, [])

    def select_dataset(self, dataset_number):
        self.current_dataset = dataset_number

    def get_selected_dataset(self):
        dataset_name = f"self.defl_r_data_{self.current_dataset}"
        return getattr(self, dataset_name)

    # Otras funciones para agregar datos a los conjuntos de datos y actualizar el gráfico en Figure

# Ejemplo de uso:
mi_objeto = TuClase()

# Crear nuevos conjuntos de datos
mi_objeto.create_arrays()

# Selección inicial del conjunto de datos (por ejemplo, seleccionar el conjunto de datos 1)
mi_objeto.select_dataset(1)

# Acceder al conjunto de datos seleccionado
dataset = mi_objeto.get_selected_dataset()

# Agregar datos al conjunto de datos seleccionado
dataset.append(10)
dataset.append(20)

# Actualizar el gráfico en el objeto Figure con los datos del conjunto de datos seleccionado
# (debes tener una función para realizar esta actualización)

import tkinter as tk
from tkinter import ttk, Radiobutton

def mostrar_menu():
    deflexiones_message = tk.Toplevel(root)

    deflexiones_message.title("Deflexiones")
    message_label = tk.Label(deflexiones_message, text="¿Cómo desea el gráfico de las deflexiones individuales?", font=(None, 12))
    var = tk.IntVar()
    var.set(1)  # Establecer 'Total' como predeterminado
    parcial = Radiobutton(deflexiones_message, text='Parcial', variable=var, value=0)
    total = Radiobutton(deflexiones_message, text='Total', variable=var, value=1)
    ok = ttk.Button(deflexiones_message, text="Ok", style="TButton")

    deflexiones_message.protocol("WM_DELETE_WINDOW", lambda: None)  # Evitar cerrar la ventana

    def continuar():
        deflexiones_message.destroy()  # Cerrar la ventana del menú
        root.update()  # Actualizar la ventana principal
        # El código continúa aquí después de que el usuario hace clic en "Ok"
        seleccion_usuario = var.get()
        print("Selección del usuario:", seleccion_usuario)

    ok.config(command=continuar)  # Asignar la función "continuar" al botón "Ok"

    message_label.pack()
    parcial.pack()
    total.pack()
    ok.pack()

root = tk.Tk()
mostrar_menu()
root.mainloop()
