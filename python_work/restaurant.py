# page 171 python crash course
class Restaurant():
	"""Simple attempt to describe a restaurant"""
	def __init__(self, restaurant_name, cuisine_type, number_served = 0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	def describe_restaurant(self):
		print(self.restaurant_name.title() + " is a restaurant serve " + self.cuisine_type + " cuisine.")

	def open_reataurant(self):
		print(self.restaurant_name + " is now open!")

	def restaurant(self):
		print("Number of customers served: " + str(self.number_served))

	def increment_number_served(self, served):
		self.number_served += served


# 9.5 Login attempts

class User():
	def __init__(self, first_name, last_name, login_attempts, middle_name = ''):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = login_attempts
		self.middle_name = middle_name

		if middle_name:
			self.full_name = first_name + ' ' + middle_name + ' ' + last_name
		else:
			self.full_name = first_name + ' ' + last_name


	def describe_user(self):
		print("Your name is " + self.full_name.title())

	def greet_user(self):
		print("Welcome, " + self.full_name.title())

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user1 = User('Cool', 'Wei', 0)
user1.increment_login_attempts()
print("You had tried to login in " + str(user1.login_attempts) + " times.")

user1.increment_login_attempts()
print("You had tried to login in " + str(user1.login_attempts) + " times.")

user1.increment_login_attempts()
print("You had tried to login in " + str(user1.login_attempts) + " times.")

user1.reset_login_attempts()
print("You had tried to login in " + str(user1.login_attempts) + " times.")

