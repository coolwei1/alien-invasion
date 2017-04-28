from random import randint

class Die():
	def __init__(self, side):
		self.side = side

	def roll_die(self):
		i = 0
		while i < 10:
			x = randint(1,self.side)
			j = i+1
			print("Number " + str(j) + " you get is " + str(x))
			i += 1


die_side = input("Enter sides of your die: ")
test = Die(int(die_side))
test.roll_die()