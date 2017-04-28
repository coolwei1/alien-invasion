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

class IceCreamStand(Restaurant):
	""""""
	def __init__(self, restaurant_name, cuisine_type, number_served = 0, flavors = ''):
		"""Initialize attributes of the parent class."""
		super().__init__(restaurant_name, cuisine_type, number_served = 0)
		self.flavors = flavors

	def display_flavors(self, *flavors):
		for flavor in flavors:
			print("Our ice cream has flavor " + flavor + ".")

my_restaurant = IceCreamStand('subway', 'western', 0)
my_restaurant.display_flavors('chocolate', 'vanilla', 'apple')
