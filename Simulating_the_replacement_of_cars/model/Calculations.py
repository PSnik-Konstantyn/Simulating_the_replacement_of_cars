import numpy as np
import matplotlib.pyplot as plt


def calculate_transition_matrix(fuel_price, electricity_price, dvz_maintenance_factor, ev_maintenance_factor,
                                dvz_range, ev_range, charging_speed, refueling_speed, ev_subsidy, dvz_subsidy):

    price_factor = electricity_price / (fuel_price + electricity_price)
    subsidy_factor = ev_subsidy / (ev_subsidy + dvz_subsidy + 1e-6)

    maintenance_factor = ev_maintenance_factor / (dvz_maintenance_factor + ev_maintenance_factor)
    range_factor = ev_range / (dvz_range + ev_range)
    speed_factor = charging_speed / (charging_speed + refueling_speed)

    # Розрахунок імовірностей
    p_dvz_to_dvz = 0.7 + 0.2 * (1 - price_factor) + 0.1 * (1 - maintenance_factor)
    p_dvz_to_ev = 1 - p_dvz_to_dvz

    p_ev_to_ev = 0.7 + 0.2 * price_factor + 0.1 * (subsidy_factor + maintenance_factor + range_factor + speed_factor)
    p_ev_to_dvz = 1 - p_ev_to_ev

    # Формування матриці переходу
    transition_matrix = np.array([
        [p_dvz_to_dvz, p_dvz_to_ev],
        [p_ev_to_dvz, p_ev_to_ev]
    ])

    # Нормалізація для точності
    transition_matrix = transition_matrix / transition_matrix.sum(axis=1, keepdims=True)

    print (transition_matrix)

    return transition_matrix


def simulate_changing(initial_dvz_share, initial_ev_share, years, transition_matrix):
    dvz_share = [float(initial_dvz_share)]
    ev_share = [float(initial_ev_share)]

    # Симуляція з використанням марковських переходів
    for _ in range(1, years + 1):
        # Попередні частки
        current_dvz_share = dvz_share[-1]
        current_ev_share = ev_share[-1]

        # Нові частки з використанням матриці переходів
        new_dvz_share = transition_matrix[0, 0] * current_dvz_share + transition_matrix[1, 0] * current_ev_share
        new_ev_share = transition_matrix[0, 1] * current_dvz_share + transition_matrix[1, 1] * current_ev_share

        # Нормалізація до 100% у разі розбіжностей
        total_share = new_dvz_share + new_ev_share
        if total_share != 1.0:  # Перевірка на суму
            correction = 1.0 - total_share
            new_dvz_share += correction  # Додаємо залишок до частки ДВЗ

        # Додаємо нові значення
        dvz_share.append(float(new_dvz_share))
        ev_share.append(float(new_ev_share))

    # Конвертація часток у відсотки
    dvz_share_percent = [round(share * 100, 2) for share in dvz_share]
    ev_share_percent = [round(share * 100, 2) for share in ev_share]

    # Формування результату у вигляді мапи
    result = {i: (dvz_share_percent[i], ev_share_percent[i]) for i in range(years + 1)}

    # Побудова графіків для часток автомобілів з ДВЗ та електромобілів
    years_range = np.arange(0, years + 1)
    plt.plot(years_range, dvz_share_percent, label="Частка ДВЗ (%)", color='r')
    plt.plot(years_range, ev_share_percent, label="Частка електромобілів (%)", color='g')
    plt.xlabel("Роки")
    plt.ylabel("Частка (%)")
    plt.title("Зміна частки автомобілів з ДВЗ та електромобілів з часом")
    plt.legend()
    plt.grid()
    plt.show()

    print(result)
    return result

