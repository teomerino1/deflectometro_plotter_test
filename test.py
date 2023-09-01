import tkinter as tk

def actualizar_estado():
    # Aquí debes implementar la lógica para determinar el estado actual del programa
    # Por ejemplo, puedes usar variables o consultas a la base de datos
    estado_actual = obtener_estado_actual()
    
    # Actualizar la etiqueta con el nuevo estado
    estado_label.config(text=f'Estado: {estado_actual}')
    
    # Programar la próxima actualización después de un cierto tiempo (en milisegundos)
    ventana.after(1000, cambiar_estado)  # Actualiza cada 1000ms (1 segundo)

def cambiar_estado():
    # Simula un cambio de estado después de 1 segundo
    estado_label.config(text='Estado actualizado')
    
    # Programar la próxima actualización después de un cierto tiempo (en milisegundos)
    ventana.after(1000, actualizar_estado)  # Actualiza cada 1000ms (1 segundo)

# Función de ejemplo para obtener el estado actual
def obtener_estado_actual():
    # Aquí puedes implementar tu propia lógica para determinar el estado
    # Puedes consultar la base de datos, verificar condiciones, etc.
    return 'Obteniendo datos'  # Cambia esto según tu lógica real

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Programa con Estado en Tiempo Real')

# Crear una etiqueta para mostrar el estado
estado_label = tk.Label(ventana, text='', font=('Arial', 12))
estado_label.pack()

# Iniciar la actualización del estado
actualizar_estado()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
