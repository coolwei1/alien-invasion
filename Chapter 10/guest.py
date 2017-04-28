## name = input("Enter your name: ")
## 
## with open('Chapter 10\guest.txt',  ##'w') as f:
## 	f.write(name)

while True:
	name = input("Enter your name: ")
	print("Welcome, " + name)
	with open('Chapter 10\guest_book.txt', 'a') as f:
		f.write(name + "\n")