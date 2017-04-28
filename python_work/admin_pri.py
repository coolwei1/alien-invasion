from user import User

class Admin(User):
	""" """
	def __init__(self, first_name, last_name, middle_name = ''):
		""" """
		super().__init__(first_name, last_name, middle_name = '')

class Privilages():
	def __init__(self, privileges):
		self.privileges = []

	def show_privileges(*privileges):
		for privilege in privileges:
			print("Ad-min " + privilege)