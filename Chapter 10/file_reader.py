# Read entire file
with open('Chapter 10\pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

# Read line by line
filename = 'Chapter 10\pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# Make a list of lines from a file
filename = 'Chapter 10\pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Work with file's contents
filename = 'Chapter 10\pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip() #remove newline and whitespace character from each line

print(pi_string)
print(len(pi_string)) #show the length of string

# Large file: one million digits
filename = 'Chapter 10\pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# Is your birthday contained in Pi?
filename = 'Chapter 10\pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	 print("Your birthday does not appear in the first million digits of pi.")