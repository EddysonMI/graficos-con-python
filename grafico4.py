import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la primera línea (diagonal)
ax.plot([0, 4], [2, 6], marker='o', linestyle='-', color='b', label='Línea Diagonal en x=2')

# Graficar la segunda línea (vertical)
ax.plot([5, 4], [3, 6], marker='s', linestyle='--', color='r', label='Línea Vertical en x=3')

# Graficar la segunda línea (vertical)
ax.plot([5, 6], [3, 6], marker='s', linestyle='--', color='r', label='Línea Vertical en x=3')

# Graficar la segunda línea (vertical)
ax.plot([7, 6], [3, 6], marker='s', linestyle='--', color='r', label='Línea Vertical en x=3')



# Configurar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Ejemplo de Líneas Diagonales y Verticales')
ax.legend()

# Establecer los límites de los ejes
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

# Configurar los ticks del eje x e y para mostrar solo enteros
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Mostrar el gráfico
plt.show()