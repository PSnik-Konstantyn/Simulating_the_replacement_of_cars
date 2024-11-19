from app.model.Calculations import calculate_transition_matrix, simulate_changing

years = 10
initial_dvz_share = 0.8
initial_ev_share = 0.2

fuel_price = 1.9 # Ціна пального за 100 км
electricity_price = 0.75 # Ціна електроенергії за 100 км
dvz_maintenance_factor = 1.0 # Коефіцієнт обслуговування ДВЗ
ev_maintenance_factor = 0.8 # Коефіцієнт обслуговування електромобіля
dvz_range = 600 # Дальність поїздки на ДВЗ
ev_range = 300 # Дальність поїздки на електромобілі
charging_speed = 50 # Швидкість зарядки
refueling_speed = 300 # Швидкість заправки
ev_subsidy = 5 # Субсидія на електромобілі
dvz_subsidy = 1 # Субсидія на ДВЗ

# Марковська матриця переходів, наприклад
# P[DVZ->DVZ, DVZ->EV, EV->DVZ, EV->EV]
transition_matrix = calculate_transition_matrix(fuel_price, electricity_price, dvz_maintenance_factor, ev_maintenance_factor,
                                dvz_range, ev_range, charging_speed, refueling_speed, ev_subsidy, dvz_subsidy)

simulate_changing (initial_dvz_share, initial_ev_share, years, transition_matrix)
