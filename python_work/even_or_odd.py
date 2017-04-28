number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

#7.1 - 7.3

car = input("Hi, what kind of car you would like to rent? ")
print("Let me see if I can find you a " + car + ".")

seat = input("Hello, how many seat you need? ")
seat = int(seat)

if seat > 8:
    print("Sorry, you guys have to wait for table")
else:
    print("Your table is ready!")

number = input("Enter a number to check whether is multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print("Number " + str(number) + " is multiple of 10.")
else:
    print("Number " + str(number) + " is not multiple of 10.")