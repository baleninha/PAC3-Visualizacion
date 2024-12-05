import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('hotel_bookings.csv')

def calculate_show_vs_cancel(hotel_name):

    hotel_data = data[data['hotel'] == hotel_name]

    total_bookings = len(hotel_data)
    cancellations = len(hotel_data[hotel_data['is_canceled'] == 1])
    shows = total_bookings - cancellations

    cancellation_percentage = round((cancellations / total_bookings) * 100)
    show_percentage = 100 - cancellation_percentage

    return cancellation_percentage, show_percentage

resort_cancel, resort_show = calculate_show_vs_cancel("Resort Hotel")
city_cancel, city_show = calculate_show_vs_cancel("City Hotel")

labels = ['Resort Hotel', 'City Hotel']
cancel_percentages = [resort_cancel, city_cancel]
show_percentages = [resort_show, city_show]


fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(labels, cancel_percentages, label='Cancelaciones/No Apariciones', color='#FF6F61')
bar2 = ax.bar(labels, show_percentages, bottom=cancel_percentages, label='Clientes Presentados', color='#6BAED6')

for bar in bar1:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f"{int(bar.get_height())}%", ha='center', va='center', color='white', fontsize=12)

for bar in bar2:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + bar.get_y() + 2, f"{int(bar.get_height())}%", ha='center', va='center', color='white', fontsize=12)


ax.set_title('Porcentaje de Cancelaciones vs Clientes Presentados', fontsize=16, fontweight='bold')
ax.set_ylabel('Porcentaje (%)', fontsize=14)
ax.set_ylim(0, 100)
ax.legend(fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
