import pandas as pd
import plotly.express as px

data = pd.read_csv('hotel_bookings.csv')

def create_robinson_map(hotel_name):
    hotel_data = data[(data['hotel'] == hotel_name) & (data['country'] != 'PRT')]

    country_counts = hotel_data['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']

    #número total de países únicos
    total_countries = len(country_counts)

    fig = px.choropleth(
        country_counts,
        locations='country',
        color='count',
        hover_name='country',
        title=f"Distribución de Clientes Extranjeros - {hotel_name} (Total Países: {total_countries})",
        color_continuous_scale=px.colors.sequential.Blues,
        projection="robinson"
    )

    fig.update_geos(
        showframe=False,
        showcoastlines=False, 
        showland=True,
        landcolor='lightgrey',
        oceancolor='aliceblue'
    )

    fig.update_layout(
        title=dict(
            x=0.5,
            font=dict(size=20, family="Arial", color="black")
        ),
        coloraxis_colorbar=dict(
            title="Clientes",
            titlefont=dict(size=14, family="Arial", color="black"),
            tickfont=dict(size=12, family="Arial", color="black")
        )
    )
    return fig

fig_resort = create_robinson_map("Resort Hotel")
fig_resort.show()

fig_city = create_robinson_map("City Hotel")
fig_city.show()
