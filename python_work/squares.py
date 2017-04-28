squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)

squares = [value**2 for value in range(1,11)]
print(squares)

print(squares)

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


#Exercise
for value in range(1,21):
	print(value)
	
odd = []
for value in range(1,21,2):
	print(value)

for value in range(3,31,3):
	print(value)

multiple_3 = list(range(3,31,3))
print(multiple_3)

cube = []
for value in range(1,11):
	cube.append(value**3)

print(cube)

cube = [value**3 for value in range(1,11)]
print(cube)
