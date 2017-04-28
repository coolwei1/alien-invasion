place = ['China', 'japan', 'korea', 'isreal', 'philippines']
print(place)

print(sorted(place))
print(place)

print(sorted(place, reverse=True))

print(place)

place.reverse()
print(place)

place.reverse()
print(place)

place.sort()
print(place)

place.sort(reverse=True)
print(place)

#all function
cities = ['hong kong', 'bangkok', 'seoul', 'kuala lumpur', 'tokyo', 'beijing', 'jakarta', 'dhaka', 'mumbai', 'karachi', 'ulaanbaatar', 'vientiane', 'hanoi', 'pyongyang', 'astana', 'baku', 'ganja', 'damascus', 'luang prabang', 'darkhan', 'macau', 'dushanbe', 'taipei']

#Accessing Elements in a List
print(cities[5].title())
print(cities[0].title())
print(cities[-1].title())

#Using Individual Values from a List
message = "\nMy favorite city is " + cities[3].title() + " that located in Malaysia."
print(message)

#Modifying Elements in a List
cities[0] = "manila"
print(cities)

#Adding Elements to a List
cities.append('hong kong')
print(cities)

#Inserting Elements into a List
cities.insert(0, 'amman')
print(cities)

#removing an Item Using the del Statement
del cities[0]
print(cities)

#removing an Item Using the pop() Method
popped_cities = cities.pop()
print(cities)
print(popped_cities.title())

#Popping Items from any Position in a List
popped_cities = cities.pop(0)
print(popped_cities)

#removing an Item by Value
cities.remove('kuala lumpur')
print(cities)

#Sorting a List Permanently with the sort() Method
cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

print(len(cities))





