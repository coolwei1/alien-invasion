name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")

def greet_user():
		"""Display a simple greeting."""
		print("Hello")

greet_user()

#
#
#
#
#

def display_message():
		"""Display what I learnt in chapter 8"""
		print("I learnt how to define function in this chapter!")

display_message()

def favorite_book(bookName):
		"""Display user's favorite book"""
		print("One of my favorite book is " + bookName + ".")

bookName = input("Hi, what is your favorite book? ")
favorite_book(bookName)

class User():
	def __init__(self, first_name, last_name, middle_name = ''):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name

		if middle_name:
			self.full_name = first_name + ' ' + middle_name + ' ' + last_name
		else:
			self.full_name = first_name + ' ' + last_name

	def describe_user(self):
		print("Your name is " + self.full_name.title())

	def greet_user(self):
		print("Welcome, " + self.full_name.title())


my_info = User('chek wei' , 'tan')
my_info.describe_user()
my_info.greet_user()

violinist = User('lindsey', 'stirling')
violinist.describe_user()
violinist.greet_user()
