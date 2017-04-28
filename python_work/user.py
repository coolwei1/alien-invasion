class User():
	def __init__(self, first_name, last_name, middle_name = ''):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name

		if middle_name:
			self.full_name = first_name + ' ' + middle_name + ' ' + last_name
		else:
			self.full_name = first_name + ' ' + last_name

	def describe_user(self):
		print("Your name is " + self.full_name.title())

	def greet_user(self):
		print("Welcome, " + self.full_name.title())