
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		# msg = "Sorry, the file " + filename + " does not exist."
		pass
		# print(msg)
	else:
		# Count the approximate number of words in	 the file.
		words = contents.split()
		num_words = len(words)

		# Count occurrence of 'the' word
		the_count = contents.lower().count('the')

		print("The file " + filename + " has about " + str(num_words) + " words.")
		print("There are " + str(the_count) + " times occurrence of 'the' word in " + filename + ".")
	
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
	count_words(filename)

