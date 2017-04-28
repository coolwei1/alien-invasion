with open('Chapter 10\learning_python.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.rstrip()
	print(line.replace('C', 'Python'))
	## return a copy!! so replace() must inside print()

