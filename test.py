
        
import matplotlib.pyplot as plt

# Crea una figura y un conjunto de subplots
fig = plt.figure()
ax = fig.add_subplot(111)

# Define los datos para el gráfico de barras
categorias = ['A', 'B', 'C', 'D']
valores = [10, 15, 7, 12]

# Crea el gráfico de barras
ax.bar(categorias, valores)

# Ajusta la posición y el tamaño del gráfico dentro de la figura
ax.set_position([0.3, 0.3, 0.4, 0.8])

# Muestra la figura
plt.show()
