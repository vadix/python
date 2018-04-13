import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Тесты для 'city_functions.py'."""

    def test_city(self):
        """проверяет отформатированную строку Santiago, Chile"""
        city_name = get_formatted_city('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago, Chile')

    def test_city_population(self):
        """проверяет отформатированную строку Santiago, Chile"""
        city_name = get_formatted_city('santiago', 'chile', '5000')
        self.assertEqual(city_name,  'Santiago, Chile — Population 5000')

unittest.main()
