import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.new_emp = Employee('chek wei', 'tan', '100000')
	
	def test_give_default_raise(self):
		annual_salary = self.new_emp.give_raise()

		self.assertEqual(annual_salary, '105000')

	def test_give_custom_raise(self):
		annual_salary = self.new_emp.give_raise(10000)
		self.assertEqual(annual_salary, '110000')

unittest.main()