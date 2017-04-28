import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and stored it.

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		while True:
			yesORno = input("Is your username is " + username + "? (y/n) ")
			if yesORno.lower() == 'n':
				username = get_new_username()
				print("We'll remember you when you come back, " + username + "!")
				break
			elif yesORno.lower() == 'y':
				print("Welcome back, " + username + "!")
				break
			else:
				print("Enter 'n' or 'y' only!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()