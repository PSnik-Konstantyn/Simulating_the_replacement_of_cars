import numpy as np
import matplotlib.pyplot as plt

years = 1
initial_dvz_share = 0.8
initial_ev_share = 0.2

dvz_params = {"price": 20000, "fuel_cost_per_km": 0.12, "maintenance_cost": 600}
ev_params = {"price": 30000, "electricity_cost_per_km": 0.05, "maintenance_cost": 300}

# Марковська матриця переходів, наприклад
# P[DVZ->DVZ, DVZ->EV, EV->DVZ, EV->EV]
transition_matrix = np.array([
    [0.9, 0.1],
    [0.05, 0.8]
])

# Ініціалізація масиву для зберігання часток автомобілів
dvz_share = [initial_dvz_share]
ev_share = [initial_ev_share]

# Симуляція з використанням марковських переходів
for _ in range(1, years + 1):
    # Попередні частки
    current_dvz_share = dvz_share[-1]
    current_ev_share = ev_share[-1]

    # Нові частки з використанням матриці переходів
    new_dvz_share = transition_matrix[0, 0] * current_dvz_share + transition_matrix[1, 0] * current_ev_share
    new_ev_share = transition_matrix[0, 1] * current_dvz_share + transition_matrix[1, 1] * current_ev_share

    # Додаємо нові значення
    dvz_share.append(new_dvz_share)
    ev_share.append(new_ev_share)

# Побудова графіків для часток автомобілів з ДВЗ та електромобілів
years_range = np.arange(0, years + 1)
plt.plot(years_range, dvz_share, label="Частка ДВЗ", color='r')
plt.plot(years_range, ev_share, label="Частка електромобілів", color='g')
plt.xlabel("Роки")
plt.ylabel("Частка")
plt.title("Зміна частки автомобілів з ДВЗ та електромобілів з часом")
plt.legend()
plt.grid()
plt.show()
