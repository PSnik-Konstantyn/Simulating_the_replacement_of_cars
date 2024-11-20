from django.test import TestCase, Client
from django.urls import reverse
from app.forms import Form
import json


class CalcViewTests(TestCase):
    def setUp(self):
        # Ініціалізація клієнта
        self.client = Client()
        self.calc_url = reverse('submit')  # Замініть 'calc' на ім'я вашого URL, якщо воно інше

        # Валідні дані
        self.valid_data = {
            'fuel_price': 2.5,
            'electricity_price': 0.1,
            'dvz_maintenance_factor': 1.2,
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500,
            'ev_range': 300,
            'charging_speed': 50,
            'refueling_speed': 10,
            'ev_subsidy': 1000,
            'dvz_subsidy': 500,
            'years': 10,
        }

        # Невалідні дані
        self.invalid_data = {
            'fuel_price': '',  # Пропущене значення
            'electricity_price': 0.1,
            'dvz_maintenance_factor': 1.2,
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500,
            'ev_range': 300,
            'charging_speed': 50,
            'refueling_speed': 10,
            'ev_subsidy': 1000,
            'dvz_subsidy': 500,
            'years': 10,
        }

    def test_calc_view_valid_data(self):
        """Тестуємо обробку валідних даних"""
        response = self.client.post(self.calc_url, data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_calc_view_invalid_data(self):
        """Тестуємо обробку невалідних даних"""
        response = self.client.post(self.calc_url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json())

    def test_calc_view_get_request(self):
        """Тестуємо обробку GET-запиту"""
        response = self.client.get(self.calc_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")  # Перевірка, чи використовується правильний шаблон

    def test_calc_view_missing_fields(self):
        """Тестуємо запит із пропущеними полями"""
        incomplete_data = {
            'fuel_price': 2.5,  # Тільки одне поле
        }
        response = self.client.post(self.calc_url, data=incomplete_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json())
        self.assertIn('electricity_price', response.json()['errors'])  # Перевірка, чи бракує конкретного поля

    def test_calc_view_boundary_values(self):
        """Тестуємо крайні значення полів"""
        boundary_data = {
            'fuel_price': 0,  # Мінімальне значення
            'electricity_price': 100,  # Максимальне значення
            'dvz_maintenance_factor': 0.1,
            'ev_maintenance_factor': 10,
            'dvz_range': 1,
            'ev_range': 10000,
            'charging_speed': 0.1,
            'refueling_speed': 1000,
            'ev_subsidy': 0,
            'dvz_subsidy': 0,
            'years': 1,  # Мінімум років
        }
        response = self.client.post(self.calc_url, data=boundary_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_calc_view_large_years(self):
        """Тестуємо запит із великим значенням для years"""
        large_years_data = self.valid_data.copy()
        large_years_data['years'] = 1000  # Дуже великий період
        response = self.client.post(self.calc_url, data=large_years_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_calc_view_invalid_data_types(self):
        """Тестуємо некоректні типи даних"""
        invalid_type_data = self.valid_data.copy()
        invalid_type_data['fuel_price'] = 'abc'  # Невірний тип
        response = self.client.post(self.calc_url, data=invalid_type_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json())
        self.assertIn('fuel_price', response.json()['errors'])  # Поле, яке спричинило помилку

    def test_calc_view_sql_injection(self):
        """Тестуємо захист від SQL-ін'єкцій"""
        malicious_data = self.valid_data.copy()
        malicious_data['fuel_price'] = "1; DROP TABLE users;"  # Імітація SQL-ін'єкції

        response = self.client.post(self.calc_url, data=malicious_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json())

    def test_calc_view_high_load(self):
        """Тестуємо обробку великої кількості запитів"""
        for _ in range(15):
            response = self.client.post(self.calc_url, data=self.valid_data)
            self.assertEqual(response.status_code, 200)

    def test_home_page_accessible(self):
        """Тестуємо доступність головної сторінки"""
        response = self.client.get(reverse('home'))  # Використовуємо ім'я маршруту
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")  # Перевірка використання правильного шаблону

    def test_submit_page_post(self):
        """Тестуємо обробку POST-запиту через маршрут submit"""
        response = self.client.post(reverse('submit'), data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())  # Перевіряємо, чи результат містить ключ 'result'

    def test_form_valid(self):
        """Тестуємо форму з валідними даними"""
        valid_data = {
            'fuel_price': 2.5,
            'electricity_price': 0.12,
            'dvz_maintenance_factor': 1.0,
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500.0,
            'ev_range': 300.0,
            'charging_speed': 50.0,
            'refueling_speed': 5.0,
            'ev_subsidy': 1000.0,
            'dvz_subsidy': 500.0,
            'years': 10,
        }
        form = Form(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Тестуємо форму з невалідними даними"""
        invalid_data = {
            'fuel_price': 'abc',  # Некоректний тип
            'electricity_price': 0.12,
            'dvz_maintenance_factor': 1.0,
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500.0,
            'ev_range': 300.0,
            'charging_speed': 50.0,
            'refueling_speed': 5.0,
            'ev_subsidy': 1000.0,
            'dvz_subsidy': 500.0,
            'years': 10,
        }
        form = Form(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('fuel_price', form.errors)  # Перевіряємо, чи є помилка для fuel_price

    def test_form_edge_values(self):
        """Тестуємо форму з крайніми значеннями"""
        edge_data = {
            'fuel_price': 0.0,  # Мінімальне значення
            'electricity_price': 0.0,
            'dvz_maintenance_factor': 0.0,
            'ev_maintenance_factor': 0.0,
            'dvz_range': 0.0,
            'ev_range': 0.0,
            'charging_speed': 0.0,
            'refueling_speed': 0.0,
            'ev_subsidy': 0.0,
            'dvz_subsidy': 0.0,
            'years': 50,  # Максимальне значення
        }
        form = Form(data=edge_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_fields(self):
        """Тестуємо форму з відсутніми полями"""
        missing_field_data = {
            'fuel_price': 2.5,
            'electricity_price': 0.12,
            # Відсутнє поле dvz_maintenance_factor
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500.0,
            'ev_range': 300.0,
            'charging_speed': 50.0,
            'refueling_speed': 5.0,
            'ev_subsidy': 1000.0,
            'dvz_subsidy': 500.0,
            'years': 10,
        }
        form = Form(data=missing_field_data)
        self.assertFalse(form.is_valid())
        self.assertIn('dvz_maintenance_factor', form.errors)  # Перевіряємо помилку

    def test_form_years_field(self):
        """Тестуємо, чи поле years приймає тільки цілі числа"""
        invalid_years_data = {
            'fuel_price': 2.5,
            'electricity_price': 0.12,
            'dvz_maintenance_factor': 1.0,
            'ev_maintenance_factor': 0.8,
            'dvz_range': 500.0,
            'ev_range': 300.0,
            'charging_speed': 50.0,
            'refueling_speed': 5.0,
            'ev_subsidy': 1000.0,
            'dvz_subsidy': 500.0,
            'years': 'abc',  # Некоректне значення
        }
        form = Form(data=invalid_years_data)
        self.assertFalse(form.is_valid())
        self.assertIn('years', form.errors)  # Перевіряємо помилку

