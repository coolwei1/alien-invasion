#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('shit')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

for my_food in my_foods[:]:
    print(my_food)

for friend_food in friends_foods[:]:
    print(friend_food)

#This doesn't not work
friends_foods = my_foods

my_foods.append('cannoli')
friends_foods.append('shit')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

message = "\nThe first three item in the list are:"
print(message)
print(my_foods[:3])

#pizza
list_pizzas = ['pizza1', 'pizza2', 'pizza3']
friend_pizzas = list_pizzas[:]

list_pizzas.append('pizza4')
friend_pizzas.append('pizza5')

print("\nMy favorite pizzas are:")
for pizza in list_pizzas[:]:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friendpizza in friend_pizzas[:]:
    print(friendpizza)

