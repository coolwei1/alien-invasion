motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'proton'
print(motorcycles)

#adding new element to list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('proton')
print(motorcycles)

#Appending Elements to the End of a List
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'proton')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#removing an Item Using the del Statement
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
message = "\nThe last motorcycles I owned was a " + last_owned.title() + "."
print(message)

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
message = "\nThe first motorcycle I owned was " + first_owned.title() + "."
print(message)

#removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
message = "\nA " + too_expensive.title() + " is too expensive for me."
print(message)
