import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('hotel_bookings.csv')


data['arrival_date_month'] = pd.Categorical(
    data['arrival_date_month'], 
    categories=['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True
)


resort_data = data[data['hotel'] == "Resort Hotel"]
city_data = data[data['hotel'] == "City Hotel"]


resort_counts = resort_data['arrival_date_month'].value_counts(normalize=True).sort_index() * 100
city_counts = city_data['arrival_date_month'].value_counts(normalize=True).sort_index() * 100


fig, axs = plt.subplots(1, 2, figsize=(18, 8), sharey=True)


axs[0].bar(resort_counts.index, resort_counts.values, color='#6BAED6', alpha=0.8)
axs[0].set_title("Reservas por Mes - Resort Hotel (Porcentaje)", fontsize=16, fontweight='bold')
axs[0].set_xlabel("Mes", fontsize=14)
axs[0].set_ylabel("Porcentaje de Reservas (%)", fontsize=14)
axs[0].tick_params(axis='x', rotation=45)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)


axs[1].bar(city_counts.index, city_counts.values, color='#FF6F61', alpha=0.8)
axs[1].set_title("Reservas por Mes - City Hotel (Porcentaje)", fontsize=16, fontweight='bold')
axs[1].set_xlabel("Mes", fontsize=14)
axs[1].tick_params(axis='x', rotation=45)
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.suptitle("Porcentaje de Reservas por Mes para Cada Hotel", fontsize=20, fontweight='bold', y=1.02)
plt.show()



