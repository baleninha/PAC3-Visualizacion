import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('hotel_bookings.csv')

#Función para crear la matriz de círculos
def create_circle_matrix(hotel_name, ax):
    #Filtrar datos para cada hotel
    hotel_data = data[data['hotel'] == hotel_name]

    #Calcular el porcentaje de clientes portugueses y otros
    total_clients = len(hotel_data)
    portuguese_clients = len(hotel_data[hotel_data['country'] == 'PRT'])
    other_clients = total_clients - portuguese_clients

    portuguese_percentage = round((portuguese_clients / total_clients) * 100)
    other_percentage = 100 - portuguese_percentage

    #Colores
    colors = ['#FFD580'] * portuguese_percentage + ['#D3D3D3'] * other_percentage  #Amarillo anaranjado pastel y gris claro

    #matriz de 100 círculos
    ax.set_aspect('equal')
    for i in range(10):
        for j in range(10):
            index = i * 10 + j
            if index < len(colors):
                circle = plt.Circle((j, 9 - i), 0.4, color=colors[index], edgecolor='black', linewidth=0.5)
                ax.add_artist(circle)

    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.axis('off')
    ax.set_title(f"Distribución de Clientes - {hotel_name}", fontsize=16, fontweight='bold')

    ax.text(5, -1.5, f"Portugueses: {portuguese_percentage}%", fontsize=14, color='#FFD580', ha='center')
    ax.text(5, -2.5, f"Otros Países: {other_percentage}%", fontsize=14, color='#D3D3D3', ha='center')


fig, axs = plt.subplots(1, 2, figsize=(18, 9), dpi=100)
fig.suptitle("Distribución de Clientes por Nacionalidad", fontsize=20, fontweight='bold')

create_circle_matrix("Resort Hotel", axs[0])

create_circle_matrix("City Hotel", axs[1])

orange_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD580', markersize=12, label='Portugueses')
gray_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#D3D3D3', markersize=12, label='Otros Países')
fig.legend(handles=[orange_patch, gray_patch], loc='lower center', fontsize=14, ncol=2, frameon=False)

plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.show()
