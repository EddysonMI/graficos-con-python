import matplotlib.pyplot as plt

fig, ax = plt.subplots()


ax.plot([0, 2], [2, 4], label='Línea Diagonal en x=2')



ax.plot([2, 3], [4, 0], label='Línea Vertical en x=3')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Ejemplo de Línea Diagonal')
ax.legend()



ax.set_xlim(0, 3)
ax.set_ylim(0, 4)



plt.show()