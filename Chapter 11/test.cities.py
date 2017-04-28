import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):
	"""Test for 'city_functions'"""
	def test_city_country(self):
		"""Does city and country like 'santiago' and 'chile' work?"""
		formatted_location = format_city_country('santiago', 'chile')
		self.assertEqual(formatted_location, "Santiago, Chile.")
	
	def test_city_country_population(self):
		"""Does city, country, population like 'santiago', 'chile' and 5000000 work?"""
		formatted_location = format_city_country('santiago', 'chile', '5000000')
		self.assertEqual(formatted_location, "Santiago, Chile - Population 5000000.")
unittest.main()