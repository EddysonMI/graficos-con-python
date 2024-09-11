import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

ax.plot([10, 20], [20, 40], color='b', label='Línea ')
ax.plot([20, 30], [40, 10], color='b',label='Línea ')

# ax.plot([10, 40],[40,40], )
ax.plot([10, 20],[40,10], )
ax.plot([20, 30],[10,30], )

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
# ax.set_title('')

ax.set_xlim(10, 30)
ax.set_ylim(10, 40)

# Set x-axis ticks to integers between 10 and 30
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

plt.show()
