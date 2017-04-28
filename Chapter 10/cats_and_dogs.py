filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		print(filename + " not found!")
		# pass
	else:
		print(contents)