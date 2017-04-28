requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age = 18
print(age == 18)

#Checking Whether a Value Is in a List
requested_topping = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_topping)

print('pepperoni' in requested_topping)

#Checking Whether a Value Is Not in a List
banned_user = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_user:
    print(user.title() + ', you can post a response if you wish.')

requested_topping = ['extra cheese', 'mushrooms']
if 'mushrooms' in requested_topping:
    print("\nAdding mushrooms")

if 'pepperoni' in requested_topping:
    print("\nAdding pepperoni")

if 'extra cheese' in requested_topping:
    print("\nAdding extra cheese")

print("\nFinished making your pizza!!")

#Doesn't work
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("\nAdding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("\nAdding extra cheese.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".\n")

print("\nFinished making your pizza")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".\n")

print("\nFinished making your pizza")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".\n")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushroom', 'olives', 'green peppers',
                      'pepproni', 'pineapple', 'extra cheese']

requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
