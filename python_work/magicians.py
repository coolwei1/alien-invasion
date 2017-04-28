#looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

#Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print("\n" + magician.title() + ", that was a good trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

#Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")
