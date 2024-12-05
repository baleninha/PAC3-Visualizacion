import pandas as pd
import plotly.graph_objects as go

"""

Código para mostrar el porcentaje de reservas de nuevos clientes vs. clientes repetidos

"""

data = pd.read_csv('hotel_bookings.csv')

def create_repeated_guest_chart(hotel_name):

    hotel_data = data[data['hotel'] == hotel_name]

    counts = hotel_data['is_repeated_guest'].value_counts()
    total_reservations = counts.sum()

    percentages = (counts / total_reservations) * 100

    labels = ['Nuevos Clientes', 'Clientes Repetidos']
    values = [percentages.get(0, 0), percentages.get(1, 0)]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.5, 
                textinfo='percent+label',  
                marker=dict(colors=['#6BAED6', '#FF6F61']),
                hoverinfo='label+percent+value',  
            )
        ]
    )

    fig.update_layout(
        title=f"Porcentaje de Reservas ({hotel_name})",
        title_x=0.5,
        font=dict(size=14),
        showlegend=True,
    )
    return fig


fig_resort = create_repeated_guest_chart("Resort Hotel")
fig_city = create_repeated_guest_chart("City Hotel")

fig_resort.show()
fig_city.show()
