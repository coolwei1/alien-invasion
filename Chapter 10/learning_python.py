with open('Chapter 10\learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents)

print("\n")

with open('Chapter 10\learning_python.txt') as file_object:
	for line in file_object:
		print(line.rstrip())


with open('Chapter 10\learning_python.txt') as file_object:
	lines = file_object.readlines()

string = ''

for line in lines:
	string += line.strip()

print(string)