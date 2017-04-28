from restaurant import Restaurant

my_restaurant = Restaurant('subway restaurant', 'western')
my_restaurant.describe_restaurant()
my_restaurant.open_reataurant()

my_restaurant.restaurant()
my_restaurant.number_served = 100
my_restaurant.restaurant()

my_restaurant.increment_number_served(20)
my_restaurant.restaurant()

my_restaurant.increment_number_served(50)
my_restaurant.restaurant()