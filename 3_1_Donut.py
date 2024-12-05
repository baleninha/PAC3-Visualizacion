import pandas as pd
import matplotlib.pyplot as plt

# CON MATPLOTLIB (Gráfico estático, ejecuciónmmás ligera)
data = pd.read_csv('hotel_bookings.csv')


def plot_donut(hotel_name, ax):

    hotel_data = data[data['hotel'] == hotel_name]

    hotel_data = hotel_data[hotel_data['country'] != 'PRT']

    nationality_counts = hotel_data['country'].value_counts()

    total_clients = nationality_counts.sum()
    percentages = (nationality_counts / total_clients) * 100

    top_5_nationalities = percentages[:5]
    others_percentage = percentages[5:].sum()
    top_5_nationalities['Otros'] = others_percentage

    labels = top_5_nationalities.index
    sizes = top_5_nationalities.values
    colors = ['#6BAED6', '#FF6F61', '#74C476', '#9E9AC8', '#FFA07A', '#999999']

    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85
    )

    ax.pie([1], radius=0.7, colors=['white'])

    ax.set_title(f"Top 5 Nacionalidades ({hotel_name})", fontsize=16, fontweight='bold')
    for text in texts:
        text.set_fontsize(12)
    for autotext in autotexts:
        autotext.set_fontsize(10)

fig, axs = plt.subplots(1, 2, figsize=(18, 9), dpi=100)

plot_donut("Resort Hotel", axs[0])

plot_donut("City Hotel", axs[1])

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("Top 5 Nacionalidades de Clientes Extranjeros", fontsize=20, fontweight='bold')
plt.show()




"""
-----------------
CON PLOTLY
-----------------


import plotly.graph_objects as go


def create_donut(hotel_name):
    hotel_data = data[data['hotel'] == hotel_name]

    hotel_data = hotel_data[hotel_data['country'] != 'PRT']

    nationality_counts = hotel_data['country'].value_counts()

    total_clients = nationality_counts.sum()
    percentages = (nationality_counts / total_clients) * 100

    top_5_nationalities = percentages[:5]
    others_percentage = percentages[5:].sum()
    top_5_nationalities['Otros'] = others_percentage

    labels = top_5_nationalities.index
    values = top_5_nationalities.values

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.6,  # Crear el efecto de donut
                textinfo='percent+label',  # Mostrar etiquetas y porcentajes
                marker=dict(colors=['#6BAED6', '#FF6F61', '#74C476', '#9E9AC8', '#FFA07A', '#999999']),
                hoverinfo='label+percent+value',  # Información al pasar el cursor
            )
        ]
    )

    fig.update_layout(
        title=f"Top 5 Nacionalidades Extranjeras ({hotel_name})",
        title_x=0.5,
        showlegend=False,
        font=dict(size=14),
    )
    return fig

fig_resort = create_donut("Resort Hotel")
fig_city = create_donut("City Hotel")

fig_resort.show()
fig_city.show()
"""