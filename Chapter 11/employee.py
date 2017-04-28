class Employee():
	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = int(annual_salary)

	def give_raise(self, sal_raise=''):
		if sal_raise:
			self.annual_salary += int(sal_raise)
			self.annual_salary = str(self.annual_salary)
			return self.annual_salary
		else:
			self.annual_salary += 5000
			self.annual_salary = str(self.annual_salary)
			return self.annual_salary
