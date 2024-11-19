import unittest
import numpy as np
from app.model.Calculations import calculate_transition_matrix, simulate_changing


class TestCalculations(unittest.TestCase):

    def test_transition_matrix_sum(self):
        """Перевіряє, що сума кожного рядка в матриці переходу дорівнює 1."""
        fuel_price = 1.5
        electricity_price = 0.3
        dvz_maintenance_factor = 1.2
        ev_maintenance_factor = 0.8
        dvz_range = 500
        ev_range = 400
        charging_speed = 30
        refueling_speed = 5
        ev_subsidy = 5000
        dvz_subsidy = 2000

        matrix = calculate_transition_matrix(fuel_price, electricity_price, dvz_maintenance_factor,
                                             ev_maintenance_factor,
                                             dvz_range, ev_range, charging_speed, refueling_speed, ev_subsidy,
                                             dvz_subsidy)
        # Перевіряємо, що рядки сумуються до 1
        np.testing.assert_almost_equal(matrix.sum(axis=1), np.array([1.0, 1.0]))

    def test_simulation_results_percentage(self):
        """Перевіряє, що результати симуляції видають відсотки, які сумуються до 100%."""
        years = 10
        initial_dvz_share = 0.8
        initial_ev_share = 0.2
        transition_matrix = np.array([[0.9, 0.1], [0.2, 0.8]])

        result = simulate_changing(initial_dvz_share, initial_ev_share, years, transition_matrix)

        for year, (dvz_percent, ev_percent) in result.items():
            self.assertAlmostEqual(dvz_percent + ev_percent, 100.0, msg=f"Рік {year}: сума часток не дорівнює 100%")

    def test_transition_matrix_reactiveness(self):
        """Перевіряє, що зміна вхідних параметрів змінює матрицю переходу."""
        matrix1 = calculate_transition_matrix(1.5, 0.3, 1.2, 0.8, 500, 400, 30, 5, 5000, 2000)
        matrix2 = calculate_transition_matrix(2.0, 0.5, 1.5, 0.7, 600, 300, 40, 10, 3000, 1000)

        # Матриці повинні бути різними
        self.assertFalse(np.array_equal(matrix1, matrix2), "Матриця не змінюється при зміні параметрів")

    def test_simulation_growth_direction(self):
        """Перевіряє, що частка EV зростає, якщо ймовірність переходу до EV більша."""
        years = 5
        initial_dvz_share = 0.8
        initial_ev_share = 0.2
        transition_matrix = np.array([[0.7, 0.3], [0.1, 0.9]])

        result = simulate_changing(initial_dvz_share, initial_ev_share, years, transition_matrix)
        ev_shares = [ev for _, ev in result.values()]

        # Перевіряємо, що частка EV зростає з роками
        for i in range(1, len(ev_shares)):
            self.assertGreaterEqual(ev_shares[i], ev_shares[i - 1], "Частка EV не зростає")


if __name__ == '__main__':
    unittest.main()
